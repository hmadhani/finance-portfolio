#!/usr/bin/env python3
"""
Portfolio XLS Report Generator — finance-portfolio (isolated, market-data-only)

Generates a quarterly or annual performance workbook from portfolio.md's
current state, framed as prepared for "Investor: Mr. Spock — Logical
Investor" (see investor-profile.md). Self-contained: no dependency on any
file outside this repo, since the cloud routine that runs this only has
finance-portfolio checked out.

--data-json schema (all fields required unless noted):
{
  "portfolio_data": {
    "nav": float,
    "total_return_pct": float,
    "glide_path_phase": str,
    "cycle_number": int,
    "holdings": [{"ticker": str, "type": str, "theme": str, "shares": number,
                  "mkt_value": float, "pct_nav": float, "unrealized_gl": float}, ...],
    "trades": [{"date": "YYYY-MM-DD", "ticker": str, "action": str, "rationale": str}, ...],
    "theme_exposure": [{"theme": str, "pct_nav": float}, ...],
    "return_trend": [{"date": "YYYY-MM-DD", "nav": float,
                       "blended_benchmark": float (optional), "spy": float (optional)}, ...]
  },
  "benchmark_data": {"blended_return_pct": float, "spy_return_pct": float}
}

return_trend needs one point per cycle since the last report at minimum
(ideally since inception) to plot a real trend line — portfolio.md's trade
log is the source for this; see DECISION.md if a dedicated NAV-history table
becomes necessary. blended_benchmark/spy per point are optional (omit if not
tracked historically) — the chart will still render with NAV alone.
"""

import argparse
from typing import Dict, List, Any

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.chart import LineChart, PieChart, BarChart, Reference
    from openpyxl.chart.label import DataLabelList
    from openpyxl.chart.marker import Marker
    from openpyxl.drawing.colors import ColorChoice
    from openpyxl.chart.legend import Legend
    from openpyxl.formatting.rule import CellIsRule, DataBarRule
except ImportError:
    print("openpyxl not found. Install with: pip install openpyxl --break-system-packages")
    exit(1)


# ---------------------------------------------------------------------------
# Style palette — a single, consistent theme reused across every sheet.
# ---------------------------------------------------------------------------
NAVY = "1F3864"
BLUE = "2F5496"
LIGHT_BLUE = "D6E4F0"
ACCENT_GREEN = "2E7D32"
ACCENT_RED = "C62828"
BAND_FILL = "F2F6FB"
GRID = "B9C6D6"

TITLE_FONT = Font(bold=True, size=20, color=NAVY, name="Calibri")
SECTION_FONT = Font(bold=True, size=13, color=BLUE, name="Calibri")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11, name="Calibri")
HEADER_FILL = PatternFill(start_color=BLUE, end_color=BLUE, fill_type="solid")
SUBHEADER_FILL = PatternFill(start_color=LIGHT_BLUE, end_color=LIGHT_BLUE, fill_type="solid")
BAND_PATTERN = PatternFill(start_color=BAND_FILL, end_color=BAND_FILL, fill_type="solid")
TOTAL_FILL = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
TOTAL_FONT = Font(bold=True, color="FFFFFF")

CURRENCY_FORMAT = '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'
PERCENT_FORMAT = '0.00%'
NUMBER_FORMAT = '#,##0.00'

THIN = Side(style='thin', color=GRID)
THIN_BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HEADER_BORDER = Border(left=Side(style='thin', color="FFFFFF"), right=Side(style='thin', color="FFFFFF"),
                        top=Side(style='thin', color="FFFFFF"), bottom=Side(style='medium', color=NAVY))


def apply_header_style(cell):
    cell.font = HEADER_FONT
    cell.fill = HEADER_FILL
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = HEADER_BORDER


def apply_subheader_style(cell):
    cell.font = Font(bold=True, color=NAVY)
    cell.fill = SUBHEADER_FILL
    cell.border = THIN_BORDER


def apply_data_style(cell, band=False, number_format=None, bold=False, align=None):
    cell.border = THIN_BORDER
    if band:
        cell.fill = BAND_PATTERN
    if number_format:
        cell.number_format = number_format
    if bold:
        cell.font = Font(bold=True)
    if align:
        cell.alignment = Alignment(horizontal=align)


def apply_total_row(ws, row, num_cols):
    for c in range(1, num_cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = TOTAL_FILL
        cell.font = TOTAL_FONT
        cell.border = THIN_BORDER


def signed_gl_color(value):
    if value is None:
        return None
    return ACCENT_GREEN if value >= 0 else ACCENT_RED


def auto_column_width(ws, min_width=10, max_width=50):
    for column in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)
        for cell in column:
            try:
                if cell.value is not None and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except Exception:
                pass
        adjusted_width = min(max(max_length + 2, min_width), max_width)
        ws.column_dimensions[column_letter].width = adjusted_width


def freeze_header(ws, cell="A2"):
    ws.freeze_panes = cell


# ---------------------------------------------------------------------------
# Sheets
# ---------------------------------------------------------------------------

def create_cover_sheet(wb: Workbook, portfolio_data: Dict, period_label: str) -> None:
    """Cover sheet framing the report as prepared for the Mr. Spock investor profile."""
    ws = wb.create_sheet("Cover", 0)
    ws.sheet_view.showGridLines = False

    for col, width in zip("ABCDE", [4, 26, 26, 26, 4]):
        ws.column_dimensions[col].width = width

    ws.merge_cells('B2:D2')
    ws['B2'] = "PORTFOLIO PERFORMANCE REPORT"
    ws['B2'].font = TITLE_FONT
    ws['B2'].alignment = Alignment(horizontal='center')

    ws.merge_cells('B3:D3')
    ws['B3'] = period_label
    ws['B3'].font = Font(italic=True, size=12, color=BLUE)
    ws['B3'].alignment = Alignment(horizontal='center')

    # Banner band
    for row in (2, 3):
        for col in ("A", "E"):
            ws[f"{col}{row}"].fill = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")

    ws.merge_cells('B5:D5')
    ws['B5'] = "Prepared for: Mr. Spock — Logical Investor"
    ws['B5'].font = Font(bold=True, size=13, color=NAVY)
    ws['B5'].alignment = Alignment(horizontal='center')

    ws.merge_cells('B6:D9')
    ws['B6'] = (
        "A hypothetical growth-oriented investor in the accumulation phase, "
        "governed by a fixed sizing table, a 25% theme-concentration cap, and "
        "a wall-clock-derived glide path. See investor-profile.md for the full "
        "mandate. Zero real personal data underlies this profile."
    )
    ws['B6'].alignment = Alignment(wrap_text=True, vertical='top', horizontal='center')
    ws['B6'].font = Font(italic=True, color="555555")

    # Snapshot KPI cards
    kpi_row = 11
    kpis = [
        ("NAV", portfolio_data.get('nav'), CURRENCY_FORMAT),
        ("Glide-Path Phase", portfolio_data.get('glide_path_phase', 'N/A'), None),
        ("Cycle #", portfolio_data.get('cycle_number', 'N/A'), None),
    ]
    for i, (label, value, fmt) in enumerate(kpis):
        col = chr(ord('B') + i)
        cell_label = ws[f"{col}{kpi_row}"]
        cell_label.value = label
        cell_label.font = Font(bold=True, size=10, color="FFFFFF")
        cell_label.fill = PatternFill(start_color=BLUE, end_color=BLUE, fill_type="solid")
        cell_label.alignment = Alignment(horizontal='center')
        cell_label.border = THIN_BORDER

        cell_val = ws[f"{col}{kpi_row + 1}"]
        cell_val.value = value
        cell_val.font = Font(bold=True, size=14, color=NAVY)
        cell_val.fill = PatternFill(start_color=LIGHT_BLUE, end_color=LIGHT_BLUE, fill_type="solid")
        cell_val.alignment = Alignment(horizontal='center')
        cell_val.border = THIN_BORDER
        if fmt:
            cell_val.number_format = fmt
        ws.row_dimensions[kpi_row + 1].height = 24

    disclaimer_row = kpi_row + 4
    ws.merge_cells(f'B{disclaimer_row}:D{disclaimer_row + 4}')
    dc = ws.cell(row=disclaimer_row, column=2, value=(
        "IMPORTANT: This is a paper/model portfolio for evaluation purposes "
        "only, tracked with public market data alone (no personal financial "
        "context). It does not constitute investment advice or a "
        "recommendation to buy or sell any security. All investments involve "
        "risk, including potential loss of principal. Always consult with "
        "qualified financial professionals before making investment decisions."
    ))
    dc.alignment = Alignment(wrap_text=True, vertical='top')
    dc.font = Font(size=9, italic=True, color="777777")

    ws.row_dimensions[2].height = 30


def create_summary_sheet(wb: Workbook, portfolio_data: Dict, benchmark_data: Dict) -> None:
    """NAV, return vs. blended benchmark vs. SPY, sleeve drift."""
    ws = wb.create_sheet("Summary")
    ws.sheet_view.showGridLines = False

    ws['A1'] = "SUMMARY"
    ws['A1'].font = SECTION_FONT
    ws.row_dimensions[1].height = 22

    headers = ["Metric", "This Portfolio", "Blended Benchmark", "SPY"]
    for col, h in enumerate(headers, start=1):
        apply_header_style(ws.cell(row=3, column=col, value=h))

    rows = [
        ("NAV", portfolio_data.get('nav'), None, None, CURRENCY_FORMAT),
        ("Period Return %", portfolio_data.get('period_return_pct'),
         benchmark_data.get('blended_return_pct'), benchmark_data.get('spy_return_pct'), PERCENT_FORMAT),
        ("Since-Inception Return %", portfolio_data.get('inception_return_pct'),
         benchmark_data.get('blended_inception_return_pct'), benchmark_data.get('spy_inception_return_pct'), PERCENT_FORMAT),
    ]
    r = 4
    for i, (label, this_val, bench_val, spy_val, fmt) in enumerate(rows):
        band = i % 2 == 1
        c1 = ws.cell(row=r, column=1, value=label)
        c1.font = Font(bold=True)
        apply_data_style(c1, band=band)
        for col, val in zip((2, 3, 4), (this_val, bench_val, spy_val)):
            cell = ws.cell(row=r, column=col, value=val)
            apply_data_style(cell, band=band, number_format=fmt, align='right')
        r += 1

    r += 2
    ws.cell(row=r, column=1, value="SLEEVE DRIFT VS. TARGET").font = SECTION_FONT
    r += 1
    headers2 = ["Sleeve", "Target %", "Current %", "Drift"]
    for col, h in enumerate(headers2, start=1):
        apply_header_style(ws.cell(row=r, column=col, value=h))
    r += 1
    drift_start = r
    for i, sleeve in enumerate(portfolio_data.get('sleeve_drift', [])):
        band = i % 2 == 1
        drift = sleeve['current_pct'] - sleeve['target_pct']
        c1 = ws.cell(row=r, column=1, value=sleeve['name'])
        apply_data_style(c1, band=band)
        c2 = ws.cell(row=r, column=2, value=sleeve['target_pct'])
        apply_data_style(c2, band=band, number_format=PERCENT_FORMAT, align='right')
        c3 = ws.cell(row=r, column=3, value=sleeve['current_pct'])
        apply_data_style(c3, band=band, number_format=PERCENT_FORMAT, align='right')
        c4 = ws.cell(row=r, column=4, value=drift)
        apply_data_style(c4, band=band, number_format='+0.00%;-0.00%', align='right')
        c4.font = Font(color=signed_gl_color(drift) or "000000", bold=True)
        r += 1
    drift_end = r - 1

    if drift_end >= drift_start:
        ws.conditional_formatting.add(
            f"D{drift_start}:D{drift_end}",
            DataBarRule(start_type='num', start_value=-0.15, end_type='num', end_value=0.15,
                        color="F4B183", showValue=True)
        )

        # Sleeve drift bar chart, well clear of the table (starts 3 cols right of it)
        chart = BarChart()
        chart.type = "col"
        chart.title = "Sleeve Allocation: Target vs. Current"
        chart.style = 10
        chart.y_axis.title = "% of NAV"
        chart.y_axis.numFmt = '0%'
        chart.width, chart.height = 16, 9
        cats = Reference(ws, min_col=1, min_row=drift_start, max_row=drift_end)
        data = Reference(ws, min_col=2, max_col=3, min_row=drift_start - 1, max_row=drift_end)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.legend.position = 'b'
        ws.add_chart(chart, f"F{drift_start - 1}")

    freeze_header(ws, "A4")
    auto_column_width(ws)


def create_holdings_sheet(wb: Workbook, holdings: List[Dict]) -> None:
    """Current positions + theme tags."""
    ws = wb.create_sheet("Holdings")
    ws.sheet_view.showGridLines = False

    ws['A1'] = "HOLDINGS"
    ws['A1'].font = SECTION_FONT
    ws.row_dimensions[1].height = 22

    headers = ["Ticker", "Type", "Theme", "Shares", "Entry Price", "Current Price", "Mkt Value", "% NAV", "Unrealized G/L"]
    header_row = 3
    for col, h in enumerate(headers, start=1):
        apply_header_style(ws.cell(row=header_row, column=col, value=h))

    total_mkt_value = 0.0
    r = header_row + 1
    for i, h in enumerate(holdings):
        band = i % 2 == 1
        vals = [h['ticker'], h['type'], h['theme'], h.get('shares'), h.get('entry_price'),
                h.get('current_price'), h['mkt_value'], h['pct_nav'], h.get('unrealized_gl')]
        fmts = [None, None, None, NUMBER_FORMAT, CURRENCY_FORMAT, CURRENCY_FORMAT,
                CURRENCY_FORMAT, PERCENT_FORMAT, CURRENCY_FORMAT]
        for col, (val, fmt) in enumerate(zip(vals, fmts), start=1):
            cell = ws.cell(row=r, column=col, value=val)
            align = 'right' if col >= 4 else 'left'
            apply_data_style(cell, band=band, number_format=fmt, align=align)
            if col == 9 and val is not None:
                cell.font = Font(color=signed_gl_color(val))
        total_mkt_value += h.get('mkt_value') or 0
        r += 1

    total_row = r
    ws.cell(row=total_row, column=1, value="TOTAL")
    ws.cell(row=total_row, column=7, value=total_mkt_value).number_format = CURRENCY_FORMAT
    ws.cell(row=total_row, column=8, value=sum(h.get('pct_nav') or 0 for h in holdings)).number_format = PERCENT_FORMAT
    apply_total_row(ws, total_row, len(headers))

    # Mkt Value by theme pie, positioned safely below the table
    ws.conditional_formatting.add(
        f"I{header_row + 1}:I{total_row - 1}",
        CellIsRule(operator='lessThan', formula=['0'], font=Font(color=ACCENT_RED))
    )

    freeze_header(ws, "A4")
    auto_column_width(ws)


def create_trade_log_sheet(wb: Workbook, trades: List[Dict]) -> None:
    """Period's trades with rationale."""
    ws = wb.create_sheet("Trade Log")
    ws.sheet_view.showGridLines = False

    ws['A1'] = "TRADE LOG"
    ws['A1'].font = SECTION_FONT
    ws.row_dimensions[1].height = 22

    headers = ["Date", "Ticker", "Action", "Shares", "Price", "Rationale"]
    header_row = 3
    for col, h in enumerate(headers, start=1):
        apply_header_style(ws.cell(row=header_row, column=col, value=h))

    action_colors = {"BUY": ACCENT_GREEN, "SELL": ACCENT_RED, "TRIM": "E67E22", "HOLD": "777777"}

    r = header_row + 1
    for i, t in enumerate(trades):
        band = i % 2 == 1
        c1 = ws.cell(row=r, column=1, value=t['date'])
        apply_data_style(c1, band=band)
        c2 = ws.cell(row=r, column=2, value=t['ticker'])
        apply_data_style(c2, band=band, bold=True)
        c3 = ws.cell(row=r, column=3, value=t['action'])
        apply_data_style(c3, band=band, align='center')
        c3.font = Font(bold=True, color=action_colors.get(str(t['action']).upper(), "333333"))
        c4 = ws.cell(row=r, column=4, value=t.get('shares'))
        apply_data_style(c4, band=band, number_format=NUMBER_FORMAT, align='right')
        c5 = ws.cell(row=r, column=5, value=t.get('price'))
        apply_data_style(c5, band=band, number_format=CURRENCY_FORMAT, align='right')
        c6 = ws.cell(row=r, column=6, value=t['rationale'])
        c6.alignment = Alignment(wrap_text=True, vertical='top')
        c6.border = THIN_BORDER
        if band:
            c6.fill = BAND_PATTERN
        ws.row_dimensions[r].height = 30
        r += 1

    ws.column_dimensions['F'].width = 90
    freeze_header(ws, "A4")
    auto_column_width(ws, max_width=20)


def create_charts_sheet(wb: Workbook, theme_exposure: List[Dict], return_trend: List[Dict]) -> None:
    """Theme-exposure pie and NAV/benchmark return-trend line, laid out with
    generous non-overlapping regions (data tables on the left, charts anchored
    far enough right/down that neither chart's rendered bounding box can
    collide with the other's)."""
    ws = wb.create_sheet("Charts")
    ws.sheet_view.showGridLines = False

    ws['A1'] = "CHARTS"
    ws['A1'].font = SECTION_FONT
    ws.row_dimensions[1].height = 22

    # --- Theme exposure data table (rows 3..) ---
    theme_header_row = 3
    apply_header_style(ws.cell(row=theme_header_row, column=1, value="Theme"))
    apply_header_style(ws.cell(row=theme_header_row, column=2, value="% NAV"))
    for i, t in enumerate(theme_exposure):
        r = theme_header_row + 1 + i
        band = i % 2 == 1
        c1 = ws.cell(row=r, column=1, value=t['theme'])
        apply_data_style(c1, band=band)
        c2 = ws.cell(row=r, column=2, value=t['pct_nav'])
        apply_data_style(c2, band=band, number_format=PERCENT_FORMAT, align='right')
    theme_last_row = theme_header_row + len(theme_exposure)

    pie = PieChart()
    pie.title = "Theme Exposure (% NAV)"
    pie.style = 26
    pie.width, pie.height = 16, 10
    data = Reference(ws, min_col=2, min_row=theme_header_row, max_row=theme_last_row)
    labels = Reference(ws, min_col=1, min_row=theme_header_row + 1, max_row=theme_last_row)
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    pie.dataLabels = DataLabelList()
    pie.dataLabels.showPercent = True
    pie.legend.position = 'r'
    # Anchor well clear of the data table (table maxes out around column B).
    ws.add_chart(pie, "D3")

    # --- Return trend data table, placed a fixed, generous distance below the
    # theme table AND below where the pie chart's bounding box ends (pie is
    # 10cm tall ≈ 20 rows at default row height, anchored at row 3) so the two
    # charts can never overlap regardless of how many themes/points exist. ---
    trend_start_row = max(theme_last_row, 3 + 20) + 3
    apply_header_style(ws.cell(row=trend_start_row, column=1, value="Cycle Date"))
    apply_header_style(ws.cell(row=trend_start_row, column=2, value="NAV"))
    apply_header_style(ws.cell(row=trend_start_row, column=3, value="Blended Benchmark"))
    apply_header_style(ws.cell(row=trend_start_row, column=4, value="SPY"))
    for i, point in enumerate(return_trend):
        r = trend_start_row + 1 + i
        band = i % 2 == 1
        c1 = ws.cell(row=r, column=1, value=point['date'])
        apply_data_style(c1, band=band)
        c2 = ws.cell(row=r, column=2, value=point['nav'])
        apply_data_style(c2, band=band, number_format=CURRENCY_FORMAT, align='right')
        c3 = ws.cell(row=r, column=3, value=point.get('blended_benchmark'))
        apply_data_style(c3, band=band, number_format=CURRENCY_FORMAT, align='right')
        c4 = ws.cell(row=r, column=4, value=point.get('spy'))
        apply_data_style(c4, band=band, number_format=NUMBER_FORMAT, align='right')
    trend_last_row = trend_start_row + len(return_trend)

    line = LineChart()
    line.title = "Return Trend"
    line.style = 12
    line.width, line.height = 22, 10
    line.y_axis.title = "Value"
    line.x_axis.title = "Cycle Date"
    data = Reference(ws, min_col=2, max_col=4, min_row=trend_start_row, max_row=trend_last_row)
    cats = Reference(ws, min_col=1, min_row=trend_start_row + 1, max_row=trend_last_row)
    line.add_data(data, titles_from_data=True)
    line.set_categories(cats)
    for series in line.series:
        series.marker = Marker(symbol='circle', size=5)
        series.smooth = False
    line.legend.position = 'b'
    # Anchored below the pie chart's row range (pie ends well before
    # trend_start_row by construction above), so this can't overlap it either.
    ws.add_chart(line, f"D{trend_start_row}")

    auto_column_width(ws)


def create_portfolio_performance_report(
    portfolio_data: Dict[str, Any],
    benchmark_data: Dict[str, Any],
    period_label: str,
    output_path: str,
) -> str:
    """Build the full quarterly/annual workbook. Returns output_path."""
    wb = Workbook()
    wb.remove(wb.active)

    create_cover_sheet(wb, portfolio_data, period_label)
    create_summary_sheet(wb, portfolio_data, benchmark_data)
    create_holdings_sheet(wb, portfolio_data['holdings'])
    create_trade_log_sheet(wb, portfolio_data['trades'])
    create_charts_sheet(wb, portfolio_data['theme_exposure'], portfolio_data['return_trend'])

    wb.save(output_path)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate finance-portfolio XLS performance report")
    parser.add_argument("--period", required=True, help="Period label, e.g. 2026-Q3 or 2026-annual")
    parser.add_argument("--output", required=True, help="Output .xlsx path")
    parser.add_argument("--data-json", required=True, help="Path to a JSON file with portfolio_data + benchmark_data (produced by the routine from portfolio.md)")
    args = parser.parse_args()

    import json
    with open(args.data_json) as f:
        payload = json.load(f)

    path = create_portfolio_performance_report(
        payload['portfolio_data'], payload['benchmark_data'], args.period, args.output
    )
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

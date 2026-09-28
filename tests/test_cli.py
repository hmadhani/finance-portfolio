import json
import os
import subprocess
import sys
import tempfile
import unittest

from tests.helpers import make_chain, write_fixture_dir

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLI = os.path.join(REPO, "scripts", "options_data.py")


class TestCli(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = os.path.join(self.tmp.name, "fx")
        write_fixture_dir(self.fx, {"TEST": make_chain(strikes=range(70, 131, 1), width=0.04),
                                    "ETF1": make_chain(symbol="ETF1", spot=50.0, strikes=range(40, 61, 1)),
                                    "SPY": make_chain(symbol="SPY", strikes=range(70, 131, 1), width=0.04)})
        self.env = dict(os.environ, OPTIONS_FIXTURE_DIR=self.fx)

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *args, expect=0):
        p = subprocess.run([sys.executable, CLI, "--asof", "2026-09-28", *args],
                           capture_output=True, text=True, env=self.env)
        self.assertEqual(p.returncode, expect, p.stderr)
        return json.loads(p.stdout) if expect == 0 else p

    def test_regime(self):
        r = self.run_cli("regime")
        self.assertEqual(r["vix"], 15.0)
        self.assertEqual(r["term_structure"], "contango")
        self.assertFalse(r["stress"])
        self.assertIn("vix_percentile_1y", r)
        self.assertEqual(r["bxm"], 2560.6)

    def test_scan(self):
        ivp = os.path.join(self.tmp.name, "iv.csv")
        r = self.run_cli("scan", "--symbols", "TEST,MISSING", "--iv-history", ivp)
        ok, bad = r["results"]
        self.assertEqual(ok["symbol"], "TEST")
        self.assertAlmostEqual(ok["iv30_pct"], 20.0)
        self.assertIsNone(ok["iv_rank"]["iv_rank"])
        self.assertTrue(ok["candidates"])
        self.assertIn("error", bad)

    def test_price_spread(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "2",
                         "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        self.assertEqual(r["credit_or_debit"], "credit")
        self.assertIn("*", r["payoff_ascii"])
        tpl = r["position_template"]
        self.assertEqual(tpl["qty"], 2)
        self.assertEqual(tpl["entry_cost"], r["entry_cost_per_share"])
        self.assertEqual(tpl["legs"][0]["option"], "TEST261106P00095000")

    def test_price_spread_bad_strike_is_usage_error(self):
        p = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 95.5 2026-11-06", expect=2)
        self.assertIn("no quote", p.stderr)

    def test_record_iv_then_mark(self):
        ivp = os.path.join(self.tmp.name, "iv.csv")
        r = self.run_cli("record-iv", "--symbols", "TEST,ETF1", "--iv-history", ivp)
        self.assertEqual(r["appended"], 2)
        self.assertEqual(self.run_cli("record-iv", "--symbols", "TEST", "--iv-history", ivp)["appended"], 0)

        pos_path = os.path.join(self.tmp.name, "positions.json")
        tpl = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                           "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")["position_template"]
        tpl["id"] = "T1"
        with open(pos_path, "w") as f:
            json.dump({"positions": [tpl]}, f)
        m = self.run_cli("mark", "--positions", pos_path)["marks"][0]
        self.assertEqual(m["id"], "T1")
        self.assertLess(m["pnl"], 0)          # just paid slippage: marked at mid, below fill
        self.assertEqual(m["dte"], 39)

    def test_mark_empty(self):
        pos_path = os.path.join(self.tmp.name, "positions.json")
        with open(pos_path, "w") as f:
            json.dump({"positions": []}, f)
        self.assertEqual(self.run_cli("mark", "--positions", pos_path)["marks"], [])

    def test_mark_isolates_per_symbol_chain_failure(self):
        pos_path = os.path.join(self.tmp.name, "positions.json")
        tpl = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                           "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")["position_template"]
        tpl["id"] = "T1"
        bad = json.loads(json.dumps(tpl))
        bad["id"] = "T2"
        bad["symbol"] = "MISSING"
        with open(pos_path, "w") as f:
            json.dump({"positions": [tpl, bad]}, f)
        r = self.run_cli("mark", "--positions", pos_path)
        by_id = {m["id"]: m for m in r["marks"]}
        self.assertEqual(len(by_id), 2)
        self.assertNotIn("error", by_id["T1"])
        self.assertLess(by_id["T1"]["pnl"], 0)
        self.assertIn("error", by_id["T2"])
        self.assertEqual(by_id["T2"]["symbol"], "MISSING")

    def test_regime_reports_no_errors_when_all_sources_load(self):
        r = self.run_cli("regime")
        self.assertEqual(r["errors"], [])
        self.assertEqual(r["put"], 3675.7)

    def test_regime_broken_vix_history_is_partial(self):
        with open(os.path.join(self.fx, "VIX_History.csv"), "w") as f:
            f.write("<!DOCTYPE html><html><body>Access Denied</body></html>\n")
        r = self.run_cli("regime")
        self.assertIsNone(r["vix_percentile_1y"])
        self.assertEqual([e["field"] for e in r["errors"]], ["vix_percentile_1y"])
        self.assertEqual(r["vix"], 15.0)
        self.assertEqual(r["term_structure"], "contango")
        self.assertFalse(r["stress"])
        self.assertEqual(r["bxm"], 2560.6)

    def test_regime_missing_vix3m_makes_stress_unknown(self):
        os.remove(os.path.join(self.fx, "_VIX3M.json"))
        r = self.run_cli("regime")
        self.assertIsNone(r["vix3m"])
        self.assertIsNone(r["term_structure"])
        self.assertIsNone(r["stress"])
        self.assertEqual(sorted(e["field"] for e in r["errors"]), ["stress", "term_structure", "vix3m"])
        self.assertIsNotNone(r["vix_percentile_1y"])

    def test_regime_missing_vix_nulls_dependents(self):
        os.remove(os.path.join(self.fx, "_VIX.json"))
        r = self.run_cli("regime")
        for k in ("vix", "term_structure", "stress", "vix_percentile_1y"):
            self.assertIsNone(r[k], k)
        self.assertEqual(sorted(e["field"] for e in r["errors"]),
                         ["stress", "term_structure", "vix", "vix_percentile_1y"])
        self.assertEqual(r["vix3m"], 17.0)

    def test_regime_nothing_fetched_exits_nonzero(self):
        for name in ("_VIX.json", "_VIX3M.json", "_BXM.json", "_PUT.json", "VIX_History.csv"):
            os.remove(os.path.join(self.fx, name))
        p = self.run_cli("regime", expect=1)
        self.assertIn("no regime data", p.stderr)

    def test_price_spread_leg_quotes_and_liquidity(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        short, long_ = r["fills"]
        for k in ("bid", "ask", "mid", "delta", "open_interest", "liquid"):
            self.assertIn(k, short)
        self.assertEqual((short["bid"], short["ask"], short["mid"]), (0.68, 0.72, 0.7))
        self.assertEqual(short["open_interest"], 1000)
        self.assertLess(short["delta"], 0)
        self.assertTrue(short["liquid"])
        self.assertFalse(long_["liquid"])          # 0.04 wide on a 0.12 mid > 10%
        self.assertFalse(r["all_legs_liquid"])
        self.assertEqual(r["uncovered_short_puts"], 0)

    def test_price_spread_all_legs_liquid(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 100 2026-11-06; BUY 1 P 95 2026-11-06")
        self.assertTrue(r["all_legs_liquid"])

    def test_price_spread_etf_abs_spread_override(self):
        r = self.run_cli("price-spread", "--symbol", "SPY", "--qty", "1",
                         "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        self.assertTrue(r["fills"][1]["liquid"])   # $0.04 wide <= $0.05 ETF override
        self.assertTrue(r["all_legs_liquid"])

    def test_price_spread_stock_leg_exempt_from_liquidity(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1", "--with-stock",
                         "--legs", "SELL 1 C 105 2026-11-06")
        stock = [f for f in r["fills"] if f["option"] == "STOCK"][0]
        self.assertIsNone(stock["liquid"])
        self.assertTrue(r["all_legs_liquid"])
        self.assertTrue(r["defined_risk"])

    def test_price_spread_csp_reports_uncovered_short_put(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 95 2026-11-06")
        self.assertEqual(r["uncovered_short_puts"], 1)

    def test_position_template_carries_max_loss(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "2",
                         "--legs", "SELL 1 P 100 2026-11-06; BUY 1 P 95 2026-11-06")
        self.assertEqual(r["position_template"]["max_loss"], r["max_loss"])
        self.assertLess(r["position_template"]["max_loss"], 0)

    def test_usage_error_message_is_unquoted(self):
        p = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 95.5 2026-11-06", expect=2)
        self.assertTrue(p.stderr.startswith("error: no quote for TEST"), p.stderr)

    def test_price_spread_zero_ratio_is_usage_error(self):
        p = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 0 P 95 2026-11-06", expect=2)
        self.assertIn("ratio", p.stderr)

    def test_price_spread_zero_zero_quote_is_usage_error(self):
        chain = make_chain(strikes=range(70, 131, 1), width=0.04)
        for o in chain["data"]["options"]:
            if o["option"] == "TEST261106P00095000":
                o["bid"], o["ask"] = 0.0, 0.0
        write_fixture_dir(self.fx, {"TEST": chain})
        p = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06", expect=2)
        self.assertIn("no valid quote", p.stderr)

    def test_price_spread_qty_zero_is_usage_error(self):
        self.run_cli("price-spread", "--symbol", "TEST", "--qty", "0",
                     "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06", expect=2)

    def test_price_spread_negative_qty_is_usage_error(self):
        self.run_cli("price-spread", "--symbol", "TEST", "--qty", "-1",
                     "--legs", "BUY 1 C 105 2026-11-06", expect=2)


if __name__ == "__main__":
    unittest.main()

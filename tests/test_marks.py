import unittest
from datetime import date

from tests.helpers import make_contract
from optlib import marks

ASOF = date(2026, 9, 28)


def pcs_position(entry_cost=-1.00, target=50):
    return {"id": "P1", "symbol": "TEST", "strategy": "credit_put_spread", "opened": "2026-09-01",
            "qty": 2, "entry_cost": entry_cost, "profit_target_pct": target,
            "legs": [{"action": "SELL", "ratio": 1, "option": "TEST261106P00095000"},
                     {"action": "BUY", "ratio": 1, "option": "TEST261106P00090000"}]}


def idx(short_bid, short_ask, long_bid, long_ask, exp="261106"):
    s = make_contract(f"TEST{exp}P00095000", short_bid, short_ask)
    l = make_contract(f"TEST{exp}P00090000", long_bid, long_ask)
    return {s.option: s, l.option: l}


class TestMarks(unittest.TestCase):
    def test_credit_profit_target(self):
        m = marks.mark_position(pcs_position(), idx(0.55, 0.65, 0.15, 0.25), 100.0, ASOF)
        # value = -0.60 + 0.20 = -0.40 ; pnl = (-0.40 - -1.00) * 100 * 2 = 120 ; basis 200 -> 60%
        self.assertAlmostEqual(m["pnl"], 120.0)
        self.assertAlmostEqual(m["pct_of_basis"], 60.0)
        self.assertIn("profit_target", m["triggers"])
        self.assertNotIn("21_dte", m["triggers"])
        self.assertEqual(m["dte"], 39)

    def test_credit_stop_loss(self):
        m = marks.mark_position(pcs_position(), idx(3.95, 4.05, 0.95, 1.05), 100.0, ASOF)
        # value = -4.00 + 1.00 = -3.00 ; pnl = -2.00*200 = -400 ; basis 200 -> stop at -400
        self.assertAlmostEqual(m["pnl"], -400.0)
        self.assertIn("stop_loss", m["triggers"])

    def test_21_dte(self):
        m = marks.mark_position(pcs_position(), idx(0.9, 1.0, 0.2, 0.3), 100.0, date(2026, 10, 17))
        self.assertEqual(m["dte"], 20)
        self.assertIn("21_dte", m["triggers"])

    def test_debit_stop(self):
        pos = {"id": "D1", "symbol": "TEST", "strategy": "long_call", "opened": "2026-09-01",
               "qty": 1, "entry_cost": 2.00, "profit_target_pct": 100,
               "legs": [{"action": "BUY", "ratio": 1, "option": "TEST261106C00100000"}]}
        c = make_contract("TEST261106C00100000", 0.95, 1.05)
        m = marks.mark_position(pos, {c.option: c}, 100.0, ASOF)
        self.assertAlmostEqual(m["pnl"], -100.0)
        self.assertIn("stop_loss", m["triggers"])

    def test_expired_leg_uses_intrinsic_and_flags_assignment(self):
        m = marks.mark_position(pcs_position(), {}, 93.0, date(2026, 11, 6))
        # short 95P intrinsic 2, long 90P 0 -> value -2 ; pnl = (-2+1)*200 = -200
        self.assertAlmostEqual(m["pnl"], -200.0)
        self.assertIn("expiration", m["triggers"])
        self.assertIn("assignment", m["triggers"])
        self.assertEqual(m["errors"], [])

    def test_missing_unexpired_quote_is_error(self):
        m = marks.mark_position(pcs_position(), {}, 100.0, ASOF)
        self.assertTrue(m["errors"])
        self.assertIsNone(m["pnl"])

    def test_mixed_expiry_error_still_reports_date_triggers(self):
        pos = {"id": "M1", "symbol": "TEST", "strategy": "diagonal", "opened": "2026-09-01",
               "qty": 1, "entry_cost": -1.00, "profit_target_pct": 50,
               "legs": [{"action": "SELL", "ratio": 1, "option": "TEST260925P00095000"},
                        {"action": "BUY", "ratio": 1, "option": "TEST261106P00090000"}]}
        # front leg expired (dte<0) and ITM (spot 93 < strike 95) -> expiration + assignment;
        # back leg missing from cs_index -> error, but date-based triggers must still show.
        m = marks.mark_position(pos, {}, 93.0, ASOF)
        self.assertTrue(m["errors"])
        self.assertIsNone(m["pnl"])
        self.assertIsNone(m["value_per_share"])
        self.assertIsNone(m["pct_of_basis"])
        self.assertIn("expiration", m["triggers"])
        self.assertIn("assignment", m["triggers"])
        self.assertNotIn("profit_target", m["triggers"])
        self.assertNotIn("stop_loss", m["triggers"])

    def test_stock_leg(self):
        pos = {"id": "S1", "symbol": "KO", "strategy": "assigned_shares", "opened": "2026-11-06",
               "qty": 1, "entry_cost": 85.0, "profit_target_pct": 100,
               "legs": [{"action": "BUY", "ratio": 1, "option": "STOCK"}]}
        m = marks.mark_position(pos, {}, 87.0, ASOF)
        self.assertAlmostEqual(m["pnl"], 200.0)
        self.assertIsNone(m["dte"])


if __name__ == "__main__":
    unittest.main()

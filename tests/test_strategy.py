import math
import unittest

from tests.helpers import make_chain, make_contract, ASOF, EXPIRY
from optlib import chain as ch
from optlib import strategy as st


def legs(spec, spot=100.0, with_stock=False, **chain_kwargs):
    cs = ch.contracts(make_chain(spot=spot, **chain_kwargs)["data"])
    return st.legs_from_spec(spec, "TEST", ch.index_contracts(cs), spot=spot, with_stock=with_stock)


class TestSpecAndFills(unittest.TestCase):
    def test_parse_leg_spec(self):
        parsed = st.parse_leg_spec("SELL 1 P 95 2026-11-06; buy 1 p 90 2026-11-06")
        self.assertEqual(parsed[0], ("SELL", 1, "P", 95.0, EXPIRY))
        self.assertEqual(parsed[1][0:3], ("BUY", 1, "P"))

    def test_bad_spec_raises(self):
        with self.assertRaises(ValueError):
            st.parse_leg_spec("SELL P 95")
        with self.assertRaises(ValueError):
            st.parse_leg_spec("HOLD 1 P 95 2026-11-06")

    def test_missing_strike_raises_keyerror(self):
        with self.assertRaises(KeyError):
            legs("SELL 1 P 97 2026-11-06")

    def test_fill_model(self):
        c = make_contract("TEST261106P00095000", 1.00, 1.20)
        self.assertAlmostEqual(st.fill_price(st.Leg("BUY", 1, c)), 1.15)
        self.assertAlmostEqual(st.fill_price(st.Leg("SELL", 1, c)), 1.05)

    def test_fees(self):
        L = legs("SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        self.assertAlmostEqual(st.fees(L, 3), 2 * 3 * 0.65)


class TestAnalyze(unittest.TestCase):
    def test_credit_put_spread_exact_values(self):
        L = legs("SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        a = st.analyze(L, 2, 100.0, ASOF)
        credit = -a["entry_cost_per_share"]
        self.assertGreater(credit, 0)
        self.assertEqual(a["credit_or_debit"], "credit")
        self.assertAlmostEqual(a["max_profit"], credit * 100 * 2, places=1)
        self.assertAlmostEqual(a["max_loss"], -(5 - credit) * 100 * 2, places=1)
        self.assertEqual(len(a["breakevens"]), 1)
        self.assertAlmostEqual(a["breakevens"][0], 95 - credit, places=2)
        self.assertTrue(a["defined_risk"])
        self.assertTrue(0.5 < a["prob_profit"] < 0.95, a["prob_profit"])
        self.assertGreater(a["net_greeks"]["theta_per_day"], 0)   # short premium earns theta
        self.assertGreater(a["net_greeks"]["delta_shares"], 0)    # bullish
        self.assertAlmostEqual(a["fees_round_trip"], 2 * 2 * 2 * 0.65)

    def test_iron_condor(self):
        L = legs("BUY 1 P 85 2026-11-06; SELL 1 P 90 2026-11-06; "
                 "SELL 1 C 110 2026-11-06; BUY 1 C 115 2026-11-06")
        a = st.analyze(L, 1, 100.0, ASOF)
        credit = -a["entry_cost_per_share"]
        self.assertAlmostEqual(a["max_loss"], -(5 - credit) * 100, places=1)
        self.assertEqual(len(a["breakevens"]), 2)
        self.assertAlmostEqual(a["breakevens"][0], 90 - credit, places=2)
        self.assertAlmostEqual(a["breakevens"][1], 110 + credit, places=2)

    def test_long_call_is_defined_risk_unbounded_profit(self):
        a = st.analyze(legs("BUY 1 C 100 2026-11-06"), 1, 100.0, ASOF)
        self.assertTrue(a["unbounded_profit"])
        self.assertTrue(a["defined_risk"])
        self.assertAlmostEqual(a["max_loss"], -a["entry_cost_per_share"] * 100, places=1)

    def test_naked_short_call_rejected(self):
        a = st.analyze(legs("SELL 1 C 110 2026-11-06"), 1, 100.0, ASOF)
        self.assertTrue(a["unbounded_loss"])
        self.assertFalse(a["defined_risk"])

    def test_calendar_is_defined_risk(self):
        L = legs("SELL 1 C 100 2026-11-06; BUY 1 C 100 2026-12-18",
                 expiries=(EXPIRY, __import__("datetime").date(2026, 12, 18)))
        a = st.analyze(L, 1, 100.0, ASOF)
        self.assertEqual(a["eval_date"], EXPIRY.isoformat())
        self.assertTrue(a["defined_risk"])
        self.assertEqual(a["credit_or_debit"], "debit")

    def test_covered_call_with_stock(self):
        L = legs("SELL 1 C 110 2026-11-06", with_stock=True)
        a = st.analyze(L, 1, 100.0, ASOF)
        self.assertTrue(a["defined_risk"])                 # short call covered by shares
        self.assertAlmostEqual(a["net_greeks"]["delta_shares"], 100 - 100 * L[0].contract.delta, places=0)

    def test_high_iv_calendar_is_defined_risk(self):
        # Reviewer repro: at high IV the back-month long call hasn't reached its
        # asymptote at the old 2x-strike grid boundary, so a naive finite-difference
        # slope wrongly read this as unbounded loss. Structural upside-exposure
        # (net calls+stock sign*ratio == 0 here) must call it defined-risk.
        back = __import__("datetime").date(2026, 12, 18)
        L = legs("SELL 1 C 100 2026-11-06; BUY 1 C 100 2026-12-18",
                 expiries=(EXPIRY, back), iv=0.6)
        a = st.analyze(L, 1, 100.0, ASOF)
        self.assertTrue(a["defined_risk"])
        self.assertFalse(a["unbounded_loss"])
        self.assertTrue(math.isfinite(a["max_loss"]))
        self.assertLess(a["max_loss"], 0)
        debit = a["entry_cost_per_share"] * 100
        self.assertGreaterEqual(a["max_loss"], -debit - a["fees_round_trip"])

    def test_high_iv_calendar_longer_back_month_is_defined_risk(self):
        back = __import__("datetime").date(2027, 1, 15)
        L = legs("SELL 1 C 100 2026-11-06; BUY 1 C 100 2027-01-15",
                 expiries=(EXPIRY, back), iv=0.4)
        a = st.analyze(L, 1, 100.0, ASOF)
        self.assertTrue(a["defined_risk"])
        self.assertFalse(a["unbounded_loss"])
        self.assertTrue(math.isfinite(a["max_loss"]))
        self.assertLess(a["max_loss"], 0)
        debit = a["entry_cost_per_share"] * 100
        self.assertGreaterEqual(a["max_loss"], -debit - a["fees_round_trip"])

    def test_naked_short_call_still_unbounded_after_fix(self):
        a = st.analyze(legs("SELL 1 C 110 2026-11-06"), 1, 100.0, ASOF)
        self.assertTrue(a["unbounded_loss"])
        self.assertFalse(a["defined_risk"])
        self.assertIsNone(a["max_loss"])


class TestAscii(unittest.TestCase):
    def test_shape(self):
        L = legs("SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        art = st.ascii_payoff(L, 1, 100.0, width=41, height=9)
        lines = art.splitlines()
        self.assertEqual(len(lines), 9 + 2)
        self.assertIn("*", art)
        self.assertIn("|", art)


if __name__ == "__main__":
    unittest.main()

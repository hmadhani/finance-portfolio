import os
import unittest
from datetime import date

from tests.helpers import make_chain, make_contract, ASOF, EXPIRY
from optlib import chain as ch


class TestOcc(unittest.TestCase):
    def test_parse_and_build_roundtrip(self):
        root, exp, kind, strike = ch.parse_occ("SPY261106C00771000")
        self.assertEqual((root, exp, kind, strike), ("SPY", date(2026, 11, 6), "C", 771.0))
        self.assertEqual(ch.occ_symbol("SPY", date(2026, 11, 6), "C", 771.0), "SPY261106C00771000")

    def test_fractional_strike_and_long_root(self):
        self.assertEqual(ch.parse_occ("GOOGL261106P00172500")[3], 172.5)
        self.assertEqual(ch.parse_occ("GOOGL261106P00172500")[0], "GOOGL")


class TestContracts(unittest.TestCase):
    def setUp(self):
        self.cs = ch.contracts(make_chain()["data"])

    def test_contract_count_and_mid(self):
        self.assertEqual(len(self.cs), 9 * 2)
        c = self.cs[0]
        self.assertAlmostEqual(c.mid, (c.bid + c.ask) / 2, places=4)
        self.assertEqual(c.dte(ASOF), 39)

    def test_index_by_symbol(self):
        idx = ch.index_contracts(self.cs)
        self.assertIn("TEST261106P00095000", idx)

    def test_stock_contract(self):
        s = ch.stock_contract("KO", 87.66)
        self.assertEqual((s.kind, s.bid, s.ask, s.delta), ("S", 87.66, 87.66, 1.0))
        self.assertEqual(s.expiry, ch.STOCK_EXPIRY)


class TestLiquidity(unittest.TestCase):
    def test_rules(self):
        ok = make_contract("X261106P00095000", 1.00, 1.08, oi=600)
        wide = make_contract("X261106P00095000", 1.00, 1.30, oi=600)
        thin = make_contract("X261106P00095000", 1.00, 1.05, oi=100)
        zero_bid = make_contract("X261106P00095000", 0.0, 0.05, oi=5000)
        cheap_etf = make_contract("X261106P00095000", 0.20, 0.25, oi=5000)
        self.assertTrue(ch.is_liquid(ok))
        self.assertFalse(ch.is_liquid(wide))
        self.assertFalse(ch.is_liquid(thin))
        self.assertFalse(ch.is_liquid(zero_bid))
        self.assertFalse(ch.is_liquid(cheap_etf))            # 0.05 wide on 0.225 mid = 22%
        self.assertTrue(ch.is_liquid(cheap_etf, abs_spread_ok=0.05))


class TestSelection(unittest.TestCase):
    def test_expected_move(self):
        self.assertAlmostEqual(ch.expected_move(100, 0.20, 365), 20.0, places=6)
        self.assertAlmostEqual(ch.expected_move(100, 0.20, 36.5), 20.0 * (0.1 ** 0.5), places=6)

    def test_select_expiries_in_window(self):
        exps = (date(2026, 10, 9), date(2026, 11, 6), date(2026, 11, 20), date(2026, 12, 31))
        cs = ch.contracts(make_chain(expiries=exps)["data"])
        self.assertEqual(ch.select_expiries(cs, ASOF, 30, 60), [date(2026, 11, 6), date(2026, 11, 20)])
        self.assertEqual(ch.select_expiries(cs, ASOF, 30, 60, max_expiries=1), [date(2026, 11, 6)])

    def test_delta_buckets_pick_nearest_liquid(self):
        cs = ch.contracts(make_chain(strikes=range(70, 131, 1), width=0.05)["data"])
        picked = ch.delta_buckets(cs, ASOF, EXPIRY, [0.16, 0.30, 0.50], {"abs_spread_ok": 0.05})
        puts = [c for c in picked if c.kind == "P"]
        calls = [c for c in picked if c.kind == "C"]
        self.assertEqual(len(puts), 3)
        self.assertEqual(len(calls), 3)
        best16 = min((c for c in cs if c.kind == "P"), key=lambda c: abs(abs(c.delta) - 0.16))
        self.assertIn(best16.option, [c.option for c in puts])


if __name__ == "__main__":
    unittest.main()

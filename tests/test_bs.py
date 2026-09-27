import os
import sys
import math
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from optlib.bs import bs_price, bs_greeks, prob_itm, norm_cdf


class TestBlackScholes(unittest.TestCase):
    # Hull, "Options, Futures, and Other Derivatives", worked example:
    # S=42, K=40, r=10%, sigma=20%, T=0.5 -> call 4.76, put 0.81
    def test_hull_example_call_and_put(self):
        self.assertAlmostEqual(bs_price(42, 40, 0.5, 0.10, 0.20, "C"), 4.76, places=2)
        self.assertAlmostEqual(bs_price(42, 40, 0.5, 0.10, 0.20, "P"), 0.81, places=2)

    def test_put_call_parity(self):
        S, K, T, r, sig = 100.0, 95.0, 0.25, 0.04, 0.3
        c = bs_price(S, K, T, r, sig, "C")
        p = bs_price(S, K, T, r, sig, "P")
        self.assertAlmostEqual(c - p, S - K * math.exp(-r * T), places=6)

    def test_expired_option_is_intrinsic(self):
        self.assertEqual(bs_price(105, 100, 0, 0.04, 0.2, "C"), 5.0)
        self.assertEqual(bs_price(105, 100, 0, 0.04, 0.2, "P"), 0.0)

    def test_greeks_signs_and_hull_delta(self):
        g = bs_greeks(42, 40, 0.5, 0.10, 0.20, "C")
        self.assertAlmostEqual(g["delta"], 0.7791, places=3)
        self.assertGreater(g["gamma"], 0)
        self.assertLess(g["theta"], 0)
        self.assertGreater(g["vega"], 0)
        gp = bs_greeks(42, 40, 0.5, 0.10, 0.20, "P")
        self.assertAlmostEqual(g["delta"] - gp["delta"], 1.0, places=6)

    def test_theta_is_per_day_and_vega_per_point(self):
        # ATM 40-day SPY-like call: theta ~ -0.16/day, vega ~ 1.0 per vol point
        g = bs_greeks(771.35, 771, 40 / 365, 0.04, 0.1315, "C")
        self.assertTrue(-0.25 < g["theta"] < -0.10, g["theta"])
        self.assertTrue(0.8 < g["vega"] < 1.3, g["vega"])

    def test_greeks_at_expiry_or_zero_vol_no_exception(self):
        gc = bs_greeks(105, 100, 0, 0.04, 0.2, "C")
        self.assertEqual(gc, {"delta": 1.0, "gamma": 0.0, "theta": 0.0, "vega": 0.0})
        gp = bs_greeks(95, 100, 0, 0.04, 0.2, "P")
        self.assertEqual(gp, {"delta": -1.0, "gamma": 0.0, "theta": 0.0, "vega": 0.0})
        gc_otm = bs_greeks(95, 100, 0, 0.04, 0.2, "C")
        self.assertEqual(gc_otm["delta"], 0.0)
        gz = bs_greeks(105, 100, 0.5, 0.04, 0.0, "C")
        self.assertEqual(gz, {"delta": 1.0, "gamma": 0.0, "theta": 0.0, "vega": 0.0})

    def test_prob_itm(self):
        self.assertAlmostEqual(prob_itm(100, 100, 1e-9, 0.0, 0.2, "C"), 0.5, places=2)
        self.assertEqual(prob_itm(110, 100, 0, 0.04, 0.2, "C"), 1.0)
        self.assertEqual(prob_itm(110, 100, 0, 0.04, 0.2, "P"), 0.0)
        self.assertAlmostEqual(norm_cdf(0), 0.5)


if __name__ == "__main__":
    unittest.main()

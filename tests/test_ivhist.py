import os
import tempfile
import unittest

import tests.helpers  # noqa: F401  (adds scripts/ to sys.path)
from optlib import ivhist


class TestRecord(unittest.TestCase):
    def test_append_and_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "iv.csv")
            self.assertEqual(ivhist.record(p, "2026-09-28", [("SPY", 11.982, 771.35), ("QQQ", 15.1, 745.4)]), 2)
            self.assertEqual(ivhist.record(p, "2026-09-28", [("SPY", 12.5, 772.0)]), 0)
            self.assertEqual(ivhist.record(p, "2026-09-29", [("SPY", 12.5, 772.0)]), 1)
            with open(p) as f:
                lines = f.read().strip().splitlines()
            self.assertEqual(lines[0], "date,symbol,iv30,price")
            self.assertEqual(len(lines), 4)
            self.assertEqual(ivhist.history(p, "SPY"), [11.982, 12.5])

    def test_history_missing_file(self):
        self.assertEqual(ivhist.history("/nonexistent/iv.csv", "SPY"), [])

    def test_dedupes_within_same_call(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "iv.csv")
            self.assertEqual(
                ivhist.record(p, "2026-09-28", [("SPY", 11.0, 1.0), ("SPY", 12.0, 2.0)]), 1)
            self.assertEqual(ivhist.history(p, "SPY"), [11.0])


class TestRank(unittest.TestCase):
    def test_insufficient_history(self):
        r = ivhist.iv_rank([10.0] * 5, 12.0)
        self.assertIsNone(r["iv_rank"])
        self.assertEqual(r["n_obs"], 5)
        self.assertIn("VIX percentile", r["note"])

    def test_rank_and_percentile(self):
        values = [10.0 + i for i in range(21)]  # 10..30
        r = ivhist.iv_rank(values, 25.0)
        self.assertEqual(r["iv_rank"], 75.0)                 # (25-10)/(30-10)
        self.assertAlmostEqual(r["iv_percentile"], 15 / 21 * 100, places=1)

    def test_rank_clamped(self):
        values = [10.0 + i for i in range(21)]
        self.assertEqual(ivhist.iv_rank(values, 40.0)["iv_rank"], 100.0)
        self.assertEqual(ivhist.iv_rank(values, 5.0)["iv_rank"], 0.0)

    def test_vix_percentile(self):
        csv_text = "DATE,OPEN,HIGH,LOW,CLOSE\n" + "".join(
            f"01/01/2025,{c},{c},{c},{c}\n" for c in range(1, 101))
        self.assertEqual(ivhist.vix_percentile(csv_text, 50.5, lookback=100), 50.0)
        self.assertEqual(ivhist.vix_percentile(csv_text, 50.5, lookback=10), 0.0)  # last 10 are 91..100


if __name__ == "__main__":
    unittest.main()

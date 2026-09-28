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
                                    "ETF1": make_chain(symbol="ETF1", spot=50.0, strikes=range(40, 61, 1))})
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

    def test_price_spread_qty_zero_is_usage_error(self):
        self.run_cli("price-spread", "--symbol", "TEST", "--qty", "0",
                     "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06", expect=2)

    def test_price_spread_negative_qty_is_usage_error(self):
        self.run_cli("price-spread", "--symbol", "TEST", "--qty", "-1",
                     "--legs", "BUY 1 C 105 2026-11-06", expect=2)


if __name__ == "__main__":
    unittest.main()

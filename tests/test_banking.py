import tempfile
from pathlib import Path
import unittest

from src.reconcile import reconcile
from src.build_demo_warehouse import build


class BankingTests(unittest.TestCase):
    def test_reconciliation(self):
        result = reconcile("data/source_transactions.csv", "data/warehouse_transactions.csv")
        self.assertTrue(result["row_count_match"])
        self.assertTrue(result["transaction_set_match"])
        self.assertTrue(result["control_total_match"])

    def test_demo_warehouse(self):
        with tempfile.TemporaryDirectory() as d:
            rows = build(Path(d) / "demo.db")
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0]["customer_id"], "C001")


if __name__ == "__main__": unittest.main()

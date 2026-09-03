from __future__ import annotations

import csv
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "local" / "banking_demo.db"


def build(database: Path = DB) -> list[dict]:
    database.parent.mkdir(parents=True, exist_ok=True)
    if database.exists():
        database.unlink()
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    try:
        conn.executescript((ROOT / "sql" / "sqlite_demo.sql").read_text(encoding="utf-8"))
        with (ROOT / "data" / "warehouse_transactions.csv").open(newline="", encoding="utf-8") as handle:
            for r in csv.DictReader(handle):
                conn.execute("insert into fact_transaction values (?,?,?,?,?)", (r["transaction_id"], r["customer_id"], r["transaction_date"], float(r["amount"]), r["category"]))
        conn.commit()
        rows = conn.execute("""select customer_id, count(*) transaction_count, round(sum(amount),2) total_amount from fact_transaction group by customer_id order by total_amount desc""").fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))

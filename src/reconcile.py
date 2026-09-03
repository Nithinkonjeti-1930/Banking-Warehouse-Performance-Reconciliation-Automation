from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

REQUIRED = {"transaction_id", "customer_id", "transaction_date", "amount", "category"}


def profile(path: str | Path) -> dict:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing required columns: {sorted(missing)}")
        rows = list(reader)
    ids = [r["transaction_id"].strip() for r in rows]
    amount = Decimal("0")
    for row in rows:
        try:
            amount += Decimal(row["amount"])
        except InvalidOperation as exc:
            raise ValueError(f"invalid amount for {row.get('transaction_id')}") from exc
    return {"rows": len(rows), "ids": set(ids), "amount": amount, "duplicates": sorted({x for x in ids if ids.count(x)>1})}


def reconcile(source, target):
    s, t = profile(source), profile(target)
    return {
        "row_count_match": s["rows"] == t["rows"],
        "transaction_set_match": s["ids"] == t["ids"],
        "control_total_match": s["amount"] == t["amount"],
        "source_duplicates": s["duplicates"],
        "target_duplicates": t["duplicates"],
    }


def main():
    p=argparse.ArgumentParser(); p.add_argument("--source",required=True); p.add_argument("--target",required=True); a=p.parse_args()
    result=reconcile(a.source,a.target); print(result)
    ok=all(result[k] for k in ("row_count_match","transaction_set_match","control_total_match")) and not result["source_duplicates"] and not result["target_duplicates"]
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__": main()

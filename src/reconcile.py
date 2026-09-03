from __future__ import annotations

import argparse
import csv
from decimal import Decimal
from pathlib import Path


def profile(path):
    rows = list(csv.DictReader(Path(path).open(newline="", encoding="utf-8")))
    ids = [r["transaction_id"] for r in rows]
    return {
        "rows": len(rows),
        "ids": set(ids),
        "amount": sum((Decimal(r["amount"]) for r in rows), Decimal("0")),
        "duplicates": sorted({x for x in ids if ids.count(x) > 1}),
    }


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
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--target", required=True)
    args = p.parse_args()
    result = reconcile(args.source, args.target)
    print(result)
    if not all(result[k] for k in ("row_count_match", "transaction_set_match", "control_total_match")):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

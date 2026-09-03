from src.reconcile import reconcile


def test_source_matches_warehouse():
    result = reconcile("data/source_transactions.csv", "data/warehouse_transactions.csv")
    assert result["row_count_match"]
    assert result["transaction_set_match"]
    assert result["control_total_match"]
    assert result["target_duplicates"] == []

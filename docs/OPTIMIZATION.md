# Query optimization patterns

This repository demonstrates portable patterns rather than pretending one query is optimal on every warehouse.

1. Filter early when predicates are selective.
2. Avoid `select *` in recurring analytical extracts.
3. Pre-aggregate repeated grain reductions.
4. Join on appropriately typed, stable keys.
5. Inspect warehouse-specific execution plans before changing indexes, clustering, sort keys, or distribution keys.
6. Keep reconciliation queries simple and independent from presentation logic.

Warehouse-specific physical tuning should be tested separately for PostgreSQL, Redshift, and Snowflake because their optimizers and storage models differ.

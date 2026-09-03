# Query optimization notes

The portfolio examples demonstrate patterns rather than claiming one query is universally optimal.

- Filter early when it materially reduces scanned rows.
- Aggregate reusable monthly/customer datasets instead of repeating large detail scans.
- Index/cluster/sort according to the engine and access pattern.
- Avoid `select *` in production analytical paths.
- Inspect execution plans and warehouse scan metrics before and after a change.
- Reconcile row counts and monetary control totals after transformations.

Platform specifics differ: PostgreSQL uses indexes heavily; Redshift relies on distribution/sort design; Snowflake relies on micro-partition pruning and can use clustering selectively.

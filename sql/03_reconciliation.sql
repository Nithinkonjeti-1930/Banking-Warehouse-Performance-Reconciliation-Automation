-- Example warehouse-side control totals.
select
    count(*) as row_count,
    count(distinct transaction_id) as distinct_transaction_count,
    sum(amount) as amount_control_total
from fact_transaction;

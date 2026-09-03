-- PostgreSQL/Redshift-style example. Snowflake uses the same DATE_TRUNC concept with minor syntax differences.
with monthly as (
    select customer_key, date_trunc('month', transaction_date) as month_start,
           count(*) as transaction_count, sum(amount) as total_amount
    from fact_transaction
    group by customer_key, date_trunc('month', transaction_date)
)
select customer_key, month_start, transaction_count, total_amount,
       avg(total_amount) over (partition by customer_key order by month_start rows between 2 preceding and current row) as rolling_3m_amount
from monthly;

-- Pre-aggregate once for recurring reporting instead of repeatedly scanning transaction detail.
with monthly as (
    select
        customer_key,
        date_trunc('month', transaction_date) as month_start,
        count(*) as transaction_count,
        sum(amount) as total_amount
    from fact_transaction
    group by 1, 2
)
select
    customer_key,
    month_start,
    transaction_count,
    total_amount,
    avg(total_amount) over (
        partition by customer_key
        order by month_start
        rows between 2 preceding and current row
    ) as rolling_3m_amount
from monthly;

-- Generic warehouse pattern; adapt types/DDL to the target platform.
create table if not exists dim_customer (
    customer_key bigint,
    customer_id varchar(64) not null,
    segment varchar(64),
    effective_from date,
    effective_to date,
    is_current boolean
);

create table if not exists fact_transaction (
    transaction_id varchar(64) not null,
    customer_key bigint not null,
    transaction_date date not null,
    amount decimal(18,2) not null,
    category varchar(64)
);

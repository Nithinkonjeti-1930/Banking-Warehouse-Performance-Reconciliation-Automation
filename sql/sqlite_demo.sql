create table fact_transaction (
  transaction_id text primary key,
  customer_id text not null,
  transaction_date text not null,
  amount real not null,
  category text not null
);
create index idx_fact_customer_date on fact_transaction(customer_id, transaction_date);
create index idx_fact_category on fact_transaction(category);

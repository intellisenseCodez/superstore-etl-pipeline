with orders as (
    select * from {{ ref('int_orders_enriched') }}
)

select
    customer_id,
    customer_name,
    segment,
    avg(quantity) as avg_quantity,
    avg(sales) as avg_sales,
    sum(sales) as total_sales,
    sum(profit) as total_profit,
    count(distinct order_id) as total_orders
from orders
group by 1,2,3

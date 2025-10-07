with orders as (
    select * from {{ ref('int_orders_enriched') }}
),

sales_summary as (
    select
        region,
        category,
        sub_category,
        sum(sales) as total_sales,
        sum(profit) as total_profit,
        avg(profit_margin) as avg_margin,
        sum(quantity) as total_quantity
    from orders
    group by 1, 2, 3
)

select * from sales_summary


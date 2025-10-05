with base as (
    select * from {{ ref('stg_orders') }}
),

enriched as (
    select
        *,
        (profit / nullif(sales, 0)) as profit_margin,
        (ship_date - order_date) as ship_days
    from base
)

select * from enriched

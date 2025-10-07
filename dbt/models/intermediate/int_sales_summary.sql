SELECT
    order_date,
    DATE_PART('year', order_date) AS order_year,
    DATE_PART('month', order_date) AS order_month,
    region,
    category,
    SUM(sales) AS total_sales,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(profit) AS total_profit
FROM {{ ref('stg_orders') }}
GROUP BY 1, 2, 3, 4, 5

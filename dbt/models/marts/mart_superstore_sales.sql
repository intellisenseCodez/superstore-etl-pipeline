WITH summary AS (
    SELECT * FROM {{ ref('int_sales_summary') }}
)
SELECT
    SUM(total_sales) AS total_sales,
    SUM(total_orders) AS num_orders,
    ROUND(SUM(total_sales) / NULLIF(SUM(total_orders), 0), 2) AS avg_sales_per_order,
    region,
    category,
    order_year,
    order_month
FROM summary
GROUP BY region, category, order_year, order_month
ORDER BY order_year, order_month
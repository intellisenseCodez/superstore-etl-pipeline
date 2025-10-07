SELECT
    order_month,
    SUM(total_sales) AS total_sales
FROM {{ ref('int_sales_summary') }}
GROUP BY order_month
ORDER BY order_month
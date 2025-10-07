SELECT
    order_year,
    SUM(total_sales) AS total_sales
FROM {{ ref('int_sales_summary') }}
GROUP BY order_year
ORDER BY order_year
SELECT
    category,
    SUM(total_sales) AS total_sales
FROM {{ ref('int_sales_summary') }}
GROUP BY category
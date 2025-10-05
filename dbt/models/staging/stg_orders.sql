with source as (
    select * from {{ source('raw', 'raw_orders') }}
),
renamed as (
    select
        "Row ID" as row_id,
        "Order ID" as order_id,
        TO_DATE("Order Date", 'DD-MM-YYYY') AS order_date,
        TO_DATE("Ship Date", 'DD-MM-YYYY') AS ship_date,
        "Ship Mode" as ship_mode,
        "Customer ID" as customer_id,
        "Customer Name" as customer_name,
        "Segment" as segment,
        "Country" as country,
        "City" as city,
        "State" as state,
        "Postal Code" as postal_code,
        "Region" as region,
        "Product ID" as product_id,
        "Category" as category,
        "Sub-Category" as sub_category,
        "Product Name" as product_name,
        cast("Sales" as numeric) as sales,
        cast("Quantity" as int) as quantity,
        cast("Discount" as numeric) as discount,
        cast("Profit" as numeric) as profit
    from source
)
select * from renamed
/* 
==================================================================================
CREATE USER AND DATABASE - SUPERSTORE PROJECT
==================================================================================

Script Purpose:

Author:

*/

-- Create application user
DO
$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'dev_user') THEN
        CREATE ROLE dev_user LOGIN PASSWORD 'dev123';
    END IF;
END
$$;


-- Create DB superstore database if not exists
DO
$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'superstore') THEN
        CREATE DATABASE superstore;
    END IF;
END
$$;

-- Connect to it
\c superstore;

-- Create schema for raw layer
CREATE SCHEMA IF NOT EXISTS raw AUTHORIZATION dev_user;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE superstore TO dev_user;


-- drop table if exit
DROP TABLE IF EXISTS raw.raw_orders;

-- Create Raw_orders table inside raw schema
CREATE TABLE raw.raw_orders (
    "Row ID" VARCHAR(255),
    "Order ID" VARCHAR(255),
    "Order Date" VARCHAR(255),
    "Ship Date" VARCHAR(255),
    "Ship Mode" VARCHAR(255),
    "Customer ID" VARCHAR(255),
    "Customer Name" VARCHAR(255),
    "Segment" VARCHAR(255),
    "Country" VARCHAR(255),
    "City" VARCHAR(255),
    "State" VARCHAR(255),
    "Postal Code" VARCHAR(255),
    "Region" VARCHAR(255),
    "Product ID" VARCHAR(255),
    "Category" VARCHAR(255),
    "Sub-Category" VARCHAR(255),
    "Product Name" VARCHAR(255),
    "Sales" VARCHAR(255),
    "Quantity" VARCHAR(255),
    "Discount" VARCHAR(255),
    "Profit" VARCHAR(255)
);





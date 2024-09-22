CREATE TABLE production.categories (category_id IDENTITY(1,1) int NOT NULL, category_name varchar(255) NOT NULL);

CREATE TABLE production.brands (brand_id IDENTITY(1,1) int NOT NULL, brand_name varchar(255) NOT NULL);

CREATE TABLE production.products (product_id IDENTITY(1,1) int NOT NULL, product_name varchar(255) NOT NULL, brand_id int NOT NULL, category_id int NOT NULL, model_year smallint NOT NULL, list_price decimal(10, 2) NOT NULL);

CREATE TABLE sales.customers (customer_id IDENTITY(1,1) int NOT NULL, first_name varchar(255) NOT NULL, last_name varchar(255) NOT NULL, phone varchar(25) NULL, email varchar(255) NOT NULL, street varchar(255) NULL, city varchar(50) NULL, state varchar(25) NULL, zip_code varchar(5) NULL);

CREATE TABLE sales.stores (store_id IDENTITY(1,1) int NOT NULL, store_name varchar(255) NOT NULL, phone varchar(25) NULL, email varchar(255) NULL, street varchar(255) NULL, city varchar(255) NULL, state varchar(10) NULL, zip_code varchar(5) NULL);

CREATE TABLE sales.staffs (staff_id IDENTITY(1,1) int NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL, email varchar(255) NOT NULL, phone varchar(25) NULL, active tinyint NOT NULL, store_id int NOT NULL, manager_id int NULL);

CREATE TABLE sales.orders (order_id IDENTITY(1,1) int NOT NULL, customer_id int NULL, order_status tinyint NOT NULL, order_date date NOT NULL, required_date date NOT NULL, shipped_date date NULL, store_id int NOT NULL, staff_id int NOT NULL);

CREATE TABLE sales.order_items (order_id int NOT NULL, item_id int NOT NULL, product_id int NOT NULL, quantity int NOT NULL, list_price decimal(10, 2) NOT NULL, discount decimal(4, 2) NOT NULL);

CREATE TABLE production.stocks (store_id int NOT NULL, product_id int NOT NULL, quantity int NULL);


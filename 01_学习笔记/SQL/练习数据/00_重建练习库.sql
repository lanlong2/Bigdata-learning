-- PostgreSQL 专用课程初始化脚本。
-- 执行前：连接自己新建的专用学习数据库，例如 sql_learning_db。
-- 注意：每次运行都会删除并重建 sql_learning schema，清空其中全部对象和数据。
-- sql_learning 中只应存本课程数据；不要让其他 schema 的对象依赖课程对象，
-- 因为 CASCADE 也会删除依赖这些对象的外部对象。
-- 本脚本不删除数据库，也不删除 public schema。
-- 00—03 的学习者不需要先掌握下列建表语法；模块 07 再系统解释。

BEGIN;

DROP SCHEMA IF EXISTS sql_learning CASCADE;
CREATE SCHEMA sql_learning;
SET search_path TO sql_learning;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    city VARCHAR(50)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    order_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('paid', 'cancelled'))
);

INSERT INTO customers (customer_id, customer_name, city) VALUES
    (1, 'ada', '北京'),
    (2, 'bo', '上海'),
    (3, 'cy', '北京'),
    (4, 'dan', '广州'),
    (5, 'eve', NULL);

INSERT INTO products (product_id, product_name, category, unit_price) VALUES
    (1, 'pen', 'stationery', 3.00),
    (2, 'notebook', 'stationery', 5.00),
    (3, 'eraser', 'stationery', 2.00),
    (4, 'mug', 'home', 20.00);

INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date, status) VALUES
    (1001, 1, 1, 2, DATE '2026-10-01', 'paid'),
    (1002, 1, 2, 1, DATE '2026-10-01', 'paid'),
    (1003, 2, 1, 3, DATE '2026-10-02', 'paid'),
    (1004, 3, 2, 2, DATE '2026-10-02', 'cancelled'),
    (1005, 2, 3, 4, DATE '2026-10-03', 'paid'),
    (1006, 4, 2, 1, DATE '2026-10-03', 'paid'),
    (1007, NULL, 1, 1, DATE '2026-10-04', 'paid'),
    (1008, 1, 3, 2, DATE '2026-10-04', 'paid');

COMMIT;

-- 初始化后的三条检查：预期分别显示 5、4、8。
SELECT COUNT(*) AS customer_rows FROM customers;
SELECT COUNT(*) AS product_rows FROM products;
SELECT COUNT(*) AS order_rows FROM orders;

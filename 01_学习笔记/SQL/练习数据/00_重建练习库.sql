-- MySQL 8.4 LTS 课程数据：只用于专用学习库 sql_learning。
-- 重复执行会删除 module07_tasks，并清空重建 customers、products、orders。
-- 不删除整个数据库，不删除其他表；模块 07 的任务练习需重新创建。
-- 如已写入自己的练习数据，请先备份。遇到第一条错误立即停止，不跳过错误继续。
-- MySQL 的 CREATE / DROP / ALTER 会隐式提交，整份脚本不能用 ROLLBACK 撤销。
-- 00—06 先把本文件当作课程准备工具；建表、约束与事务在模块 07 学习。

CREATE DATABASE IF NOT EXISTS sql_learning
    CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs;
ALTER DATABASE sql_learning
    CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs;
USE sql_learning;

-- 先删除引用其他表的课程表，不关闭外键检查。
DROP TABLE IF EXISTS module07_tasks;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    city VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT chk_products_price CHECK (unit_price >= 0)
) ENGINE=InnoDB;

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),
    CONSTRAINT fk_orders_product FOREIGN KEY (product_id)
        REFERENCES products(product_id),
    CONSTRAINT chk_orders_quantity CHECK (quantity > 0),
    CONSTRAINT chk_orders_status CHECK (status IN ('paid', 'cancelled'))
) ENGINE=InnoDB;

-- 以下数据写入在同一事务中提交；这一段事务不包括上面的建表操作。
START TRANSACTION;

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

-- 预期：客户 5 行、商品 4 行、订单 8 行。
SELECT COUNT(*) AS customer_rows FROM customers;
SELECT COUNT(*) AS product_rows FROM products;
SELECT COUNT(*) AS order_rows FROM orders;

-- 预期：已付款 7 笔、14 件、40.00 元。
SELECT COUNT(*) AS paid_orders,
       SUM(o.quantity) AS paid_quantity,
       SUM(o.quantity * p.unit_price) AS paid_amount
FROM orders AS o
JOIN products AS p ON p.product_id = o.product_id
WHERE o.status = 'paid';

-- 日常学习入口：此文件只查询，不创建、修改或删除课程数据。
-- DBeaver 数据源选择“MySQL 数据学习”，选中一条语句后 Ctrl+Enter 执行。
-- Ctrl+S 保存的是项目里的 SQL 文字；Git 提交、推送后才会同步到 GitHub。

USE sql_learning;

-- 1. 确认连接。database_name 应为 sql_learning，版本应为 8.4.x。
SELECT DATABASE() AS database_name,
       VERSION() AS mysql_version,
       CURRENT_USER() AS login_account,
       @@session.time_zone AS time_zone,
       @@character_set_connection AS connection_charset,
       @@collation_database AS database_collation,
       @@session.sql_mode AS sql_mode;

-- 2. 三张课程表应依次为 5、4、8 行，使用 InnoDB。
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders;

SELECT table_name, engine, table_collation
FROM information_schema.tables
WHERE table_schema = DATABASE()
  AND table_name IN ('customers', 'products', 'orders')
ORDER BY table_name;

-- 3. 查看课程数据。从这里开始在自己的作答文件中练习查询。
SELECT customer_id, customer_name, city
FROM customers
ORDER BY customer_id;

-- 4. 业务结果基准：7 笔、14 件、40.00 元。
SELECT COUNT(*) AS paid_orders,
       SUM(o.quantity) AS paid_quantity,
       SUM(o.quantity * p.unit_price) AS paid_amount
FROM orders AS o
JOIN products AS p ON p.product_id = o.product_id
WHERE o.status = 'paid';

-- 5. 确认外键实际存在：orders 应有两条 FOREIGN KEY。
SELECT table_name, constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_schema = DATABASE()
  AND table_name IN ('customers', 'products', 'orders')
ORDER BY table_name, constraint_type, constraint_name;

-- 环境配置完成不等于已学完模块；实际学习进度按自己的完成情况记录。

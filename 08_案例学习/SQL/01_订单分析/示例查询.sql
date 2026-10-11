-- SQL 订单分析案例：完整示范，待学习。
-- 仅连接个人 PostgreSQL 练习数据库，先运行共享练习数据脚本。
-- 不在真实业务数据上执行；本文件只查询 sql_learning 的共享练习表。
SET search_path TO sql_learning;

-- C01｜已支付整体概览：7 笔、14 件、40.00 元。
SELECT COUNT(*) AS paid_order_count,
       SUM(o.quantity) AS paid_quantity,
       SUM(o.quantity * p.unit_price) AS paid_amount
FROM orders AS o
INNER JOIN products AS p ON o.product_id = p.product_id
WHERE o.status = 'paid';

-- C02｜完整支付明细：保留匿名订单，共 7 行。
SELECT o.order_id, o.order_date,
       COALESCE(c.customer_name, '匿名客户') AS customer_name,
       p.product_name, o.quantity,
       o.quantity * p.unit_price AS amount
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
INNER JOIN products AS p ON o.product_id = p.product_id
WHERE o.status = 'paid'
ORDER BY o.order_date, o.order_id;

-- C03｜每日支付：日期、订单数、数量、金额。
SELECT o.order_date, COUNT(*) AS paid_order_count,
       SUM(o.quantity) AS paid_quantity,
       SUM(o.quantity * p.unit_price) AS paid_amount
FROM orders AS o
INNER JOIN products AS p ON o.product_id = p.product_id
WHERE o.status = 'paid'
GROUP BY o.order_date
ORDER BY o.order_date;

-- C04｜全部商品，包含零销量 mug。
SELECT p.product_id, p.product_name,
       COUNT(o.order_id) AS paid_order_count,
       COALESCE(SUM(o.quantity), 0) AS paid_quantity,
       COALESCE(SUM(o.quantity * p.unit_price), 0) AS paid_amount
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
   AND o.status = 'paid'
GROUP BY p.product_id, p.product_name
ORDER BY p.product_id;

-- C05｜全部已登记客户，包含零支付客户。
-- 客户总额只有 37.00，匿名订单 3.00 不归属到任何已登记客户。
SELECT c.customer_id, c.customer_name,
       COUNT(o.order_id) AS paid_order_count,
       COALESCE(SUM(o.quantity * p.unit_price), 0) AS paid_amount
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
   AND o.status = 'paid'
LEFT JOIN products AS p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

-- C06｜有支付订单的已登记客户总额排名。
WITH customer_totals AS (
    SELECT c.customer_id, c.customer_name,
           SUM(o.quantity * p.unit_price) AS total_amount
    FROM customers AS c
    INNER JOIN orders AS o ON c.customer_id = o.customer_id
    INNER JOIN products AS p ON o.product_id = p.product_id
    WHERE o.status = 'paid'
    GROUP BY c.customer_id, c.customer_name
)
SELECT customer_id, customer_name, total_amount,
       DENSE_RANK() OVER (ORDER BY total_amount DESC) AS rank_no
FROM customer_totals
ORDER BY rank_no, customer_id;

-- C07｜保留匿名订单的逐笔累计金额。
WITH paid_detail AS (
    SELECT o.order_id, o.order_date,
           o.quantity * p.unit_price AS amount
    FROM orders AS o
    INNER JOIN products AS p ON o.product_id = p.product_id
    WHERE o.status = 'paid'
)
SELECT order_id, order_date, amount,
       SUM(amount) OVER (
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_amount
FROM paid_detail
ORDER BY order_date, order_id;

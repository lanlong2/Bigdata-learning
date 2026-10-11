# 05｜子查询与 CTE：把一个查询的结果交给另一个查询

状态：待学习。前置：[04｜多表连接](04_多表连接.md)。对应进阶习题 J05—J08。

使用 PostgreSQL，在个人练习数据库准备好[共享数据](练习数据/00_重建练习库.sql)，每次新连接先执行：

```sql
SET search_path TO sql_learning;
```

本章仍然只查询数据。子查询是嵌在另一条查询里的查询；CTE 是给一段查询结果起名字，供同一条语句后面的查询使用。它们都能帮助我们把“大问题”拆成“小问题”。

## 1. 先算平均金额，再找高于平均的订单

先独立执行平均值查询：

```sql
SELECT AVG(o.quantity * p.unit_price) AS avg_amount
FROM orders AS o
INNER JOIN products AS p ON o.product_id = p.product_id
WHERE o.status = 'paid';
```

结果约为 `5.7142857142857143`，因为 7 笔已支付订单合计 40 元。工具显示的小数位数可能不同。

现在把这条查询放进括号，作为外层 `WHERE` 的比较值：

```sql
SELECT o.order_id, o.quantity * p.unit_price AS amount
FROM orders AS o
INNER JOIN products AS p ON o.product_id = p.product_id
WHERE o.status = 'paid'
  AND o.quantity * p.unit_price > (
      SELECT AVG(o2.quantity * p2.unit_price)
      FROM orders AS o2
      INNER JOIN products AS p2 ON o2.product_id = p2.product_id
      WHERE o2.status = 'paid'
  )
ORDER BY o.order_id;
```

| order_id | amount |
| --- | --- |
| 1001 | 6.00 |
| 1003 | 9.00 |
| 1005 | 8.00 |

这里括号中的子查询返回一行一列的值，叫作“标量子查询”，可以放在需要单个值的位置。用 `AVG` 且没有 `GROUP BY`，保证只返回一行。

如果用 `=` 或 `>` 比较的子查询返回多行，PostgreSQL 会报错；它无法确定应比较哪一个值。如果子查询没找到任何可用值，`AVG` 返回 `NULL`，外层与 `NULL` 的大小比较不会筛选出行。这种情况不能擅自当成平均值为 0。

内外层使用不同别名 `o`、`o2`，便于分清范围；不是要求必须使用这些名字。内层筛选支付状态，外层也筛选支付状态，是因为它们分别控制“算哪些订单的平均”和“检查哪些订单”。

## 2. IN：与一个查询给出的多个值比较

想找“至少有一笔已支付订单的已登记客户”，可以先查所有已支付订单中的客户编号，再在客户表匹配：

```sql
SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE status = 'paid'
)
ORDER BY customer_id;
```

结果：`1 | ada`、`2 | bo`、`4 | dan`。

`IN` 表示“等于括号中任意一个值”。子查询在这里可以返回多行，但必须只返回一列。重复客户编号不让外层客户重复出现，因为外层仍是对客户表的每一行判断是否满足条件。

已支付订单中有一个匿名客户编号 `NULL`；真正存在的 1、2、4 仍可匹配。不要直接把 `IN` 换成 `NOT IN` 来找没有订单的客户：子查询带 `NULL` 时，未匹配值的判断会变成未知，可能一个客户也查不出来。上一章的左连接加 `o.order_id IS NULL` 更适合当前范围。

## 3. FROM 里的子查询：先生成结果表，再查询它

把查询放到 `FROM` 中，可以把它当成临时的结果表。`AS paid_detail` 给这个结果表起别名，结果的列名来自内部 `SELECT`。

```sql
SELECT paid_detail.order_id, paid_detail.amount
FROM (
    SELECT o.order_id, o.quantity * p.unit_price AS amount
    FROM orders AS o
    INNER JOIN products AS p ON o.product_id = p.product_id
    WHERE o.status = 'paid'
) AS paid_detail
WHERE paid_detail.amount >= 8
ORDER BY paid_detail.order_id;
```

结果：`1003 | 9.00`、`1005 | 8.00`。先构造订单金额，再在外层筛选金额，就不用在外层重复写乘法。只能使用内层选出来的列；上例没有选 `status`，外层就不能写 `paid_detail.status`。

## 4. WITH 与 CTE：给中间结果起名字

`CTE` 是 Common Table Expression 的简称，中文叫“公共表表达式”。初学时可以理解成“这条语句里有名字的中间结果”。写法是 `WITH 名字 AS (查询)`，紧接着写使用这个名字的主查询。

```sql
WITH paid_detail AS (
    SELECT o.order_id, o.customer_id,
           o.quantity * p.unit_price AS amount
    FROM orders AS o
    INNER JOIN products AS p ON o.product_id = p.product_id
    WHERE o.status = 'paid'
)
SELECT customer_id, SUM(amount) AS total_amount
FROM paid_detail
WHERE customer_id IS NOT NULL
GROUP BY customer_id
HAVING SUM(amount) >= 10
ORDER BY total_amount DESC, customer_id;
```

| customer_id | total_amount |
| --- | --- |
| 2 | 17.00 |
| 1 | 15.00 |

理解步骤：

1. `paid_detail` 表示已支付订单的明细，共 7 行。
2. 主查询排除匿名编号，留下 6 行。
3. 按客户编号合并，得到 ada 15 元、bo 17 元、dan 5 元。
4. `HAVING` 保留客户总额至少 10 元的组，再按金额排序。

CTE 不创建永久表，也不是保存后的文件。分号写在整个语句末尾；如果在 CTE 的右括号后立刻写分号，它与主查询就断开了。执行下一条语句时，不能继续使用上一次的 `paid_detail` 名字。

CTE 主要让逻辑更清晰，不保证查询更快；本阶段先保证统计范围和结果正确。

## 5. 多个 CTE：比较客户总额与客户平均总额

多个 CTE 在同一个 `WITH` 后用逗号分开，后面的 CTE 可以引用前面定义的结果。

```sql
WITH paid_detail AS (
    SELECT o.customer_id, o.quantity * p.unit_price AS amount
    FROM orders AS o
    INNER JOIN products AS p ON o.product_id = p.product_id
    WHERE o.status = 'paid'
      AND o.customer_id IS NOT NULL
),
customer_totals AS (
    SELECT customer_id, SUM(amount) AS total_amount
    FROM paid_detail
    GROUP BY customer_id
)
SELECT c.customer_name, t.total_amount
FROM customer_totals AS t
INNER JOIN customers AS c ON t.customer_id = c.customer_id
WHERE t.total_amount > (
    SELECT AVG(total_amount)
    FROM customer_totals
)
ORDER BY t.total_amount DESC, t.customer_id;
```

结果：`bo | 17.00`、`ada | 15.00`。

这次平均的单位是“有支付订单的已登记客户”：客户总额 15、17、5，平均 `37 / 3`，约 12.3333 元。它与“每笔订单平均 40 / 7”是不同指标。cy、eve 不在此次平均范围内，匿名订单也不在范围内；如果任务要求全部客户含零订单，就需要按上一章的方法改造中间结果。

## 常见错误和边界

- 对子查询返回值的行数判断错误：单个值用标量子查询，多值匹配用 `IN`。
- 把“单笔金额大于平均”误写成“客户总金额大于平均”：先写清统计单位，再选分组方式。
- 在内层筛选了 `paid`，却忘记外层也需要它，导致取消订单混入。
- 以为 CTE 让重复数据自动消失：它保留内部查询的结果，重复与否取决于内部查询。
- 把 `WITH` 看作持久化存储；结束语句后名字失效，不会新增练习表。

## 就地练习

1. 用金额子查询查出单笔金额高于全部已支付订单平均金额的订单，核对 1001、1003、1005。
2. 用 `IN (SELECT ...)` 查出有已支付订单的客户，核对 ada、bo、dan。
3. 写 `paid_detail` CTE，按商品编号汇总已支付件数，核对 1→6、2→2、3→6。
4. 说明“有已支付订单的客户平均消费”和“全部客户平均消费”是否相同。当前分别是 `37 / 3` 与 `37 / 5`，匿名 3 元都不属于已登记客户。

完成检查：能说明子查询返回一行一列、多行一列、多个字段时分别如何使用；能把嵌套查询改写为 CTE；能说明 CTE 的有效范围；能说清客户均值和订单均值的分母。

随后完成[J05—J08](../../02_习题册/SQL/01_关联与进阶/题目.md)，再学习[06｜窗口函数](06_窗口函数.md)。

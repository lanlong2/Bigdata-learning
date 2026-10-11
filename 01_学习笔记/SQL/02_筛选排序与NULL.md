# 02 筛选、排序与 NULL

状态：待学习。前置：[01_基础查询](01_基础查询.md)。配套：[基础题 Q05—Q08](../../02_习题册/SQL/00_基础查询/题目.md)。新窗口先运行 `SET search_path TO sql_learning;`。

## 1. WHERE 选择要保留的行

`SELECT` 决定显示哪些列，`WHERE` 决定留下哪些行。条件成立才保留；不成立或结果未知都不保留。

```sql
SELECT order_id, quantity
FROM orders
WHERE quantity >= 3;
```

| order_id | quantity |
| --- | --- |
| 1003 | 3 |
| 1005 | 4 |

逐行看数量是否至少为 3，只留下两行。常用比较符号如下：

| 符号 | 意思 | 示例 |
| --- | --- | --- |
| `=` | 等于 | `status = 'paid'` |
| `<>` | 不等于 | `status <> 'cancelled'` |
| `>` / `>=` | 大于 / 大于或等于 | `quantity >= 3` |
| `<` / `<=` | 小于 / 小于或等于 | `unit_price < 5` |

SQL 用一个 `=` 比较相等，不写 Python 的 `==`。数字不加引号，文本值用英文单引号。

## 2. AND、OR 与括号

`AND` 要求两个条件同时成立，`OR` 要求至少一个成立。筛选“已支付且数量至少为 2”：

```sql
SELECT order_id, quantity, status
FROM orders
WHERE status = 'paid' AND quantity >= 2;
```

结果有 1001、1003、1005、1008 四笔订单。1004 虽然数量为 2，却是取消订单，因此不保留。

混合时 `AND` 优先于 `OR`。若想要“客户为 1 或 2，而且必须已支付”，显式写括号：

```sql
SELECT order_id, customer_id
FROM orders
WHERE (customer_id = 1 OR customer_id = 2)
  AND status = 'paid';
```

结果有 1001、1002、1003、1005、1008。写条件时先用中文说明每一组，再加括号。不能写 `customer_id = 1 OR 2`，每一边都必须是可判断的条件。

## 3. IN 与 BETWEEN

`IN` 表示“属于这个候选集合”，上面的条件可写成：

```sql
SELECT order_id, customer_id
FROM orders
WHERE customer_id IN (1, 2)
  AND status = 'paid';
```

结果相同。括号里用逗号分隔值，不写 Python 的方括号。

`BETWEEN a AND b` 表示闭区间，包含两端：

```sql
SELECT product_name, unit_price
FROM products
WHERE unit_price BETWEEN 2 AND 5;
```

结果是 `pen` 3.00、`notebook` 5.00、`eraser` 2.00。相当于 `unit_price >= 2 AND unit_price <= 5`；下界写在前，不会自动交换错误的上下界。SQL 不能写 `2 <= unit_price <= 5`。

课程日期列是 `DATE`（日期，不含一天中的时分秒）。用 `DATE '2026-10-02'` 明确表示日期值：

```sql
SELECT order_id, order_date
FROM orders
WHERE order_date BETWEEN DATE '2026-10-02' AND DATE '2026-10-03';
```

结果为 1003、1004、1005、1006，包括 2 日和 3 日。将来碰到带时间的时间戳列，不要照搬“末日零点”表示整天；本阶段只处理 `DATE`。

## 4. LIKE 做简单文字匹配

`LIKE` 使用模式检查整个文本。模式中的 `%` 表示零个或更多字符，`_` 表示恰好一个字符。

```sql
SELECT product_name
FROM products
WHERE product_name LIKE '%e%';
```

返回 `pen`、`notebook`、`eraser`，因为名字任意位置包含 `e`。

| 模式 | 意思 | 课程数据示例 |
| --- | --- | --- |
| `'p%'` | 以 p 开头 | pen |
| `'%r'` | 以 r 结尾 | eraser |
| `'%e%'` | 任意位置有 e | pen、notebook、eraser |
| `'__'` | 恰好两个字符 | 客户名 bo、cy |

本课程使用普通默认排序规则，`LIKE` 会区分英文字母大小写，`'P%'` 不匹配 `pen`。匹配规则可能受数据库排序规则影响；暂不自定义规则。文字中真的含有 `%` 或 `_` 时要额外使用转义写法，本模块题目不涉及。

## 5. 缺失值用 IS NULL 判断

`NULL` 表示没有已知值。它不是 `'NULL'` 这四个字母，不是空字符串，也不是 0。与缺失值做普通比较无法断定真或假：

```sql
SELECT customer_id, customer_name
FROM customers
WHERE city IS NULL;
```

| customer_id | customer_name |
| --- | --- |
| 5 | eve |

已知城市则用 `city IS NOT NULL`，会留下四位客户。不要使用 `city = NULL` 或 `city <> NULL`，它们不是正确的缺失判断。

```sql
SELECT customer_id, customer_name, city
FROM customers
WHERE city <> '北京';
```

这条只有 `bo`（上海）、`dan`（广州），没有 `eve`；未知城市不代表已知“不是北京”。如果明确要包括缺失城市，写：

```sql
SELECT customer_id, customer_name, city
FROM customers
WHERE city <> '北京' OR city IS NULL;
```

此时返回 `bo`、`dan`、`eve`。同理，`customer_id IN (1, 2)` 不会选中客户编号缺失的 1007；需要缺失行时另加 `OR customer_id IS NULL`，不要把 `NULL` 放进 `IN` 列表期待它匹配。

## 6. ORDER BY 排序

默认升序 `ASC`，降序用 `DESC`；多个排序键用逗号分隔。先按数量降序，相同数量再按订单编号升序：

```sql
SELECT order_id, quantity
FROM orders
WHERE status = 'paid'
ORDER BY quantity DESC, order_id ASC;
```

| order_id | quantity |
| --- | --- |
| 1005 | 4 |
| 1003 | 3 |
| 1001 | 2 |
| 1008 | 2 |
| 1002 | 1 |
| 1006 | 1 |
| 1007 | 1 |

不要认为 `DESC` 会作用于前面所有列：`ORDER BY quantity DESC, order_id` 中第二列默认升序。使用唯一订单编号打破并列，才能固定全部行的相对顺序。

PostgreSQL 升序默认把 `NULL` 放最后，降序默认放最前。需要明确位置时写 `NULLS FIRST` 或 `NULLS LAST`，例如：

```sql
SELECT order_id, customer_id
FROM orders
ORDER BY customer_id ASC NULLS LAST, order_id ASC;
```

客户编号缺失的 1007 最后显示。中文城市的先后可能随排序规则不同；要核对固定顺序的练习优先用数值编号排序。

## 7. LIMIT 取前几行

```sql
SELECT order_id, quantity
FROM orders
WHERE status = 'paid'
ORDER BY quantity DESC, order_id ASC
LIMIT 3;
```

结果只有前三笔：1005（4）、1003（3）、1001（2）。`LIMIT 3` 最多取三行，有并列也不会自动扩展到四行。1008 数量同为 2，但编号更大，按题意排在第四。

没有 `ORDER BY` 时，“前 3 行”没有确定业务含义；只有数量排序而没有打破并列时，第三行也可能不稳定。`LIMIT 0` 返回零行；匹配行数不足时只返回已有行。

本阶段完整书写顺序是：

```sql
SELECT 要显示的列
FROM 来源表
WHERE 行条件
ORDER BY 排序列
LIMIT 行数;
```

这是语法示意，中文占位文字不能直接运行。可先理解为：读表 → 筛选行 → 选择结果列 → 排序 → 限制行数；这是帮助理解的逻辑顺序，不是在描述数据库实际执行计划。

## 8. 就地练习与完成检查

1. 找北京客户，显示编号与姓名，编号升序。预期 1/ada、3/cy。
2. 找已支付且数量在 2 到 3 之间的订单，编号升序。预期 1001、1003、1008。
3. 找姓名恰好两个字符的客户。预期 bo、cy。
4. 找客户编号缺失的订单。预期 1007。
5. 找最贵的两种商品，价格降序、商品编号升序。预期 mug 20.00、notebook 5.00。

完成检查：能写组合条件与括号；解释闭区间和模糊匹配；正确判断缺失值；给“前 N 行”写出稳定排序；不会混淆列选择与行筛选。随后做 [Q05—Q08](../../02_习题册/SQL/00_基础查询/题目.md)，再进入 [03_聚合与分组](03_聚合与分组.md)。

## 官方依据

- [查询表](https://www.postgresql.org/docs/18/tutorial-select.html)：筛选与排序。
- [比较与缺失判断](https://www.postgresql.org/docs/18/functions-comparison.html)：闭区间、未知比较结果与 `IS NULL`。
- [文字模式匹配](https://www.postgresql.org/docs/18/functions-matching.html)：`LIKE`、`%` 与 `_`。
- [限制行数](https://www.postgresql.org/docs/18/queries-limit.html)：`LIMIT` 与确定排序。

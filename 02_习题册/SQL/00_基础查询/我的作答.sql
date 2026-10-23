-- SQL 基础查询个人作答模板：尚未作答。
-- 在 DBeaver 中连接 MySQL 8.4 LTS，只在专用学习数据库 sql_learning 运行。
-- 可以使用自己的别名；题目要求的结果列、条件与排序需要满足。
USE sql_learning;
-- 阶段一：学完 01_基础查询后




-- Q01 指定列
-- 在下面填写自己的 SQL：
select customer_id, customer_name from customers limit 5;

desc customers;

select * from customers ;

select * from products;


-- Q02 列别名
select product_name as "item_name", unit_price as "price" from products;

-- Q03 表达式
select product_name, unit_price*4 as "four_unit_cost" from products;

-- Q04 去重
-- 文字说明：
select distinct category from products ;

-- 阶段二：学完 02_筛选排序与NULL后

-- Q05 支付状态与数量区间
select order_id , quantity from orders where quantity between 2 and 3;

-- Q06 版本一：IN
select order_id ,product_id from orders where product in (1,3) order by  asc;


-- Q06 版本二：带括号的 OR
-- 括号说明：
select order_id ,product_id from orders where product_id = 1 
or product_id = 3 order by order_id asc;

-- Q07 日期与前两笔

select order_id,order_date from orders  where order_date
between date "2026-10-02" and date "2026-10-04" and status ="paid"
order by order_id desc , product_id asc  
limit 2;
-- Q08.1 城市不是北京，包含缺失城市


-- Q08.2 名称包含 e
-- 缺失值说明：
select customer_id,customer_name,city from customers 
where city <> "北京" or city is null
order by customer_id asc;

-- 阶段三：学完 03_聚合与分组后

-- Q09 已支付订单总览

select count(quantity) as order_quantity,sum(quantity) as quantity,avg(quantity) as avg_quantity 
,min(quantity) as min_quantity,max(quantity) as max_quantity
from orders
where status = "paid";
select * from orders;
-- Q10 总行数与已知客户编号行数
-- 差值说明：

select count(*) as all_orders,count(customer_id) as order_with_cusromer
from orders;
-- 里面有一个客户编号未知


-- Q11 每种商品的已支付统计
-- 商品 4 未出现的原因：
select product_id,count(order_id) as order_count
,sum(quantity) as total_quantity
from orders
where status="paid"
group by product_id
order by product_id asc;

-- Q12.1 只保留数量合计至少 5 的商品组

select product_id,count(order_id) as order_count
,sum(quantity) as total_quantity
from orders
where status="paid" 
group by product_id
having sum(quantity)>=5
order by product_id asc;

-- Q12.2 空输入的不分组聚合
-- 结果行数、COUNT、SUM：
-- 加上分组后的行数与原因：
select count(*) as order_count,sum(quantity) as total_quantity
from orders
where order_id <0;

--
select product_id, count(*) as order_count,sum(quantity) as total_quantity
from orders
where order_id <0
group by product_id;


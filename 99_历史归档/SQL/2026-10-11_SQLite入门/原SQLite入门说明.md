# SQLite 入门 · SQL第一课

这份练习用于熟悉 DBeaver、SQL 文件和 GitHub 保存流程，使用 SQLite。原文件来自桌面的 `SQL第一课.sql`，2026-10-11 原样加入项目。它是助手配置环境时使用的示例，不代表已经完成项目中的教材或习题。

## 从哪里打开

双击桌面的 **SQL第一课（项目版）** 快捷方式，或在 DBeaver 用“文件 → 查找所指定的文件”打开本目录的 [SQL第一课.sql](SQL第一课.sql)。

确认编辑器上方的数据源是 `sql-learning.db`；如果显示 `<none>`，按 **Ctrl+9**，选择已有的 `sql-learning.db`。快捷方式只适用于这台电脑，换电脑后按该电脑的实际路径打开项目文件并配置连接。

以后编辑这一份项目文件，按 **Ctrl+S** 就保存到仓库目录。桌面原来的 `SQL第一课.sql` 保留为初次练习副本，与项目文件不会自动互相更新。要继续参与 Git 同步，请使用“项目版”。

## 保存和执行分别做什么

| 操作 | 作用 |
|---|---|
| Ctrl+S | 保存 `.sql` 中的代码文字 |
| 选中语句，再按 Ctrl+Enter | 在当前连接的数据库执行选中语句 |
| Git commit | 在本机仓库保存一个可回看的版本 |
| Git push | 将提交上传到 GitHub |

文件中的建表和插入语句已经在当前 SQLite 学习库执行过。继续练习时只选中最后三行查询，不要重复执行前面的建表和插入语句：

```sql
SELECT id, name, score
FROM students
ORDER BY id;
```

当前学习库应返回三行：小明 80、小红 95、小华 88。运行查询不会替你保存 SQL 文件；保存文件也不会替你执行查询。

## 如何上传

按 [DBeaver 与 GitHub 同步说明](../../../01_学习笔记/Git/DBeaver与GitHub同步.md) 操作。

`.sql` 是代码文件，`.db` 是 SQLite 的表和数据。上传代码不会自动上传当前数据库，也不会自动在另一台电脑执行代码。新电脑需要另外建立 SQLite 连接，指向新的数据库文件，然后依次执行一次建表、插入和查询。

## 与正式教材的关系

本项目的主线教材使用 **PostgreSQL**，学习数据是 `customers`、`products`、`orders`；当前 SQLite 的 `students` 是单独的环境练习。

开始主线教材时，先按 [00 环境与关系表](../../../01_学习笔记/SQL/00_环境与关系表.md) 配置 PostgreSQL，并在 DBeaver 中另建 PostgreSQL 连接。教材中的 `CREATE SCHEMA`、`SET search_path` 等不能直接在当前 SQLite 连接执行。正式习题继续使用原有的“我的作答.sql”。

[返回 SQL 习题入口](../README.md)

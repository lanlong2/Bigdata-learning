# 大数据学习 · 从这里开始

**2026-10-10：Python学习阶段已结束，已进入SQL学习阶段。** 2026-10-11已决定将当前数据库统一为MySQL 8.4 LTS，使用DBeaver学习表与查询；配置与教材迁移由助手实施。Python资料、原作答、评分与阶段历史均保留在各用途目录的 `Python` 大类中。

下一步直接打开[SQL 00 环境与关系表](01_学习笔记/SQL/00_环境与关系表.md)，按说明在DBeaver连接MySQL，使用专用数据库`sql_learning`：先执行`USE sql_learning;`，再运行`SELECT 1;`。首次准备课程数据使用[重建练习库脚本](01_学习笔记/SQL/练习数据/00_重建练习库.sql)，重建前先读00模块说明。接着按[SQL教材入口](01_学习笔记/SQL/README.md)的模块→习题对应关系推进。SQL模块、习题、测验和项目的完成情况随后按实际学习记录更新。

年度主线：Python → SQL／MySQL → Pandas → 项目 → 实习。SQLite入门练习保留在[SQL历史归档](99_历史归档/SQL/README.md)，当前按MySQL教材学习。

## 每次学习这样开始

1. 看[当前阶段与下一步](07_学习阶段与下一步/README.md)和[SQL近期执行计划](00_学习计划/SQL/近期执行计划.md)，只选一个主要任务。
2. 按顺序读[SQL教材](01_学习笔记/SQL/README.md)，运行示例，再做[对应习题](02_习题册/SQL/README.md)。
3. 把自己的查询保存为 `.sql` 文件，在数据库查询编辑器中执行。第一次连接和导入数据按[00模块](01_学习笔记/SQL/00_环境与关系表.md)操作。
4. 结束时更新[SQL进度](00_学习计划/SQL/当前进度.md)和[SQL学习日志](00_学习计划/SQL/学习日志.md)。错题或疑问由你选定内容后再收录。

## 按用途和技术查找

先选用途，再进入 `Python` 或 `SQL` 文件夹；根目录入口和共用资料用于全局导航。

| 用途 | Python | SQL |
|---|---|---|
| [00 学习计划](00_学习计划/README.md) | [阶段完成记录](00_学习计划/Python/README.md) | [当前学习计划](00_学习计划/SQL/README.md) |
| [01 学习笔记](01_学习笔记/README.md) | [Python教程](01_学习笔记/Python/README.md) | [SQL教程](01_学习笔记/SQL/README.md) |
| [02 习题册](02_习题册/README.md) | [Python习题](02_习题册/Python/README.md) | [SQL习题](02_习题册/SQL/README.md) |
| [03 阶段试卷](03_阶段试卷/README.md) | [Python试卷与评分](03_阶段试卷/Python/README.md) | [SQL阶段测验入口](03_阶段试卷/SQL/README.md) |
| [04 错题与疑问](04_错题与疑问/README.md) | [Python错题与疑问](04_错题与疑问/Python/README.md) | [SQL目录（等你指定内容）](04_错题与疑问/SQL/) |
| [05 项目实践](05_项目实践/README.md) | [Python项目](05_项目实践/Python/README.md) | [SQL项目](05_项目实践/SQL/README.md) |
| [06 学习方法](06_学习方法/README.md) | [Python学习方法](06_学习方法/Python/README.md) | [SQL学习方法](06_学习方法/SQL/README.md) |
| [07 学习阶段与下一步](07_学习阶段与下一步/README.md) | [Python完整阶段历史](07_学习阶段与下一步/Python/README.md) | [SQL当前阶段](07_学习阶段与下一步/SQL/README.md) |
| [08 案例学习](08_案例学习/README.md) | [Python案例](08_案例学习/Python/README.md) | [SQL案例](08_案例学习/SQL/README.md) |
| [09 AI文档学习](09_官方文档阅读/README.md) | [Python文档入口](09_官方文档阅读/Python/README.md) | [SQL文档阅读](09_官方文档阅读/SQL/README.md) |
| [99 历史归档](99_历史归档/README.md) | [Python原始资料](99_历史归档/Python/README.md) | [SQL归档入口](99_历史归档/SQL/README.md) |

全局资料：[当前进度](00_学习计划/当前进度.md) · [近期执行计划](00_学习计划/近期执行计划.md) · [年度路线](00_学习计划/年度路线与验收.md) · [预算记录](00_学习计划/预算与实际记录.md)。

## 在VS Code中使用

- 用“文件 → 打开文件夹”打开整个 `bigdata-learning`。
- 打开 `.md` 后按 **Ctrl+Shift+V** 看预览，单击链接跳转；修改后按 **Ctrl+S** 保存。
- SQL作答写在 `.sql` 中，在DBeaver连接的MySQL查询编辑器执行；查询前确认`USE sql_learning;`。SQL语句的执行环境见00模块。
- 回查Python时，在 `.py` 中作答；包含 `__file__` 的文件读写代码先保存，再运行整个文件。

## 学习记录规则

教材按知识依赖排序，学一节练对应题；示例、材料生成与助手验证分别作为资料维护记录。你明确说已完成、已订正、已学完、已达标、已掌握、复测通过或说明用时，直接写为学习事实。

Python模块00—09已全部完成，M01—M06习题完成和本地清洗项目基本完成、已修正的记录保留。前56节首测41/100、函数首测49/100及订正58/70、综合卷首测55/100仍是历史成绩。旧题、复测与项目历史建议可按需回查，当前主线执行SQL计划。具体协作规则见[AGENTS.md](AGENTS.md)。

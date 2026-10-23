# Java后端 · 官方阅读任务

第一条大模型应用路线结束后开始Java。本页为阅读导航，不代表已经安装JDK 21、开始Java学习或完成阅读。以下入口在2026-10-23维护时核对，实际开始相应阶段前再次核对维护版本与兼容关系。

| 阶段 | 官方入口 | 当前阅读任务 |
|---|---|---|
| J00—J01 | [dev.java学习入口](https://dev.java/learn/getting-started/) | 先认识JDK、编译与运行，再从站内学习语言、类、集合、异常、IO与必要的并发；本地教材按依赖展开 |
| J02 | Java官方学习材料中的集合、执行与IO说明；网络/OS中文教材待展开 | 能解释算法复杂度与基本数据结构，并沿请求说明网络、进程线程与IO，不把概念名当作掌握 |
| J03 | [MySQL 8.4手册](https://dev.mysql.com/doc/refman/8.4/en/) | 从已学SQL转向索引、执行计划、事务隔离和锁；JDBC具体驱动文档在开学时按实际版本补充 |
| J04 构建 | [Maven Getting Started](https://maven.apache.org/guides/getting-started/) | 工程目录、`pom.xml`、依赖与构建生命周期分别负责什么？ |
| J04 框架 | [Spring Boot System Requirements](https://docs.spring.io/spring-boot/system-requirements.html) | 核对所选Boot版本支持哪些Java与构建工具，再从官方教程开始应用与测试 |
| J04 数据访问 | [MyBatis Getting Started](https://mybatis.org/mybatis-3/getting-started.html) | SQL如何映射到Java对象，参数怎样传入，连接和事务由谁管理？Spring整合材料在实际开学时核对 |
| J05 | [Redis Get Started](https://redis.io/docs/latest/develop/get-started/) | 缓存读写和过期怎样运行，什么数据适合缓存，更新后怎样避免旧值？ |
| J06 | 所选框架、数据库与部署方式的官方文档 | 把每个设计问题连到可验证的行为，记录版本、运行条件和排错入口 |

建议以JDK 21 LTS教学，不把“建议版本”写成“本机已安装”。Spring Boot具体小版本、依赖组合、MyBatis整合方式和Redis客户端，按真正开学时间核对官方支持情况，不将今天的网页版本固定到未来。

官方文档补充本地教材，不替代概念解释、完整例子和练习。J01—J06中文分节教材与新习题目前尚待按进度展开；先按路线预算安排，不误记成材料全部完成。

[Java教材](../../01_学习笔记/Java/README.md) · [Java入门第一节](../../01_学习笔记/Java/00_认识Java与第一个程序.md) · [官方文档入口](../README.md)

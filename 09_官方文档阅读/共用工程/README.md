# 共用工程 · 官方资料与迁移问题

资料按第一次需要时阅读，共用概念不重复计课时。Python中理解过的HTTP、数据库和日志，在Java中重点学习相应实现与差异。

| 问题 | 官方资料 | 怎样用 |
|---|---|---|
| 不同项目如何隔离Python依赖？ | [venv](https://docs.python.org/3/library/venv.html) | 配合A01解释器检查，不向全局环境堆依赖 |
| 相对路径为何换目录就失效？ | [pathlib](https://docs.python.org/3/library/pathlib.html) | 用脚本位置与工作目录做对比；输出使用新的练习目录 |
| 程序出错后怎样留下线索？ | [Python logging](https://docs.python.org/3/library/logging.html) | 记录功能、失败和可定位上下文，避免密钥与不必要的个人信息 |
| 修改后怎样确认原功能还有效？ | [Python unittest](https://docs.python.org/3/library/unittest.html) | 先学本地最小断言示例，再学类与测试组织；Java阶段迁移相同检查思路 |
| 怎样把函数变成可调用接口？ | [FastAPI入门](https://fastapi.tiangolo.com/tutorial/first-steps/) | 从一次请求的输入、校验、处理、响应解释完整过程 |
| 数据关系、索引和事务怎样查证？ | [MySQL 8.4](https://dev.mysql.com/doc/refman/8.4/en/) | A00先学SQL，J03进一步查索引与隔离，不混用其他数据库命令 |
| Java依赖如何跟项目走？ | [Maven入门](https://maven.apache.org/guides/getting-started/) | 对照Python依赖清单理解构建与依赖管理的相同目标及不同实现 |

Git仍使用[现有共用说明](../../01_学习笔记/Git/README.md)，其中旧测验日期和评分保留为历史，不因新路线重新要求完成旧阶段。Linux与部署在项目时按实际环境补完整步骤及官方入口，不提前引入整套运维课程。

链接核对和助手验证不计用户阅读或实操完成。用户学习用时、完成与订正按其明确陈述记录。

[共用工程导航](../../01_学习笔记/共用工程/README.md) · [官方文档入口](../README.md)

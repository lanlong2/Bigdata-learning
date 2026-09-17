# Git · 保存学习成果的说明

## 命令写在哪里

VS Code打开整个bigdata-learning文件夹，选择“终端 → 新建终端”。命令写在终端，每次一行，**不要写进Python文件**。
先运行 `Get-Location` 和 `git status`，确认自己在学习仓库。

## 一次正常保存

先Ctrl+S保存文件，再逐行运行：

```powershell
git status
git diff
git add .
git diff --cached
git commit -m "学习：完成函数基础练习并记录错题"
git push
```

| 命令 | 简单理解 |
|---|---|
| git status | 看哪些文件变了 |
| git diff | 查看未暂存的改动；新文件另在编辑器中打开检查 |
| git add . | 把当前目录改动放入准备提交的清单，删除也计入 |
| git diff --cached | 检查即将提交的具体内容 |
| git commit | 在本地保存一个版本 |
| git push | 上传提交到已配置的远程仓库 |

提交说明写实际成果，不为凑天数制造空提交。push若提示没有远程或上游分支，先记录错误，查看 `git remote -v` 和 `git branch -vv`，不要复制陌生仓库地址。

## 多台电脑学习

开始前先确认工作区干净，再用 `git pull --ff-only` 获取远程提交。
有未提交改动或提示不能快进，先理解原因，不直接强制覆盖。

## 忽略文件

根目录.gitignore用来忽略Python缓存、虚拟环境等本地文件；以后用API时不上传密钥配置。
已经跟踪的文件不会因忽略规则而自动退出历史。

## 自查

- [ ] 能区分add、commit、push保存到哪里。
- [ ] 会在提交前查看改动。
- [ ] 能解释提交中包含什么。

原hello.py保存在[首次运行示例](首次运行_hello.py)。这次整理只修改本地资料，没有替你commit或push。

[返回总导航](../../README.md)

# 类型注解与模块 · 2026-10-06助手订正稿
# 原作答保留在“我的作答.py”；此文件用于逐题对照。
# M03、M04的双文件示例请分别运行helpers.py和run_examples.py。

# M01：保留area、width和height，补上题目要求的调用检查。
def area(width: int, height: int) -> int:
    return width * height


print(area(3, 4))  # 12


# M02：注解不会转换数据；字符串乘2是重复两次。
def twice(value: int) -> int:
    return value * 2


def parse_twice(value):
    return int(value) * 2


print(twice("3"))  # 字符串33
print(type(twice("3")).__name__)  # str
print(parse_twice("3"))  # 整数6
print(parse_twice(3))  # 整数6


# M03、M04：helpers.py中的函数和入口保护已经正确。
# 导入helpers时，入口保护内的演示不会运行。
# run_examples.py实际导入并调用一次，单独运行它只输出一行alice。
from helpers import clean_name

print(clean_name(" Alice "))  # alice


# M05：从tools包的cleaning模块导入clean_name函数。
# from tools.cleaning import clean_name
# 普通包示例中的__init__.py可以为空。
# 本题只分析给定结构，不必另建tools目录，所以导入语句保留为注释。


# M06：保留a、text和restore，添加ensure_ascii=False来保留中文。
import json

a = {"城市": "杭州", "数量": 3}
text = json.dumps(a, ensure_ascii=False)
restore = json.loads(text)

print(text)  # {"城市": "杭州", "数量": 3}
print(type(text).__name__)  # str
print(type(restore).__name__)  # dict
print(a == restore)  # True

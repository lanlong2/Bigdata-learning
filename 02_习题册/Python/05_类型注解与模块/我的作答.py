# 类型注解与模块日常习题作答
# 题目、答案解析各为独立文件；这里只写自己的答案。
# 每题独立，需要运行某题时连同它的初始数据／函数定义一起选中。
# 空白模板无输出是正常的。

# M01 · 给函数加说明类型
# 我的思路／预测：
def area(width:int,height:int)->int:
    return width*height



# M02 · 注解会自动转换吗
# 我的思路／预测：
# 预测：得33



# M03 · 导入自己的模块
# 我的思路／预测：
from helpers import clean_name
print(clean_name(" Alice "))



# M04 · 避免导入时自动演示
# 我的思路／预测：
print(clean_name(" Alice "))




# M05 · 看懂包的路径
# 我的思路／预测：
# from tools.cleaning import cleaning
# 可以为空



# M06 · 使用标准库JSON
# 我的思路／预测：
import json
a={"城市":"杭州","数量":3}
text=json.dumps(a)
restore=json.loads(text)
print(type(text).__name__)
print(type(restore).__name__)
print(a==restore)
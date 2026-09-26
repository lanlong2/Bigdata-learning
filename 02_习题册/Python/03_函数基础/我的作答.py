# 函数基础日常习题作答
# 题目、答案解析各为独立文件；这里只写自己的答案。
# 每题独立，需要运行某题时连同它的初始数据／函数定义一起选中。
# 空白模板无输出是正常的。

# F01 · 让函数返回一句问候
# 我的思路／预测：
def greet(name):
    return "你好"+name
print(greet("小林"))

# F02 · 计算总价
# 我的思路／预测：
def total_cost(price,quantity):
    return price*quantity
print(total_cost(8,3))
# F03 · 返回格式化记录
# 我的思路／预测：
def score_label(name,score):
    return str(name+":"+score)
print(score_label("小林",86))


# F04 · 区分打印和返回
# 我的思路／预测：
#预测：第一个输出5，第二个输出零，因为函数没有return东西
#改写：
def add(a,b):
    print(a+b)
    return a+b
result=add(2,3)
print(result)


# F05 · 处理空列表
# 我的思路／预测：
def average(scores):
    if scores:
        sum=0
        for i in scores:
            sum=sum+i
        return sum/len(scores)
    else:
        return None
print(average([60,80,100]))


# F06 · 封装名字清洗
# 我的思路／预测：
def normalize_name(name):
    name_c=name.strip()
    return name_c
print(normalize_name(" Alice Smith \n"))

# F07 · 返回一条元组记录
# 我的思路／预测：
def parse_record(raw):
    raw1=raw.split(",")
    i,p=raw1
    i1=i.strip()
    p1=int(p.strip())
    return (i1,p1)
print(parse_record(" 小林 , 86 "))
    



# F08 · 让函数相互调用
# 我的思路／预测：
def total(scores):
    sum=0
    for i in scores:
        sum=sum+i
    return sum
def average(scores):
    sum=0
    for i in scores:
        sum=sum+i
    return sum/len(scores)
def summarize(scores):
    if scores:
        return (total(scores),average(scores))
    else:
        return (0,None)
a=[79,49,60]
print(summarize(a))
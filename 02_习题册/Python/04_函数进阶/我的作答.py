# 函数进阶日常习题作答
# 题目、答案解析各为独立文件；这里只写自己的答案。
# 每题独立，需要运行某题时连同它的初始数据／函数定义一起选中。
# 空白模板无输出是正常的。

# G01 · 作用域预测
# 我的思路／预测：
#一：6 二：10，不改变，value是形参



# G02 · 用关键字传参
# 我的思路／预测：
def format_record(name,score):
    return name+":"+str(score)
format_record("小林",86)
format_record(score=86,name="小林")



# G03 · 默认分数线
# 我的思路／预测：
def is_pass(score,threshold=60):
    if score >= 60:
        return True
    else:
        return False
print(is_pass(59))
print(is_pass(60))
print(is_pass(79,80))
# G04 · 任意数量的数
# 我的思路／预测：
def total_numbers(*numbers):
    if numbers:
        sum=0
        for i in numbers:
            sum=sum+i
        return sum
    else:
        return 0
#说明：元组



# G05 · 关键字信息
# 我的思路／预测：
def build_label(**fields):
    return fields.get("name","未命名")+"@"+fields.get("city","未知")
print(build_label(name="小林",city="杭州"))


# G06 · 把函数当参数
# 我的思路／预测：
def twice(x):
    x=x*2
    return x
def apply_to_value(values,operation):
    a=[]
    for i in values:
        a.append(operation(i))
    return a
print(apply_to_value([1,2,3],twice))


# G07 · 按成绩排序
# 我的思路／预测：
def rank_scores(rows):
    if rows:
        a=sorted(rows,key=lambda row: row[1],reverse=True)
        return a
    else:
        return []
rows = [("小林",80),("小红",90),("小白",84)]
print(rank_scores(rows))

# G08 · 参数控制筛选与汇总
# 我的思路／预测：
def summarize_orders(orders,min_quantity=1):
    a=0
    sum1=0
    for i in orders:
        if i[1]>=1:
            a=a+1
            sum1=sum1+a[i[1]]
    if a:
        return (0,0)
a=[("手机",3),("电脑",0),("耳机",1),("汽车",2)]
print(summarize_orders(a,1))


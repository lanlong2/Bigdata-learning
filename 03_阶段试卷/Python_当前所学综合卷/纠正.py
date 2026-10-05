# ## C · 基础语法与容器实作（25分）

# 这部分可直接写脚本，不强制封装函数；若封装，保持题目行为与输出一致。

# ### C01 · 按指令接收到货（10分）

# ```python
# commands = ["3", "0", "-2", "5", "stop", "100"]
# initial_stock = 2
# box_size = 4
# ```

# 用**while循环**按顺序读取列表中的字符串；必须实际使用break和continue：

# - 遇到`"stop"`立即停止，其后命令不处理；没有stop就处理到列表结束。
# - 其余字符串保证能转int；小于等于0的数量跳过，正数加入初始库存。
# - 按box_size计算能装满几箱、余下多少件。initial_stock为非负整数，box_size为正整数；不可写死本例数值。
# - 不修改commands。输出以下三行：

# ```text
# 总库存：10件
# 整箱：2箱
# 剩余：2件
# ```

commands = ["3", "0", "-2", "5", "stop", "100"]
initial_stock = 2
box_size = 4
i=0
sum1=initial_stock
while i < len(commands):
    a=commands[i]
    i=i+1
    if a=="stop":
        break
    else:
        if int(a)>0:
            sum1=sum1+int (a)
        else:
            continue
#sum1
box=sum1//box_size
#box
rest=sum1%box_size
#rest
print(f"总库存：{sum1}件")
print(f"整箱：{box}件")
print(f"剩余：{rest}件")


# ### C02 · 小组成绩日报（15分）

# ```python
# rows = [("小周", 58), ("小林", 90), ("小白", 60), ("小陈", 80), ("小许", 100)]
# ```

# 姓名不重复，分数为0—100整数。用循环拆出姓名与分数，不修改rows；完成以下要求：

# - 计算总分，非空时平均分保留一位小数；空列表平均分显示`无`。
# - 分数>=60的姓名保存到**列表**，保持原顺序，用顿号连接；无人及格显示`无`。
# - 用**字典**统计优秀90—100、良好80—89、及格60—79、待加强0—59的人数。四档互斥，不重复计算。
# - 按以下固定顺序输出七行：

# ```text
# 总分：388
# 平均分：77.6
# 及格名单：小林、小白、小陈、小许
# 优秀：2人
# 良好：1人
# 及格：1人
# 待加强：1人
# ```
sum1=0
a=[]
w=0
j=0
l=0
y=0
rows = [("小周", 58), ("小林", 90), ("小白", 60), ("小陈", 80), ("小许", 100)]
for i in rows:
    sum1=sum1+i[1]
    #sum1
    if i[1]>=60:
        a.append(i[0])
    else:
        pass
    if i[1]<60:
        w=w+1
    elif i[1]>=60 and i[1]<80:
        j=j+1
    elif i[1]>=80 and i[1]<90:
        l=l+1
    elif i[1]>=90 and i[1]<=100:
        y=y+1

if a:
    print(f"总分：{sum1}")
else:
    print("无")
if a:
    avg=sum1/len(rows)
    print(f"平均分：{avg:.1f}")
else:
    print("无")
if a:
    print(f"及格名单：{"、".join(a)}")
else:
    print("无")
print(f"优秀：{y}人")
print(f"良好：{l}人")
print(f"及格{j}人")
print(f"待及格{w}人")

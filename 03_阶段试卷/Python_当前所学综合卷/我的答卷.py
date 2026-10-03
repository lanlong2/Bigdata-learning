# 当前所学综合卷：100分，建议150分钟。
# 试卷见同目录试卷.md，整卷完成后再看参考答案与评分.md。
# 日期：10.3
# 开始／结束时间：18：04，20：03
# 实际用时（扣除休息）：一个小时54分钟
# 一次／分两次完成，期间是否查资料：一次完成，没看资料
# 独立／提示／看解析及涉及题号：全部独立完成
# 每道大题独立；D04可调用D01，E题内部共享函数。

# A01（5分）三行输出：
#buy,
# 2 1,
# 28


# A02（5分）三行输出与说明：
#7
#None
#10
#说明：函数没有返回值

# B01（5分）问题说明及修复：
tags = [" SQL ", "python", " Data "]
#处理好的tag没有东西保存,sorted也是
a=[]
for tag in tags:
    a.append(tag.strip().lower())
b=sorted(a)
print("|".join(b))

# B02（5分）问题说明及修复：
position = (3, 8)
#不能直接从元组修改值
a=(6,position[1])
print(a)


# B03（5分）问题说明、keep_valid与调用：
#这样直接移除了原value的值，同时没有返回【】
def keep_valid(values):
    a=[]
    if values:
        for value in values:
            if value < 0:
                pass
            else:
                a.append(value)
        return a
    else:
        return []
print(keep_valid([4,-1,-2,0,3]))


# C01（10分）到货指令：
commands = ["3", "0", "-2", "5", "stop", "100"]
initial_stock = 2
box_size = 4
a=[]
sum1=0
for i in commands:
    while i < len(commands):
        if i=="stop":
            break
        else:
            if int(i)>0:
                a.append(int(i))
            else:
                pass
for i in a:
    sum1=sum1+i
print(f"""
总库存：{sum1}件
装箱：{sum1//box_size}
剩余：{sum1%box_size}
""")



# C02（15分）成绩日报：
rows = [("小周", 58), ("小林", 90), ("小白", 60), ("小陈", 80), ("小许", 100)]
sum1=0
for i in rows:
    sum1=sum1+i[1]
#sum1
avg=round(sum1/len(rows),1)
#avg
names=[]
for i in rows:
    if i[1]>=60:
        names.append(i[0])
    else:
        pass
names1=",".join(names)
#names
w=0
j=0
l=0
y=0
for i in rows:
    if i[1]<60:
        w=w+1
    elif i[1]>=60 and i[1]<79:
        j=j+1
    elif i[1]>=80 and i[1]<89:
        l=l+1
    elif i[1]>=90 and i[1]<=100:
        y=y+1
print(f"""
总分:{sum1}
平均分：{avg}
及格名单：{names1}
优秀：{y}人
良好：{l}人
及格：{j}人
待加强：{w}人
""")



# D01（6分）sum_minutes及列表拆包调用：
parts = [15, 30, 10]
def sum_minutes(*minutes):
    sum1=0
    if minutes:
        for i in minutes:
            sum1=sum1+i
        return sum1
    else:
        return 0
print(sum_minutes(20,0,40))
print(sum_minutes(parts))

# D02（5分）course_label与调用：
def course_label(**fields):
    topic=fields.get("topic","未分类")
    level=fields.get("level","入门")
    return topic+"/"+level


# D03（6分）apply_rule、clean_topic与两种规则调用：
def clean_topic(text):
    return text.lower().strip()
def apply_rule(values,operation):
    a=[]
    if values:
        for i in values:
            a.append=len(operation(i))
        return a
    else:
        return []
    


# D04（8分）session_summary与调用：
sessions = [('python', 20), ('sql', 40), ('python', 30), ('git', 0)]
def session_summary(sessions,min_minutes=30):
    a=[]
    h=0
    sum=0
    if min_minutes==100 or sessions==False:
        for i in sessions:
            if i[1]>=min_minutes:
                a.append(i)
                h=h+1
                sum=sum+i[1]
                
            else:
                pass
    avg=sum/len(a)   
    return (h,sum,avg)         


# E题初始数据：
raw = " Ada ,Python;bo,SQL;ADA,python;;cy,Python; Bo ,Linux;ada,sql; \n"

# E01（5分）parse_signins：
def parse_signins(raw):
    if raw:
        a=raw.split(";")
        f=[]
        for i in a:
            if i:
                h=i.split(",")
                h0=h[0].strip().lower()
                h1=h[1].strip().lower()
                f.append((h0,h1))
            else:
                pass
        return f
    else:
        return []
print(parse_signins(raw))


# E02（5分）group_topics：
def group_topic(records):
    a={}
    if records:
        for i in records:
            if i[0] not in a :
                a[i[0]]=set(a[i[1]])
            else:
                a[i[0]]= a[i[1]].add(i[1])
        return a
    else:
        return []
        

# E03（5分）rank_learners：
#太累了，下次补上吧

# E04（5分）learning_report与普通／空／不同门槛调用：
#太累了，下次补上吧

# F01（5分）五步Git命令，仅写在注释里：
# 1.git status
# 2.git add "amswer.py"
# 3.git 
# 4.git commit "完成综合练习"
# 5.git push

# 未完成题号、卡点与边界自查记录：

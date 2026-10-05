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

# commands = ["3", "0", "-2", "5", "stop", "100"]
# initial_stock = 2
# box_size = 4
# i=0
# sum1=initial_stock
# while i < len(commands):
#     a=commands[i]
#     i=i+1
#     if a=="stop":
#         break
#     else:
#         if int(a)>0:
#             sum1=sum1+int (a)
#         else:
#             continue
# #sum1
# box=sum1//box_size
# #box
# rest=sum1%box_size
# #rest
# print(f"总库存：{sum1}件")
# print(f"整箱：{box}件")
# print(f"剩余：{rest}件")


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
# sum1=0
# a=[]
# w=0
# j=0
# l=0
# y=0
# rows = [("小周", 58), ("小林", 90), ("小白", 60), ("小陈", 80), ("小许", 100)]
# h={}
# for i,p in rows:
#     h[i]=p
    
# for i in rows:
#     sum1=sum1+i[1]
#     #sum1
#     if i[1]>=60:
#         a.append(i[0])
#     else:
#         pass
# for i in h:
#     if h.get(i)<60:
#         w=w+1
#     elif h.get(i)>=60 and h.get(i)<80:
#         j=j+1
#     elif h.get(i)>=80 and h.get(i)<90:
#         l=l+1
#     elif h.get(i)>=90 and h.get(i)<=100:
#         y=y+1
# if a:
#     print(f"总分：{sum1}")
# else:
#     print("无")
# if a:
#     avg=sum1/len(rows)
#     print(f"平均分：{avg:.1f}")
# else:
#     print("无")
# if len(a)!=0:
#     print(f"及格名单：{"、".join(a)}")
# else:
#     print("无")
# print(f"优秀：{y}人")
# print(f"良好：{l}人")
# print(f"及格{j}人")
# print(f"待及格{w}人")
# print(0)

# ## E · 学习签到数据报告（20分）

# 每问5分。不同于订单累计，这次重复签到同一个主题**只算一个不同主题**，但原始有效记录条数仍逐条计算。

# ```python
# raw = " Ada ,Python;bo,SQL;ADA,python;;cy,Python; Bo ,Linux;ada,sql; \n"
# ```

# 分号分隔记录，逗号分隔姓名与主题。忽略纯空白片段；非空片段保证恰有一个逗号，姓名与主题去两端空白后非空，仅含英文字母，统一转小写。原始数据允许空字符串、重复记录、不同大小写。
# ### E01 · 解析签到（5分）

# 定义`parse_signins(raw)`，返回按输入顺序排列的`(姓名, 主题)`元组列表，保留重复记录。

# ```python
# # 本例结果
# [('ada', 'python'), ('bo', 'sql'), ('ada', 'python'),
#  ('cy', 'python'), ('bo', 'linux'), ('ada', 'sql')]
# # ''或' ; \n;;' -> []
# ```

raw = " Ada ,Python;bo,SQL;ADA,python;;cy,Python; Bo ,Linux;ada,sql; \n"
def parise_signins(raw):
    a=[]
    b=raw.split(";")
    for i in b:
        if i.strip():
            c=i.split(",")
            d=c[0].strip().lower()
            f=c[1].strip().lower()
            a.append((d,f))
    return a
print(parise_signins(raw))
result1=parise_signins(raw)


# ### E02 · 每人学过哪些主题（5分）

# 定义`group_topics(records)`，返回字典，键为姓名，值必须是保存不同主题的**集合**。本例对应ada拥有python、sql；bo拥有sql、linux；cy拥有python。集合显示顺序不限，空输入返回`{}`，不改原记录。


def group_topics(record):
    a={}
    for i in record:
        if i[0] in a:
            a[i[0]].add(i[1])
        else:
            a[i[0]]=set()
            a[i[0]].add(i[1])
    return a
records = [('ada', 'python'), ('bo', 'sql'), ('ada', 'python'),
           ('cy', 'python'), ('bo', 'linux'), ('ada', 'sql')]
print(group_topics(records))



# ### E03 · 按不同主题数排名（5分）

# 定义`rank_learners(grouped, min_topics=1)`，保留主题数>=门槛的人，返回`(姓名, 不同主题数)`元组列表。按主题数降序；同数量按姓名字母升序。使用lambda作为主题数排序key，可分两次排序。门槛为正整数，不修改grouped及其中集合。

# 默认返回`[('ada', 2), ('bo', 2), ('cy', 1)]`；门槛2返回前两项；门槛3或空字典返回`[]`。            
def rank_learners(grouped,min_topics=1):
    a=[]
    for i in grouped:
        if len(grouped[i])>=min_topics:
            a.append((i,len(grouped[i])))
        else:
            pass
    c=sorted(a,key=lambda a: a[0],reverse=True)
    c=sorted(a,key=lambda a: a[1],reverse=True)
    return c
grouped = {'cy': {'python'}, 'bo': {'sql', 'linux'}, 'ada': {'python', 'sql'}}
rank_learners(grouped)
# ### E04 · 组合成报告（5分）

# 定义`learning_report(raw, min_topics=1)`，依次调用E01、E02、E03；将实际min_topics传入排名函数。返回如下字典：

# ```python
# # learning_report(raw)
# {'record_count': 6, 'learner_count': 3,
#  'topic_names': ['linux', 'python', 'sql'],
#  'ranked': [('ada', 2), ('bo', 2), ('cy', 1)]}
# ```

# 四个键含义：record_count是**筛选前有效签到记录条数**；learner_count是门槛筛选后人数；topic_names是**筛选后这些人**学过的主题总集合转成的字母升序列表；ranked为E03返回值。

# 门槛2时record_count仍为6，人数为2，主题仍为上述3个。门槛3时record_count仍为6，人数0，主题列表及排名均为空。原始数据为空时四项分别为0、0、[]、[]。

# 检查连续调用不同门槛时结果互不影响。字典键顺序不限，列表顺序和集合/元组类型按题意核对。
def learning_report(raw,min_topics=1):
    h={}
    a=parise_signins(raw)
    h["record_count"]=len(a)
    b=group_topics(a)
    c=rank_learners(b,min_topics)
    p=set()
    h["learner_count"]=len(c)
    for i in c:
           p.update(b[i[0]])
    y=sorted(p) 
    h["topic_names"]=y
    h["ranked"]=c
    return h
print(learning_report(raw))

# ### D1.1 · 切片范围（5 分）

# 目标是从 `code` 中取出年份，输出 `2026`。下面的代码没有达到目标，请修复切片表达式，不能修改 `code` 的内容。

# ```python
# code = "CODE2026"
# print(code[3:7])
# ```
#1.1
#问题说明：下标问题，列表下标从0开始，且切片中包含前项不包含后项
#修正
code = "CODE2026"
print(code[4:])
#1.2
# 问题说明：sort不会返回分类的值，只会修改原数列，sorted返回值，不修改原数列
#修正
letters = ["c", "a", "b"]
li=sorted(letters)
print("".join(li))
#1.3
#问题说明：不能直接修改元组的值，因此直接用新元组代替
#修正
point=(3,8)
point=(6,point[1])
print(point)
# ## 五、大题二：成绩记录处理（D2，共 15 分）

# 每问 3 分。只使用本题给定的数据，完成下面五项要求。

# ```python
# rows = [("林晓", 72), ("周宁", 59), ("陈雨", 91), ("苏禾", 88), ("许安", 60)]
# ```

# 约定：名单非空，姓名不重复，分数为 `0`—`100` 的整数，最高分唯一。不要修改 `rows`，结果必须由代码计算得到。
### D2.1 · 逐条打印（3 分）

# 用循环拆出姓名和分数，按原顺序输出：
rows = [("林晓", 72), ("周宁", 59), ("陈雨", 91), ("苏禾", 88), ("许安", 60)]
for i,p in rows:
    print(f"{i}：{p}分")

### D2.2 · 总分与平均分（3 分）

# 计算总分、平均分；平均分保留一位小数。输出：
sum=0
for i,p in rows:
    sum=sum+p
print(f"""
总分：{sum}
平均分：{sum/len(rows):.1f}
""")
# ### D2.3 · 及格名单（3 分）

# 筛选分数**大于等于 60** 的学生，把姓名保存到列表 `passed_names`，顺序与原名单一致，再输出：

# ```text
# 及格名单：林晓、陈雨、苏禾、许安
# ```

# 如果更换数据后没有人及格，则输出 `及格名单：无`。
passed_names=[]
for i,p in rows:
    if p >=60:
        passed_names.append(i)
if passed_names:
    print("及格名单："+"、".join(passed_names))
else:
    print("及格名单：无")
# ### D2.4 · 最高分（3 分）

# 找出分数最高的学生，输出：

# ```text
# 最高分：陈雨 91分
# ```
mna,max=rows[0]
for i,p in rows:
    if p>max:
        max=p
        mna=i
    else:
        pass
print(f"最高分：{mna} {max}分")
# ### D2.5 · 分数分档（3 分）

# 按下面四个**互不重叠**的区间统计人数：

# - 优秀：`90`—`100`。
# - 良好：`80`—`89`。
# - 及格：`60`—`79`。
# - 待加强：`0`—`59`。

# 按上述顺序输出：

# ```text
# 优秀：1人
# 良好：1人
# 及格：2人
# 待加强：1人
# ```

# 注意：D2.3 的“及格名单”包含所有 `>= 60` 的人；D2.5 的“及格档”只包含 `60`—`79` 分，两个统计范围不同。

# ---
y=0
l=0
j=0
d=0
for i,p in rows:
    if p>=90 and p <=100:
        y=y+1
    elif p>=80 and p<90:
        l=l+1
    elif p>=60 and p<80:
        j=j+1
    else:
        d=d+1
print(f"""
优秀：{y}人
良好：{l}人
及格：{j}人
待加强：{d}人
""")
# ## 六、大题三：订单数量汇总（D3，共 20 分，综合拔高）

# 每问 4 分。本题把学过的几种容器连起来使用，可以拆成多步完成，不要求写成一行。

# ### 原始数据与规则

# ```python
# raw_orders = " Pen , 2 ; notebook,3;; PEN,4; eraser , 1; notebook ,3;   ;\n"
# ```

# 数据约定：

# - 分号 `;` 分隔记录，逗号 `,` 分隔商品名和数量。
# - 连续分号、只含空白的片段、末尾空白不算订单，必须忽略。
# - 有效记录中恰好有一个逗号；商品名非空，只含英文字母，允许大小写不同及字段两端空白。
# - 商品名统一为小写后再统计，`Pen` 和 `PEN` 是同一种商品。
# - 数量转换为整数；有效数量保证为正整数，不考非法数字和异常处理。
# - 至少有一条有效记录；同名商品可以出现多次，销量最高的商品可以并列。
# - 所有商品清单均按**统一小写后的商品名字母升序**输出；不直接依赖集合的显示顺序。

# ### D3.1 · 拆分记录并去掉空项（4 分）

# 把有效记录保存到列表 `clean_rows` 中：去掉每段记录两端空白，保留非空记录，顺序与输入一致。此时不用改记录内部的空格。

# 输出：

# ```text
# 有效记录：5条
raw_orders = " Pen , 2 ; notebook,3;; PEN,4; eraser , 1; notebook ,3;   ;\n"
raw_li=raw_orders.split(";")
raw_clean=[]
for i in raw_li:
    raw_d=i.strip()
    if raw_d:
        raw_clean.append(raw_d)
print(raw_clean)
# ### D3.2 · 整理成元组记录（4 分）

# 进一步清洗每条记录，创建列表 `records`，每个元素都是 `(小写商品名, 整数数量)`，顺序与有效记录一致。打印 `records`，结果应为：

# ```text
# [('pen', 2), ('notebook', 3), ('pen', 4), ('eraser', 1), ('notebook', 3)]
# ```
records=[]
for a in raw_clean:
    i,p=a.split(",")
    i=i.strip().lower()
    p=int(p.strip())
    records.append((i,p))
print(records)

# ### D3.3 · 按商品累计数量（4 分）

# 创建字典 `totals`，键是商品名，值是这种商品的累计数量。按商品名字母升序逐行输出：

# ```text
# eraser：1件
# notebook：6件
# pen：6件
# ```
total={}
for i,p in records:
    if i in total:
        total[i]=total[i]+p
    else :
        total[i]=p

for i in sorted(total):
    print(f"{i}:{total[i]}件")

# ### D3.4 · 商品去重与种类统计（4 分）

# 用集合 `product_names` 保存不重复的商品名，统计种类数，并按商品名字母升序输出清单：

# ```text
# 商品种类：3种
# 商品清单：eraser、notebook、pen
# ```
z=0
q=[]
for i in total:
        q.append(i)
z=len(q)
print(f"{z}")
h="、".join(q)
print(f"物品清单：{h}")

# ### D3.5 · 找出全部最高销量商品（4 分）

# 找出**累计数量**最多的商品。如果并列，要全部保留并按商品名字母升序输出：

# ```text
# 最高销量：6件
# 最高销量商品：notebook、pen
# ```

# 更换数据后，如果最高销量商品只有一个，也按照同样格式输出该商品名。

# ---
max=0
li=[]
for i  in sorted(total):
    p=total[i]
    if p>max:
        max=p
        li=[i]
    elif p==max:
        li.append(i)
    else:
        pass
print(f"最高销量：{max}件")
print("商品清单:"+",".join(sorted(li)))
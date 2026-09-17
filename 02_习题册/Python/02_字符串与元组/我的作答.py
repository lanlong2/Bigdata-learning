#A1
s="BigDsta2026"
print(s[0],s[-1])
print(s[0:2])
print(s[3:6])
print(s[-1:])
#A2 
#"PYTHON!"
#A3
line = "苹果,香蕉,橘子"
list=line.split(",")
ls="|".join(list)
print(list)
print(ls)
#4
raw = "   Zhang San ,  18  \n"
s=raw.strip()
print(s)
s1=s.split(',')
s11=s1[0].strip()
s12=s1[1].strip()
s2=[s11,s12]
print(s2)
s31=s2[0].replace(' ','')
s32=s2[1].replace(" ","")
s311=s31.lower()
s321=s32.lower()
s3=[s311,s321]
print(s3)
s4="|".join(s3)
print(s4)
#A5
text = "the quick brown fox jumps over the lazy dog"
text.count("the")
text.index("fox")
text.find("cat")
text.endswith("dog")
i=text.split(" ")
print(len(i))
#A6
rows = [("张三", 88), ("李四", 95), ("王五", 79)]
total=0
for name ,score in rows:
    print(f"{name:<8}{score:>6}")
    total=total+score
avg=total/len(rows)
print(f"{avg:.1f}")
#A7
word = "Mississippi"
word.count("s")
i=set(word)
sorted(i)
print(i)
w="".join(i)
print(w)
if word==word[::-1]:
    print("是回文")
else:
    print("不是回文")
#B1
#a 元组 3
#b int 1
#c 元组 1
#d 不知道
#e 元组 2
#f 字符 3
#g 字符 1

# ===== 新增空白区域（上面的已有作答保留原内容）=====
# A1～A7、B1：先核对原题数据及每个小问，再在原位置订正。

# A8 我的回答／代码：


# B2 我的回答／代码：


# B3 我的回答／代码：


# B4 我的回答／代码：


# B5 我的回答／代码：


# B6 我的回答／代码：


# 综合题1：只有题目数据与空白提示。
raw = "张三,88,92,79;李四,95,60,73;王五,45,100,68"

# 1) 拆成每个学生一条


# 2) records = [(姓名, 总分, 平均分), ...]


# 3) 按平均分排序 ranked


# 4) 打印排行榜


# 5) 有不及格科目的学生 + 挂科数


# 6) 姓名用"、"连接


# 7) 思考题（写在这里）：

# 综合题2：只有题目数据与空白提示。
text = "  Python is fun. python is powerful; PYTHON is everywhere!  "

# 1) 两个长度 + 说明


# 2) clean


# 3) words + 单词总数


# 4) uniq


# 5) pairs


# 6) ranked + 最高频元组


# 7) 词频表


# 8) 出现>=2次的单词用 | 连接


# 9) count / find / startswith

# 综合题3：只有题目数据与空白提示。
points = [(1, 2), (4, 0), (-3, 5), (0, 0), (2, -7)]

# 1) enumerate 打印


# 2) 最远的点


# 3) 按 y 排序


# 4) swapped


# 5) 第一象限


# 6) xs / ys / zip 还原 + 验证


# 7) xs2, ys2 = zip(*points)，type 是？和第6步差别：


# 8) 标签配对


# 9) 连成字符串


# 10) points[0][0] = 99 的结果是：
#     正确的修改做法：

# 综合题四：在注释里写预测，再单独验证并跳过报错行。
# 第1处结果／原因：
# 第2处结果／原因：
# 第3处结果／原因：
# 第4处结果／原因：
# 第5处结果／原因：
# 第6处结果／原因：
# 第7处结果／原因：
# 第8处结果／原因：
# 第9处结果／原因：
# 第10处结果／原因：
# 第11处结果／原因：
# 第12处结果／原因：
# 第13处结果／原因：
# 第14处结果／原因：
# 元组内部列表为什么能改：
# 哪些对象共享：
# 本例快照不变的适用条件：

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
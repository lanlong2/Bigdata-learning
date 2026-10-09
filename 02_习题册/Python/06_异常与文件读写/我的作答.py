# 异常与文件读写日常习题作答
# 题目、答案解析各为独立文件；这里只写自己的答案。
# 每题独立，但本册使用 __file__，应先保存再运行整个文件。
# 只检查某题时，先把其他题的代码注释掉，不使用“运行选定内容”。
# 空白模板无输出是正常的。
# import json
# from pathlib import Path
# import csv
# BASE = Path(__file__).resolve().parent
# OUTPUT = BASE / "练习数据"
# 写文件前自己调用 OUTPUT.mkdir(exist_ok=True)。

# I01 · 把坏输入变成可处理结果
# 我的思路／预测：
# def parse_integer(text):
#     try: 
#         return int(text)
#     except ValueError:
#         return None
# # print(parse_integer("2"))
# # print(parse_integer("0"))
# # print(parse_integer("-3"))
# # print(parse_integer("2.5"))



# # I02 · 转换成功还要检查条件
# # 我的思路／预测：
# def positive_quantity(text):
#     try:
#         if int(text)>0:
#             return int(text)
#         else:
#             return None
#     except ValueError:
#         return None
# # print(positive_quantity("2"))
# # print(positive_quantity("0"))
# # print(positive_quantity("-3"))
# # print(positive_quantity("2.5"))



# # I03 · 读取文本并过滤空行
# # 我的思路／预测：
# OUTPUT.mkdir(exist_ok=True)
# output_file=OUTPUT/"names.txt"

# names=[]
# with open(output_file,"r",encoding="utf-8") as file:
#     for row in file:
#         a=row.strip("\n\r")
#         b=a.strip().lower()
#         if b:
#             names.append(b)
# # print(names)





# # # I04 · JSON写入后再读回
# # # 我的思路／预测：
# # input_dir=BASE/"我的输出"
# # input_file=input_dir/"record.json"
# # records={"姓名":"小林","分数":[80,90]}

# # with open(input_file,"w",encoding="utf-8") as file:
# #     json.dump(records,file,indent=2)

# # with open(input_file,"r",encoding="utf-8") as file:
# #     resolved=json.load(file)

# # print(records==resolved)

# # I05 · 读取CSV并处理非法数量
# # 我的思路／预测：
# from pathlib import Path
# import json 
# import csv
# base= Path(__file__).resolve().parent
# input_dir=base/"练习数据"
# input_dir.mkdir(exist_ok=True)
# input_file=input_dir/"orders.csv"
# #clean_h函数来得到一条row（脏数据）的判断，如果判断正确，得到一条列表包含字典的干净数据
# def clean_h(row:dict) -> tuple[dict|None , str] :
#     if None in row:
#         return None,"字段超过表头"
#     a=row.get("product")
#     b=row.get("quantity")
#     #a代表获得的row的product键的内容,同理b获得quantity
#     if a is None or b is None:
#             return None,"无内容"
#     a1=a.strip().lower()
#     b1=b.strip()
#     if not a1:
#         return None,"商品为空"
#     try:
#         b2=int(b1)
#     except ValueError:
#         return None,"非整数内容"
#     if b2 <= 0:
#         return None,"必须为正整数"
#     return {"product": a1,"quantity":b2},""
# clean_g=[]
# z_count=0
# z_reason=[]
# r_count=0
# with open(input_file,"r",encoding="utf-8") as file:
#     rows_d=csv.DictReader(file)
#     rows=list(rows_d)
#     for row in rows:
#         a,b=clean_h(row)
#         if a==None:
#             z_count=z_count+1
#             z_reason.append(b)
#         else:
#             clean_g.append(a)
#             r_count=r_count+1
    
# print(z_count)
# print(r_count)






# I06 · 写CSV并检查结果
# 我的思路／预测：
import csv
from pathlib import Path

base=Path(__file__).resolve().parent
output_dir=base/"我的输出"
output_dir.mkdir(exist_ok=True)
output_file=output_dir/"clean.csv"
clean=[{"product":"pen","quantity":2},{"product":"book","quantity":3}]

def clean_w(rows,path):
    with open(path,"w",encoding="utf-8",newline="") as file :
        writer= csv.DictWriter(file,fieldnames=["product","quantity"])
        writer.writeheader()
        writer.writerows(rows)

def clean_r(path) :
    with open(path,"r",encoding="utf-8",newline="") as file:
        return list(csv.DictReader(file))

clean_w(clean,output_file)
clean_yr=clean_r(output_file)
print(clean_yr)
print(len(clean_yr))
sum=0
for row in clean_yr:
    sum=sum+int(row.get("quantity"))
print(sum)
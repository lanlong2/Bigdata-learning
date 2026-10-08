# 异常与文件读写日常习题作答
# 题目、答案解析各为独立文件；这里只写自己的答案。
# 每题独立，但本册使用 __file__，应先保存再运行整个文件。
# 只检查某题时，先把其他题的代码注释掉，不使用“运行选定内容”。
# 空白模板无输出是正常的。
import json
from pathlib import Path
import csv
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "练习数据"
# 写文件前自己调用 OUTPUT.mkdir(exist_ok=True)。

# I01 · 把坏输入变成可处理结果
# 我的思路／预测：
def parse_integer(text):
    try: 
        return int(text)
    except ValueError:
        return None
# print(parse_integer("2"))
# print(parse_integer("0"))
# print(parse_integer("-3"))
# print(parse_integer("2.5"))



# I02 · 转换成功还要检查条件
# 我的思路／预测：
def positive_quantity(text):
    try:
        if int(text)>0:
            return int(text)
        else:
            return None
    except ValueError:
        return None
# print(positive_quantity("2"))
# print(positive_quantity("0"))
# print(positive_quantity("-3"))
# print(positive_quantity("2.5"))



# I03 · 读取文本并过滤空行
# 我的思路／预测：
OUTPUT.mkdir(exist_ok=True)
output_file=OUTPUT/"names.txt"

names=[]
with open(output_file,"r",encoding="utf-8") as file:
    for row in file:
        a=row.strip("\n\r")
        b=a.strip().lower()
        if b:
            names.append(b)
# print(names)





# I04 · JSON写入后再读回
# 我的思路／预测：
input_dir=BASE/"我的输出"
input_file=input_dir/"record.json"
records={"姓名":"小林","分数":[80,90]}

with open(input_file,"w",encoding="utf-8") as file:
    json.dump(records,file,indent=2)

with open(input_file,"r",encoding="utf-8") as file:
    resolved=json.load(file)

# print(records==resolved)

# I05 · 读取CSV并处理非法数量
# 我的思路／预测：






# I06 · 写CSV并检查结果
# 我的思路／预测：
def save_clean(rows: list[dict],path: Path) -> None:
    with open(path,"w",encoding="utf-8",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["product","quantity"])
        writer.writeheader()
        writer.writerows(rows)

def read_clean(path:Path) -> list[dict]:
    with open(path,"r",encoding="utf-8",newline="") as file:
        return list(csv.DictReader(file))

output_dir= BASE/"我的输出"
output_dir.mkdir(exist_ok=True)
output_file= output_dir/"clean.csv"

clean=[{"product":"pen","quantity":2},
       {"product":"book","quantity":3}
       ]
clean_w1=save_clean(clean,output_file)
clean_w2=read_clean(output_file)

print(len(clean_w2),sum(int(row["quantity"]) for row in clean_w2))
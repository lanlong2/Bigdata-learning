# import json
# from pathlib import Path

# base=Path(__file__).resolve().parent
# output_dir=base/"我的输出"
# output_dir.mkdir(exist_ok=True)
# output_file=output_dir/"record.json"
# records={"姓名": "小林","分数":[80,90]}
# with open(output_file,"w",encoding="utf-8") as file:
#     json.dump(records,file,ensure_ascii=False,indent=2)
# with open(output_file,"r",encoding="utf-8") as file:
#     restored=json.load(file)
# print(restored==records)
# print(sum(restored["分数"]))

# import json
# from pathlib import Path

# base=Path(__file__).resolve().parent
# output_dir=base/"我的输出"
# output_dir.mkdir(exist_ok=True)
# output_file=output_dir/"record.json"
# records={"有效数量":0,"商品":[]}
# with open(output_file,"w",encoding="utf-8") as file:
#     json.dump(records,file,ensure_ascii=False,indent=2)

# with open(output_file,"r",encoding="utf-8") as file:
#     restore=json.load(file)

# print(restore == records)

# print(restore["有效数量"],len(restore["商品"]))
import csv
from pathlib import Path

base=Path(__file__).resolve().parent
input_file=base/"练习数据"/"orders.csv"

with open(input_file,"r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        print(row)
        print(type(row["quantity"]).__name__)
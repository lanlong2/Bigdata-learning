# 学习起步模板：尚未实现清洗逻辑。
# 先读上一级文件夹的“任务书.md”，不要把验收数字直接写成答案。
import csv
from pathlib import Path
base=Path(__file__).resolve().parent.parent
input_dir=base/"data"
input_file=input_dir/"示例订单.csv"
import json

# TODO 1：读取 INPUT_FILE。
with open(input_file,"r",encoding="utf-8",newline="") as file:
    c_r= csv.DictReader(file)
    if c_r.fieldnames !=["order_id","product","quantity","unit_price"] :
        raise ValueError("表头不对")
    d_rows=list(c_r)#把脏数据按条放到d_rows
    #判断表头对不对
    #c_r代表读取的待清理数据
# TODO 2：校验字段，记录无效行及原因。

error_r=[]
error_c=0
r_c=0
r_clean_1=[]#正确数据

def judge_c(row:dict) -> tuple[dict|None,str]:
     #此函数用于对写入的单条数据进行判断成功则写入clean_1
    if None in row:
        return None,"字段超过表头"
    a=row.get("order_id")
    b=row.get("product")
    c=row.get("quantity")
    d=row.get("unit_price")
    if a is None or b is None or c is None or d is None :
        return None,"缺少字段"
    a1=a.strip()
    b1=b.strip().lower()
    c1=c.strip()
    d1=d.strip()
    if not a1 or not b1 or not c1 or not d1:
        return None,"字段为空"
    try:
        c2=int(c1)
        d2=int(d1)
    except ValueError:
        return None,"商品数量,单价应为整数"
    if c2 <=0 or d2 <0:
        return None ,"数量，单价应大于0"
    return {"order_id":a1,"product":b1,"quantity":c2,"unit_price":d2},""
for row in d_rows:
    a,b=judge_c(row)
    if a is None:
        error_c += 1
        error_r.append({"row":row,"reason":b})
    else:
        r_clean_1.append(a)
print(r_clean_1)

# TODO 3：按订单编号去重。
r_clean_2=[]
r_clean_id=[]
repeat_c=0
for row in r_clean_1:
    if row.get("order_id") in r_clean_id:
        repeat_c +=1
    else:
        r_clean_2.append(row)
        r_clean_id.append(row.get("order_id"))
print(r_clean_2)


# TODO 4：汇总数量、销售额和商品销量。
sum=0
sum_c=0
p_c=0#产品汇总数量
for row in r_clean_2:
    sum_c += row.get("quantity")
    sum += row.get("quantity")*row.get("unit_price")
p_c=len(r_clean_2)
print(sum,sum_c,p_c)
# TODO 5：创建 RESULT_DIR，保存 CSV 和 JSON。
result_dir=base/"我的输出"
result_dir.mkdir(exist_ok=True)
result_file1=result_dir/"result.csv"
result_file2=result_dir/"result.json"
with open(result_file1,"w",encoding="utf-8",newline="") as file:
    write=csv.DictWriter(file,fieldnames=["order_id","product","quantity","unit_price"])
    write.writeheader()
    write.writerows(r_clean_2)
pen_s=0
notebook_s=0
eraser_s=0
for row in r_clean_2:
    if row.get("product")=="pen":
        pen_s += row.get("quantity")
    elif row.get("product")=="notebook":
        notebook_s += row.get("quantity")
    elif row.get("product")=="eraser":
        eraser_s += row.get("quantity")
j_s={}
j_s["有效订单"]=p_c
j_s["重复行"]=repeat_c
j_s["无效行"]=error_c
j_s["商品总数量"]=sum_c
j_s["销售额"]=sum
j_s["pen销量"]=pen_s
j_s["notebook销量"]=notebook_s
j_s["eraser销量"]=eraser_s

with open(result_file2,"w",encoding="utf-8") as file:
    json.dump(j_s,file,ensure_ascii=False,indent=2)

# TODO 6：用任务书里的边界情况检验程序。
#边界情况由ai验证
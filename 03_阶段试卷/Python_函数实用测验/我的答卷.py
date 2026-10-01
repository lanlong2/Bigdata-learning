# Python函数实用测验，100分，建议120分钟。
# 题目见同目录试卷.md；整卷完成后再看参考答案。
# 姓名：lanlong
# 日期：10.1
# 开始／结束时间：
# 实际用时（扣除休息）：
# 独立／提示／看解析及涉及题号：
# 空白模板运行没有输出属正常。各题独立，D题内部共享函数。

# A01（5分）三行输出与说明：
#7，4，6
#说明：result取的是函数结果，导入的两个值quantity，bonus分别为4，3
#外部参数quantity的值始终没变
#add_bonus（quantity）传入4，bonus没变
# A02（5分）三行输出与应返回的值：
#"alice smith",None,True
#指出：return clean

# B01（10分）问题说明、stock_label修复与调用：
#说明：没有返回值，只是单纯的打印，quantity应该是文本型
def stock_label(name,quantity) :
    text=name+":"+str(quantity)
    return text
label=stock_label("pen",3)
print(label)
print(stock_label("bag",0))

# B02（10分）问题说明、rank_items修复与调用：
#说明：sort只会出值但是不返回，应用sorted，同时没有考虑传入空值
def rank_items(rows):
    if rows:
        a= sorted(rows,key=lambda rows :rows[1],reverse=True)
        return a
    else:
        return []
rows=[("pen",2),("book",5),("bag",2)]
ranked=rank_items(rows)
print(rows)
print(ranked)


# C01（10分）clean_names与调用：
names = [" Alice Smith ", " \t", "BOB", " alice smith\n"]
def clean_names(names):
    c=[]
    for i in names:
        a=i.lower().strip()
        if i:
            c.append(a)
        else:
            pass
    return c
print(clean_names(names))
# C02（10分）received_total与调用，含列表拆包：
def recived_total(*quantity):
    if quantity:
        sum=0
        for i in quantity:
            if type(i)==list:
                for a in i:
                    sum=sum+a
            else:
                sum=sum+i
        return sum
    else:
        return 0
batches=[2,4,1]
print(recived_total(3,0,5))
print(recived_total(batches))    
# C03（10分）order_label与调用：
# def order_label(**field:product="未命名"):


# C04（10分）map_values、两个处理函数与调用：
def add_one(value):
    a=[]
    for i in value:
        i=i+1
        a.append(i)
    return a
def map_values(values,operation):
    if values:
        return operation(values)        
    else:
        return []
print(map_values([0,2,5],add_one))
# D题初始数据：
raw = " Pen ,2;book,0;;PEN,3; bag ,5;book,2; \n"

# D01（6分）parse_orders：
#不会处理空白数据，本大题基本搁置

# D02（6分）select_orders：


# D03（8分）sum_by_product：


# D04（10分）build_report：


# D题调用与边界自查（普通、空输入、门槛3/0/过高、并列销量）：


# 未完成题号／卡点：

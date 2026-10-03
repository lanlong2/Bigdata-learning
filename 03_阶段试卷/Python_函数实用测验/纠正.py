# ### C01 · 清洗收货人名单（10分）

# 定义`clean_names(names)`。输入字符串列表，去每个名字两端空白、转小写，丢弃清洗后为空的名字；保留名字内部空格、重复项和原先顺序。返回新列表，不修改输入。

# ```python
# names = [" Alice Smith ", " \t", "BOB", " alice smith\n"]
# # 返回 ['alice smith', 'bob', 'alice smith']
# # [] 返回 []；['  '] 返回 []
# ```
names = [" Alice Smith ", " \t", "BOB", " alice smith\n"]
def clean_names(names):
    b=[]
    for i in names:
            a=i.strip().lower()
            if a:
                  b.append(a)
            else:
                  pass
    return b        
#print(clean_names(names))


### C02 · 合并多批到货数量（10分）

# 定义`received_total(*quantities)`，返回所有传入数量的总和；数
# 量均为非负整数，没有参数返回0。必须使用不定长位置参数。

# 除`received_total(3, 0, 5)`得到8外，还要
# 把`batches = [2, 4, 1]`通过拆包传入同一个函数，得到7；不能针对列表
# 重新写一个求和函数。
batches = [2, 4, 1]
def recived_total(*quantities):
    a=0
    for i in quantities:
            a=a+i
            
    return a
#print(recived_total(3,0,5))
#print(recived_total(*batches))

### C03 · 生成订单摘要标签（10分）

# 定义`order_label(**fields)`，字段值均为字符串。取`product`、`city`，缺少时分别
# 用`"未命名"`、`"未知"`，返回`"商品@城市"`。忽略其他字段，不需要清洗字段值；已传入
# 的空字符串保留，不当成缺失。必须使用不定长关键字参数。

# ```python
# # order_label(product='pen', city='杭州', note='加急') -> 'pen@杭州'
# # order_label(product='book') -> 'book@未知'
# # order_label() -> '未命名@未知'
# # order_label(product='', city='杭州') -> '@杭州'
# ```
def order_label(**fields):
    product=fields.get("product","未命名")
    city=fields.get("city","未知")
    return product +"@"+ city

order_label(product='pen', city='杭州', note='加急')
order_label(product='book')
order_label()
order_label(product='', city='杭州')

# ### C04 · 批量应用处理规则（10分）

# 定义`map_values(values, operation)`，依次对每个元素调用传入函数，返回新列表，不修改输入列表。再定义`add_one(value)`返回原数字加1，将这个函数传入处理`[0, 2, 5]`，得到`[1, 3, 6]`。换成另一个“乘2”函数后应得到`[0, 4, 10]`；空列表返回`[]`。

# 约定：operation接收一个元素并返回处理结果，不修改该元素；本题无须处理复杂对象复制。
def add_one(value):
      value =value+1
      return value
def double_value(value):
     value =value *2
     return value
def map_values(values,operation):
    b=[]
    if values:
        for i in values:
            a=operation(i)
            b.append(a)
        return b
    else:
         return []
#print(map_values([0,2,5],add_one))
#print(map_values([0,2,5],double_value))

# ```python
# raw = " Pen ,2;book,0;;PEN,3; bag ,5;book,2; \n"
# ```

# 规则：`;`分记录，`,`分商品名与数量；忽略空白片段。非空记录保证恰有一个逗号，商品名非空、只含英文字母及两端空白，数量能转为非负整数。商品名去两端空白并转小写；数量转int。允许重复商品、0数量、空字符串或全空片段；不考坏数字或文件读取。

# ### D01 · 解析订单（6分）

# 定义`parse_orders(raw)`，返回`(小写商品名, 整数数量)`元组组成的列表，保留记录顺序和0数量。

# 本例返回：

# ```python
# [('pen', 2), ('book', 0), ('pen', 3), ('bag', 5), ('book', 2)]
# ```
raw = " Pen ,2;book,0;;PEN,3; bag ,5;book,2; \n"
def parse_order(raw):
    b=[]
    c=raw.split(";")
    for i in c:
        if i.strip():
            a=i.split(",")
            e=a[0].lower().strip()
            h=int(a[1])
            b.append((e,h))
        else:
             pass
    return b
#print(parse_order(raw))

# ### D02 · 按单条数量筛选（6分）

# 定义`select_orders(records, min_quantity=1)`，返回数量大于等于门槛的记录组成的新列表，不修改原列表。门槛为非负整数，必须使用实际传入值。保持原顺序。

# 对D01样例，默认返回`[('pen', 2), ('pen', 3), ('bag', 5), ('book', 2)]`；`min_quantity=3`返回`[('pen', 3), ('bag', 5)]`；门槛0保留全部；空输入返回`[]`。
records=[('pen', 2), ('book', 0), ('pen', 3), ('bag', 5), ('book', 2)]
def select_orders(records,min_quantity=1):
    a=[]
    for i in records:
         if i[1]>=min_quantity:
            a.append(i)
         else:
              pass
    return a
#print(select_orders(records))
#print(select_orders(records,3))
# ### D03 · 按商品累计（8分）

# 定义`sum_by_product(records)`，返回`{商品名: 累计数量}`字典，不修改输入；同名累加，0数量也保留商品键，空输入返回`{}`。这里不做门槛筛选。

# 对D02默认筛选后的列表，得到`{'pen': 5, 'bag': 5, 'book': 2}`。字典显示顺序不评分。
records=[('pen', 2), ('book', 0), ('pen', 3), ('bag', 5), ('book', 2)]
def sum_by_product(records):
     if records:
        a={}
        for i in records:
           if i[0] in a:
               a[i[0]]=i[1]+a[i[0]]
           else:
               a[i[0]]=i[1]
        return a  
     else:
          return {}
# print(sum_by_product(records))               
               

# ### D04 · 组合成可复用报告（10分）

# 定义`build_report(raw, min_quantity=1)`，必须依次调用D01、D02、D03三个函数，返回字典，包含以下四个键：

# - `record_count`：筛选后的记录条数，重复商品分条计数。
# - `quantity_sum`：筛选后的数量总和。
# - `product_count`：筛选后的不同商品数。
# - `ranked`：累计结果转为`(商品名, 累计数量)`元组列表，按累计数量降序；同销量按商品名字母升序。使用lambda作为销量排序key，可分两次稳定排序。
def build_report(raw,min_quantity=1):
    a1={}
    a=parse_order(raw)
    b=select_orders(a)
    a1["record_count"]=len(b)
    c=sum_by_product(b)
    print(a1.get("record_count"))
    sum1=0
    for i in c:
        sum1=sum1+c.get(i)
    a1["quantity_sum"]=sum1
    print(sum1)
    a1["product_count"]=len(c)
    ra0=[]
    for i in c:
         ra0.append((i,c.get(i)))
    print(ra0)
    a1["rank"]=ra0
    return a1
print(build_report(raw))
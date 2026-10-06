# M03：在这里定义clean_name(name)，去两端空白并转小写。
def clean_name(name):
    return name.strip().lower()
# M04：再添加入口保护下的演示代码。
# 初始模板不含解题代码。
if __name__=="__main__":
    print(clean_name(" Alice "))

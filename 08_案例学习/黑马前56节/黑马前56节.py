
#用来可以让程序持续执行的while循环
scsc={}
while True:

    print("""
    ##############################################################################

    # 1. 添加学生信息 2. 修改学生信息 3. 删除学生信息 4. 查询学生信息 5.列出学生信息

    ##############################################################################
    """)
    #scsc表示学生表格，scsn表示学生姓名，scsyc表示学生语文成绩，scssc表示学生数学成绩
    choice=input("请选择需要执行的操作（1-7）:")
    match choice:
        case "1":
            scsn=input("请输入学生姓名:")
            if scsn in scsc:
                print("学生已存在")
            else:
                scsyc=int(input("请输入学生语文成绩："))
                scssc=int(input("请输入学生数学成绩"))
                scsyyc=int(input("请输入学生英语成绩："))

                scsc[scsn]={"语文成绩":scsyc,"数学成绩":scssc,"英语成绩":scsyyc}
                print(f"【{scsn}】添加成功")
        case "2":
            scsn=input("请输入学生姓名:")
            if scsn in scsc:
                scsyc=int(input("请输入学生语文成绩："))
                scssc=int(input("请输入学生数学成绩"))
                scsyyc=int(input("请输入学生英语成绩："))
                scsc[scsn]={"语文成绩":scsyc,"数学成绩":scssc,"英语成绩":scsyyc}
            else:
                print("学生不存在")
        case "3":
            scsn=input("请输入学生姓名:")
            if scsn in scsc:
                del scsc[scsn]
            else:
                print("学生不存在")
        case "4":
            scsn=input("请输入学生姓名:")
            if scsn in scsc:
                print(f"{scsc.get(scsn)}")
            else:
                print("学生不存在")
        case "5":
            print(f"{scsc.keys()}")
        case "6":
            for name, scores in scsc.items():
                print(f"姓名：{name}，成绩：{scores}")
        case "7":
             break
        case _:
            print("非法操作，不支持")

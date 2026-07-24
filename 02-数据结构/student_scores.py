students={}
def add_student():
    name=input("please enter your name:")
    score=input("please enter your score:")
    students[name]=score
    print("打印成功")
def query_student():
    findname=input("please enter your name")
    if findname in students:
        print("{}的成绩是{}分".format(findname,students[findname]))
    else:
        print("the students is not exist")
def delete_student():
    name=input("please enter who you want to delete:")
    if name in students:
        del students[name]
        print("delete successfully")
    else:
        print("the students is not exist")
def main():
    while True:
        print("\n--- 学生成绩管理系统 ---")
        print("1. 添加学生")
        print("2. 查询学生")
        print("3. 删除学生")
        print("4. 退出")
        choice = input("请选择（1-4）：")

        if choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("系统已退出")
            break
        else:
            print("输入无效，请重新选择")


# 运行主程序
main()
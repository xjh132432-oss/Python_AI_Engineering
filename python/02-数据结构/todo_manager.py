task={}
def add_task():
    name=input("please enter your task:")
    state=input("please enter the task state:")
    task[name]=state
def show_task():
    if not task:
        print("暂无任务")
        return
    for i, name in enumerate(task, start=1):
        print(f"{i}. {name} - {task[name]}")
def delete_task():
    name=input("please enter what do you want to delete:")
    if name in task:
        del task[name]
        print("delete successfully")
    else:
        print("the task does not exist")
def done_task():
    name=input("please enter the task:")
    if name in task:
        if task[name]=="done":
            print("task has been done")
        else:
            task[name]="done"
    else:
        print("task does not exist")
def main():
    while True:
        print("\n--- 待办事项管理器 ---")
        print("1. 添加任务")
        print("2. 查看所有任务")
        print("3. 删除任务")
        print("4. 完成任务")
        print("5. 退出")
        choice = input("请选择（1-5）：")
        if choice=="1":
            add_task()
        elif choice=="2":
            show_task()
        elif choice=="3":
            delete_task()
        elif choice=="4":
            done_task()
        elif choice=="5":
            break
main()
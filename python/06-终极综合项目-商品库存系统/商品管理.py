import json
import time
def log_action(level, message):
    timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
    with open("log.app", "a+", encoding="utf-8")as f:
        f.write(f"{timestamp}\t{level}\t{message}\n")

# ---- 数据加载与保存 ----
def load_data():
    # 加载 inventory.json，不存在返回空字典
    try:
        with open("inventory.json", "r", encoding="utf-8")as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_data(data):
    # 保存到 inventory.json
    with open("inventory.json", "w", encoding="utf-8")as f:
        json.dump(data,f,ensure_ascii=False)
# ---- 功能函数 ----
def add_item(inventory):
    # 输入编号，检查是否已存在
    ID = input("请输入要添加的编号").strip()
    if ID in inventory:
        print("该编号已存在")
        log_action("WARNING","添加的编号重复")
        return
    code={}
    name=input("请输入物品名称").strip()
    code["name"]=name
    price=input("请输入物品价格").strip()
    code["price"]=price
    num = input("请输入物品数量").strip()
    code["num"]=num
    inventory[ID]=code
    # 保存 + 日志
    save_data(inventory)
    log_action("INFO",f"{ID} {name} {price} {num} ")
def query_item(inventory):
    key = input("请输入你要查找的物品名称关键字").strip()
    found = False
    for ID, info in inventory.items():
        if key in info["name"]:
            print(f"{ID} | {info['name']} | {info['price']} | {info['num']}")
            found = True
    if not found:
        print("查无此物")
        log_action("WARNING", f"查询失败，关键字：{key}")
    else:
        log_action("INFO", f"查询成功，关键字：{key}")

    # 完全匹配和模糊匹配都支持

def update_item(inventory):
    # 输入编号，查找是否存在
    code=input("请输入编号").strip()
    if code not in inventory:
        print("无此编号")
        log_action("WARNING","查无此编号")
    else:
        while True:
            print("1.修改价格")
            print("2.修改数量")
            print("3.退出")
            choice=input("请输入要执行的操作代码").strip()
            if choice=="1":
                print(inventory[code])
                ori_price=inventory[code]["price"]
                price=input("请输入你要修改的价格")
                inventory[code]["price"]=price
                log_action("INFO",f"修改{code}的{ori_price}为{price}")
            elif choice=="2":
                print(inventory[code])
                ori_num = inventory[code]["num"]
                num = input("请输入你要修改的数量")
                inventory[code]["num"] = num
                log_action("INFO", f"修改{code}的{ori_num}为{num}")
            elif choice=="3":
                log_action("INFO","退出修改程序")
                break
    save_data(inventory)
    # 选择修改价格或数量
    # 保存 + 日志

def delete_item(inventory):
    # 输入编号，删除‘
        code=input("请输入编号").strip()
        if code in inventory:
            del inventory[code]
            print("删除成功")
            save_data(inventory)
            log_action("INFO",f"删除编号{code}成功")
        if code not in inventory:
            print("该编号不存在")
            log_action("WARNING", f"删除失败，编号{code}不存在")
        # 保存 + 日志
def show_all(inventory):
    if not inventory:
        print("无信息")
        log_action("WARNING", "无信息无法打印")
        return
    print("编号\t名称\t价格\t数量")
    for ID, info in inventory.items():   # 同时获取编号和详细信息
        print(f"{ID}\t{info["name"]}\t{info["price"]}\t{info["num"]}")
    log_action("INFO", "打印表格成功")
def show_stats(inventory):
    # 打印总种类数 + 总价值
    total_value=0
    for code in inventory:
        price = float(inventory[code]["price"])
        num = int(inventory[code]["num"])
        value = price * num
        total_value=value+total_value
    print(f"共{len(inventory)}种商品价值{total_value}元")
    log_action("INFO",f"打印 共{len(inventory)}种商品价值{total_value}元")
# ---- 主菜单 ----
def main():
    inventory = load_data()
    log_action("INFO", f"程序启动，当前库存 {len(inventory)} 种商品")
    while True:
        # 打印菜单
        print("1.添加商品")
        print("2.搜索商品")
        print("3.修改商品")
        print("4.删除商品")
        print("5.查看商品")
        print("6.商品总值")
        print("7.退出")
        # 处理用户选择
        choice=input("请输入需求代码").strip()
        if choice=="1":
            add_item(inventory)
        elif choice=="2":
            query_item(inventory)
        elif choice=="3":
            update_item(inventory)
        elif choice=="4":
            delete_item(inventory)
        elif choice=="5":
            show_all(inventory)
        elif choice=="6":
            show_stats(inventory)
        elif choice=="7":
            break

    log_action("INFO", "程序正常退出")

if __name__ == "__main__":
    main()
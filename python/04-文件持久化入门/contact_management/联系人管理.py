import time
import json
import os
def log_action(level,message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a+", encoding="utf-8")as f:
        f.write(f"{timestamp}\t{level}\t{message}\n")
def load_contacts():
    try:
        with open("contacts.json", "r")as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts
def add_contacts(contacts):
    ls = {}
    name = input("请输入联系人姓名").strip()
    if name in contacts:
        print("该联系人已存在")
        log_action("warniing",f"添加联系人{name}已存在")
        return
    phone = input("请输入联系人电话").strip()
    group = input("请输入联系人关系").strip()
    ls["phone"] = phone
    ls["group"] = group
    contacts[name] = ls
    log_action("info",f"添加联系人{name}成功")
    save_contacts(contacts)
def save_contacts(contacts):
    with open("contacts.json", "w")as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
def query_contact(contacts):
    name = input("姓名：").strip()
    if name in contacts:
        print(contacts[name])
        log_action("info",f"查询成功{name}")
    else:
        print("姓名不存在")
        log_action("warning",f"姓名{name}不存在")
def delete_contact(contacts):
    name = input("姓名：").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        log_action("info",f"删除成功{name}")
        print("删除成功")
    else:
        print("姓名不存在")
        log_action("warning",f"姓名不存在{name}")
def show_all(contacts):
    groups={}
    if not contacts:
        print("无联系人")
        log_action("warning",f"无联系人")
        return
    for name, info in contacts.items():
        group = info.get("group", "未分组")
        if group not in groups:
            groups[group] = []
        groups[group].append(name)
    for group in sorted(groups.keys()):
        print(f"\n【{group}】组：")
        for name in sorted(groups[group]):
            info = contacts[name]
            print(f"  {name} -> 电话：{info['phone']}")
    log_action("info",f"展示成功")
def main():
    contacts = load_contacts()
    log_action("info","加载成功")
    while True:
        print("\n--- 通讯录管理系统 ---")
        print("1. 添加联系人")
        print("2. 查询联系人")
        print("3. 删除联系人")
        print("4. 显示所有联系人（分组）")
        print("5. 退出")
        choice = input("请选择：")
        if choice == "1":
            add_contacts(contacts)
        elif choice == "2":
            query_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            show_all(contacts)
        elif choice == "5":
            log_action("info","退出成功")
            break
if __name__ == "__main__":
    main()
from tkinter import *
from tkinter.ttk import Notebook
from tkinter import messagebox
import tkinter as tk
import csv
import pandas as pd

def main():
    # 基础参数
    root = Tk()
    root.title("密码本")
    root.geometry("420x260")
    root.resizable(0,0)


    # 创建选项卡
    notebook = Notebook(root)


    # 写入
    page1 = Frame(notebook)
    Label(page1, text="请在下方输入要录入的信息").grid(row=1, column=3, pady=10)

    Label(page1, text="项目:").grid(row=2, column=2, pady=10)
    program = StringVar()
    program_entry = Entry(page1, textvariable=program)
    program_entry.grid(row=2, column=3, pady=10, ipadx=70)

    Label(page1, text="用户:").grid(row=3, column=2, pady=10)
    username = StringVar()
    username_entry = Entry(page1, textvariable=username)
    username_entry.grid(row=3, column=3, pady=10, ipadx=70)

    Label(page1, text="密码:").grid(row=4, column=2, pady=10)
    password = StringVar()
    password_entry = Entry(page1, textvariable=password)
    password_entry.grid(row=4, column=3, pady=10, ipadx=70)

    def write():
        with open('./password.csv', 'a', encoding="utf-8") as f:
            f.write(f'{program.get()},{username.get()},{password.get()}\n')
            f.close()
        program_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        messagebox.showinfo(title="提示", message="写入成功")
    Button(page1, text="录入", command=write).grid(row=5, column=1, padx=10, pady=40)
    Button(page1, text="退出", command=root.quit).grid(row=5, column=4, pady=40)


    # 查询
    page2 = Frame(notebook)
    Label(page2, text="请输入要查询的项目名称").grid(row=1, column=3, pady=15)

    Label(page2, text="项目名称:").grid(row=2, column=2, pady=10)
    name = StringVar()
    name_entry = Entry(page2, textvariable=name)
    name_entry.grid(row=2, column=3, ipadx=70)

    Label(page2, text="用户名:").grid(row=3, column=2, pady=10)
    search_username_entry = Entry(page2)
    search_username_entry.grid(row=3, column=3, ipadx=70)

    Label(page2, text="密码:").grid(row=4, column=2, pady=10)
    search_password_entry = Entry(page2)
    search_password_entry.grid(row=4, column=3, ipadx=70)

    def search():
        with open("password.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            for row in rows:
                if name.get() == row[0]:
                    search_username = row[1]
                    search_password = row[2]
                    search_username_entry.delete(0, tk.END)
                    search_password_entry.delete(0, tk.END)
                    search_username_entry.insert(0, search_username)
                    search_password_entry.insert(0, search_password)
                    result = True
                    break
                else:
                    search_username_entry.delete(0, tk.END)
                    search_password_entry.delete(0, tk.END)
                    result = False
                    continue
            if result == True:
                Label(page2, text="查询成功!").grid(row=5, column=3)
            elif result == False:
                Label(page2, text="未找到对应信息!").grid(row=5, column=3)
    Button(page2, text="查询", command=search).grid(row=6, column=1, padx=3)
    Button(page2, text="退出", command=root.quit).grid(row=6, column=4)


    # 删除
    page3 = Frame(notebook)
    Label(page3, text="请输入要删除的项目名称").grid(row=1, column=3, pady=15)
    Label(page3, text="项目名称:").grid(row=2, column=2)
    delete_name = StringVar()
    delete_name_entry = Entry(page3, textvariable=delete_name)
    delete_name_entry.grid(row=2, column=3, ipadx=70, pady=40)
    def delete():
        with open("password.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            df = pd.read_csv("password.csv")
            df.head(2)
            n = -1
            for row in rows:
                n += 1
                if delete_name.get() == row[0]:
                    # 删除行（某个范围）
                    df.drop(df.index[n - 1:n], inplace=True)
                    # 如果想要保存新的csv文件，则为
                    df.to_csv("password.csv", index=False, encoding="utf-8")
                    result = True
                    break
                else:
                    result = False
                    continue
            if result == True:
                delete_name_entry.delete(0, tk.END)
                Label(page3, text="删除成功!").grid(row=3, column=3)
            elif result == False:
                Label(page3, text="未找到对应信息!").grid(row=3, column=3)


    Button(page3, text="删除", command=delete).grid(row=4, column=1, padx=3, pady=30)
    Button(page3, text="退出", command=root.quit).grid(row=4, column=4)


    # 添加选项卡
    notebook.grid()
    notebook.add(page1, text="录入")
    notebook.add(page2, text="查询")
    notebook.add(page3, text="删除")

    root.mainloop()
if __name__ == '__main__':
    main()
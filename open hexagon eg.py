import tkinter as tk
from tkinter import messagebox
import random

def popup():
    x = random.randint(100, 700)  # 随机X坐标
    y = random.randint(100, 500)  # 随机Y坐标
    root.geometry(f"+{x}+{y}")    # 移动窗口到随机位置
    result = messagebox.askquestion("", "叫我一声爸")  # 显示“是”或“不是”
    
    if result == 'yes':  # 用户选择 "是"
        messagebox.showinfo("", "哎乖")  # 显示一个新消息
        roop.quit(10)  #退出程序
    else:  # 用户选择 "不是"
        messagebox.showinfo("", "好吧！")  # 显示另一个消息
    
    messagebox.showinfo("", "好吧！哈哈哈")  # 再次显示原来的消息

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 无限循环弹出
while True:
    popup()

root.mainloop()

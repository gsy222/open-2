import tkinter as tk
from tkinter import messagebox
import random

def popup():
    x = random.randint(100, 700)  # 随机X坐标
    y = random.randint(100, 500)  # 随机Y坐标
    root.geometry(f"+{x}+{y}")    # 移动窗口到随机位置
    messagebox.showinfo("Hi!", "I`m hack your computer now!")

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 无限循环弹出
while True:
    popup()

root.mainloop()

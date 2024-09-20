import tkinter as tk
from tkinter import messagebox
import random
import ctypes

# 隐藏后台控制台窗口（仅适用于 Windows）
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def popup():
    x = random.randint(100, 700)  # 随机X坐标
    y = random.randint(100, 500)  # 随机Y坐标
    popup_window = tk.Toplevel(root)
    popup_window.geometry(f"300x100+{x}+{y}")  # 弹出窗口的位置和大小
    popup_window.title("警告！")

    # 创建标签
    label = tk.Label(popup_window, text="I`m hack your computer now!", font=("Arial", 12))
    label.pack(pady=10)

    # 禁用窗口关闭按钮
    popup_window.protocol("WM_DELETE_WINDOW", lambda: None)

    # 增加窗口数量
    root.after(1000, popup)  # 每隔1秒弹出一个新窗口

# 创建Tkinter主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 弹出第一个窗口
popup()

root.mainloop()

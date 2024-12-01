import tkinter as tk
from Data.block import blockdata

def open_stock_block(parent):
    new_window = tk.Toplevel(parent)
    new_window.title("板块数据库")

    # 读取data 文件夹下的板块数据
    data = blockdata.data
    for key, block_val in data.items():
        # 展示每个block
        theme_title = key
        theme_button = tk.Button(new_window, text=theme_title, command=lambda t=theme_title, b=block_val: open_theme_details(t, b, parent))
        theme_button.pack()

def open_theme_details(theme_title, block_val, parent):
    details_window = tk.Toplevel(parent)
    details_window.title(theme_title)

    # 创建一个ListBox显示股票ID
    stock_listbox = tk.Listbox(details_window, height=10, width=30)
    for idx, stock_id in block_val.items():
        stock_listbox.insert(tk.END, f"股票ID: {stock_id}")
    stock_listbox.pack()

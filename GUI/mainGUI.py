import tkinter as tk
from stocktrend import open_stock_trend
from stockbroke import open_stock_broke_trend
from stockblock import open_stock_block 
from stocktheme import open_stock_theme
from stockcontinuous import open_stock_continuous
from stockconnection import open_stock_connection

# 建立一个空白页面
root = tk.Tk()
root.title("情绪量化交易系统")


# 建立涨停数据库按钮
button_stock_trend = tk.Button(root, text="涨停数据库", command=lambda: open_stock_trend(root))
button_stock_trend.pack()

# 建立跌停数据库按钮
button_stock_broke_trend = tk.Button(root, text="跌停数据库", command=lambda: open_stock_broke_trend(root))
button_stock_broke_trend.pack()

# 建立板块数据库按钮
button_stock_block = tk.Button(root, text="板块数据库", command=lambda: open_stock_block(root))
button_stock_block.pack()

# 建立题材数据库按钮
button_stock_theme = tk.Button(root, text="题材数据库", command=lambda: open_stock_theme(root))
button_stock_theme.pack()

# 建立连板数据库按钮
button_stock_continuous = tk.Button(root, text="连板数据库", command=lambda: open_stock_continuous(root))
button_stock_continuous.pack()

# 建立涨停关联数据库按钮
button_stock_connection = tk.Button(root, text="涨停关联数据库", command=lambda: open_stock_connection(root))
button_stock_connection.pack()

root.mainloop()
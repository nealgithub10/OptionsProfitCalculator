import getopt
import tkinter as tk

from CSProject.stocks import printValues
from CSProject.Main import calculate1
from CSProject.Main import calculate2
from CSProject.Main import calculatePut1
from CSProject.Main import calculatePut2
# from CSProject.Main import calculate
# from CSProject.Main import calculatePut

def on_search():
    print("Searching for ticker...")

def on_selection(value):
    print("Selected option:", value)

root = tk.Tk()
root.title("OptiFinance")
root.configure(bg="white")
root.minsize(600,400)

# Title bar
title_frame = tk.Frame(root, bg="black", height=30)
title_frame.pack(fill=tk.X, side=tk.TOP)
title = tk.Label(title_frame, text="OptiFinance", font=("Helvetica", 16), bg="black", fg="white")
title.pack(pady=5)

def getinfo():
    ticker = search_entry.get()
    data = printValues(ticker)
    for d in data:
        print(d)

# Search bar
search_frame = tk.Frame(root, bg="white")
search_frame.pack(fill=tk.X, pady=10)

search_label = tk.Label(search_frame, text="TICKER-->", bg="black")
search_label.pack(side=tk.LEFT, padx=10)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Search", command=getinfo)
search_button.pack(side=tk.LEFT, padx=10)



# Dropdown menu
option_var = tk.StringVar(root)
option_var.set("Select an option")

options = [
    "OptionCalcBuy",
    "OptionCalcPutBuy",
    "OptionCalcSell",
    "OptionCalcPutSell"
]

dropdown = tk.OptionMenu(root, option_var, *options, command=on_selection)
dropdown.pack(pady=10)


# def getopt():
#     option = option_var.get()
#     print(option)
#     if option_var.get()=="OptionCalcBuy":
#         calculate(5,5)

submit_button = tk.Button(search_frame, text="Search", command=getopt)
submit_button.pack(side=tk.LEFT, padx=10)



root.mainloop()

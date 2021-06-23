## Importing
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import sqrt

root = Tk()
root.title("this is the newer code")

def insert(text) :
    Entry.insert(END, text)

## Elements
Entry = ttk.Entry(root, width = 50, font = ('Arial', 10))
Entry.grid(row = 0, column = 0, columnspan = 3, ipady = 10, ipadx = 10, pady = 8, padx = 8)

show = ttk.Entry(root, width  = 40, font = ('Arial', 10))
show.grid(row = 1, column = 0, columnspan = 3, ipady = 10, ipadx = 10, pady = 8, padx = 8)

########################

x = ttk.Button(root, width = 10, text = "x", command = lambda:insert("x "))
x.grid(row = 2, column = 0, ipadx = 8, ipady = 8, pady = 8, padx = 8)

X = ttk.Button(root, width = 10, text = "X", command = lambda:insert("X "))
X.grid(row = 2, column = 2, ipadx = 8, ipady = 8, pady = 8, padx = 8)

########################

buttons_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "+", 0, "-", "*", "=", "/", "*"]

rows = 3
columns = 0

for i in buttons_list :
    if i == "+" : name = "plus"
    elif i == "-" : name = "minus"
    elif i == "*" : name = "times"
    elif i == "." : name = "point"
    elif i == "/" : name = "divide"
    elif i == "=" : name = "equal"
    else : name = i
    exec(f"button_{name} = ttk.Button(root, text = '{i}', command = lambda:insert('{i} '))")
    exec(f"button_{name}.grid(row = rows, column = columns, ipadx = 8, ipady = 8)")
    columns += 1
    
    if columns == 3 :
        rows += 1
        columns = 0


button_delete = ttk.Button(root, text = "C", command = lambda:Entry.delete(0, END) )
button_delete.grid(row = 8, column = 1, ipady = 8, ipadx = 8)

button_calculate = ttk.Button(root, text = "calculate")
button_calculate.grid(row = 8, column = 2, ipady = 8, ipadx = 8)
        
########################

def calculate() :
    entry_list = Entry.get().split()
    result = float(entry_list[entry_list.index("=") + 1])
    ##############################################################
    for i in entry_list :
        if i == "+" :
            result -= float(entry_list[entry_list.index("+") + 1])
        elif i == "-" :
            result += float(entry_list[entry_list.index("-") + 1])
        elif i == "*" :
            result /= float(entry_list[entry_list.index("*") + 1])
        elif i == "/" :
            result *= float(entry_list[entry_list.index("/") + 1])
        else :
            pass
    
    if "X" in entry_list :
        result = sqrt(result)
    else :
        pass
    
    show.delete(0, END)

    show.insert(END, result)
    
    Entry.delete(0, END)
    

button_calculate.configure(command = calculate)

root.mainloop()

from tkinter import ttk
import tkinter as tk
from tkinter import *
import json

with open("config.json", "r") as config:
    data = json.load(config)

print(data)

cal = Tk()
cal.title('Fluent Calculator')

menubar = Menu(cal)
darkmode = tk.BooleanVar()
darkmode.set(False)

operator=""
tex_input= StringVar()
cal.geometry('229x300')
cal.iconbitmap('Calculator.ico')

def btnClick(numbers) :
    global operator
    operator=operator+str(numbers)
    tex_input.set(operator)

def btnClearDisplay():
    global operator
    tex_input.set("")
    operator=""

def btnEqualsInput():
    try:
      global operator
      sumup=str(eval(operator))
      tex_input.set(sumup)
      operator=""
    except:
     tex_input.set("meow")
     operator=""

def setdarkmode():
    if darkmode.get() == True:
        cal.tk.call("set_theme", "dark")  #You can change to "dark"
        data['darkmode'] = 'True'
    else:
        cal.tk.call("set_theme", "light")  #You can change to "dark"
        data['darkmode'] = 'False'

    updateConfig()

def updateConfig():
    with open("config.json", "w") as jsonfile:
        json.dump(data, jsonfile)
        jsonfile.close()

cal = Tk()
cal.title('Fluent Calculator')

menubar = Menu(cal)
darkmode = tk.BooleanVar()

if data['darkmode'] == "True":
    darkmode.set(True)
else:
    darkmode.set(False)

menubar.add_checkbutton(label="Dark Mode", onvalue=True, offvalue=False, variable=darkmode, command=setdarkmode)

menubar.add_checkbutton(label="Mode", onvalue=1, offvalue=0, variable=darkmode, command=setdarkmode)

cal.grid_columnconfigure(0,weight=1)
cal.grid_columnconfigure(1,weight=1)
cal.grid_columnconfigure(2,weight=1)
cal.grid_columnconfigure(3,weight=1)

#Entry to show result
txtDisplay = ttk.Entry(cal, textvariable=tex_input, font='12', justify='right').grid(columnspan=5, pady=8)

#First Column
btn7=ttk.Button(cal, text="7", command=lambda:btnClick(7)).grid(row=1, column=0, padx= 8, pady= 5, ipadx=4, ipady=5)
btn4=ttk.Button(cal, text="4", command=lambda:btnClick(4)).grid(row=2, column=0, padx= 8, pady= 5, ipadx=4, ipady=5)
btn1=ttk.Button(cal, text="1", command=lambda:btnClick(1)).grid(row=4, column=0, padx= 8, pady= 5, ipadx=5, ipady=5)
btn1=ttk.Button(cal, text="0", command=lambda:btnClick(0)).grid(row=5, column=0, padx= 8, pady= 5, ipadx=4, ipady=5)

#Second Column
btn8=ttk.Button(cal, text="8", command=lambda:btnClick(8)).grid(row=1, column=1, padx= 0, pady= 0, ipadx=4, ipady=5)
btn5=ttk.Button(cal, text="5", command=lambda:btnClick(5)).grid(row=2, column=1, padx= 0, pady= 0, ipadx=4, ipady=5)
btn2=ttk.Button(cal, text="2", command=lambda:btnClick(2)).grid(row=4, column=1, padx= 0, pady= 0, ipadx=4, ipady=5)
btnClear=ttk.Button(cal, text="C", style="Accent.TButton", command=btnClearDisplay).grid(row=5, column=1, padx= 10, pady= 0, ipadx=3, ipady=5)

#Thỉrd Column
btn9=ttk.Button(cal, text="9", command=lambda:btnClick(9)).grid(row=1, column=2, padx= 0, pady= 0, ipadx=4, ipady=5)
btn6=ttk.Button(cal, text="6", command=lambda:btnClick(6)).grid(row=2, column=2, padx= 0, pady= 0, ipadx=4, ipady=5)
btn3=ttk.Button(cal, text="3", command=lambda:btnClick(3)).grid(row=4, column=2, padx= 0, pady= 0, ipadx=4, ipady=5)
equal=ttk.Button(cal, text="=", style="Accent.TButton", command=btnEqualsInput).grid(row=5, column=2, padx= 10, pady= 0, ipadx=2, ipady=5)

#Fourth Column
Addition=ttk.Button(cal, text="+",  command=lambda:btnClick("+")). grid(row=1, column=3, padx= 8, pady= 0, ipadx=3, ipady=5)
Subtraction=ttk.Button(cal, text="-", command=lambda:btnClick("-")). grid(row=2, column=3, padx= 8, pady= 0, ipadx=4, ipady=5)
Multiple=ttk.Button(cal, text="x", command=lambda:btnClick("*")). grid(row=4, column=3, padx= 8, pady= 0, ipadx=4, ipady=5)
Divsion=ttk.Button(cal, text=":", command=lambda:btnClick("/")). grid(row=5, column=3, padx= 8, pady= 0, ipadx=5, ipady=5)

cal.tk.call("source", "sun-valley.tcl")
setdarkmode() # Calls the function initially to repreasent what user expects from config, if not True then defaults to light mode

#Min width for the calculator
cal.update()
cal.minsize(cal.winfo_width(), cal.winfo_height())
x_cordinate = int((cal.winfo_screenwidth() / 2) - (cal.winfo_width() / 2))
y_cordinate = int((cal.winfo_screenheight() / 2) - (cal.winfo_height() / 2))
cal.resizable(False, False)

cal.config(menu=menubar)
cal.mainloop()

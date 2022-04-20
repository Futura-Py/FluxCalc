from tkinter import BooleanVar, ttk, Label, StringVar
import tkinter as tk
import darkdetect
import sv_ttk
import ntkutils

calculation = ""

def btnClick(key):
    global calculation
    calculation = calculation + str(key)
    content.set(calculation)

def btnClearDisplay():
    global calculation
    content2.set("")
    content.set("0")
    calculation = ""

def btnEqualsInput():
    try:
        global calculation
        content2.set(calculation)
        content.set(eval(calculation))
        calculation = ""
    except:
        content.set("Error")
        calculation = ""

def backspace():
        global calculation
        calculation = calculation[:-1]
        content2.set("")
        content.set(calculation)

def aot():
    if always_on_top.get() == 1:
        root.attributes('-topmost', True)
    else:
        root.attributes('-topmost', False)

def square():
    try:
        global calculation
        try:
            int(calculation)
            content2.set(calculation + '²')
            calculation = eval("{}*{}".format(calculation, calculation))        
            if str(calculation).endswith(".0"): calculation = str(calculation).rstrip(".0")
            content.set(calculation)
            calculation =""
        except ValueError:
            content2.set("feature still in")
            content.set("development")
    except:
        content2.set("")
        content.set("Error")
        operator=""

root=tk.Tk()
root.resizable(False, False)
root.geometry('318x480')
root.title('')
root.iconbitmap(r'Calculator.ico')
ntkutils.placeappincenter(root)

if darkdetect.theme() == "Dark":
    sv_ttk.set_theme("dark")
    ntkutils.dark_title_bar(root)
    ntkutils.blur_window_background(root)
else:
    sv_ttk.set_theme("light")
    ntkutils.blur_window_background(root)    
            
operator=""
always_on_top = BooleanVar()
content= StringVar()
content2 = StringVar()
content.set("0")

Display = Label(root, textvariable=content, font=('Segoe UI Variable Display Semibold','35'),anchor="e",width=11).place(x=0, y=60)
Display2 =Label(root,textvariable=content2, font=('Segoe UI Variable Display Semibold','15'),anchor="e",width=11, fg='#707476').place(x=162,y=30)

btn1=ttk.Button(root, text="1", command=lambda:btnClick(1)).place(x=4, y=368, height=53, width=76)
btn2=ttk.Button(root, text="2", command=lambda:btnClick(2)).place(x=82, y=368, height=53, width=76)
btn3=ttk.Button(root, text="3", command=lambda:btnClick(3)).place(x=160, y=368, height=53, width=76)
btn4=ttk.Button(root, text="4", command=lambda:btnClick(4)).place(x=4, y=313, height=53, width=76)
btn5=ttk.Button(root, text="5", command=lambda:btnClick(5)).place(x=82, y=313, height=53, width=76)
btn6=ttk.Button(root, text="6", command=lambda:btnClick(6)).place(x=160, y=313, height=53, width=76)
btn7=ttk.Button(root, text="7", command=lambda:btnClick(7)).place(x=4, y=258, height=53, width=76)
btn8=ttk.Button(root, text="8", command=lambda:btnClick(8)).place(x=82, y=258, height=53, width=76)
btn9=ttk.Button(root, text="9", command=lambda:btnClick(9)).place(x=160, y=258, height=53, width=76)
btn0=ttk.Button(root, text="0", command=lambda:btnClick(0)).place(x=4, y=423, height=53, width=154)

alwaysontop=ttk.Checkbutton(root, text="", variable = always_on_top,onvalue=1, offvalue=0, style="Toggle.TButton",command=lambda:aot()).place(x=4, y=148, height=53, width=76)
openbtn=ttk.Button(root, text="(", command=lambda:btnClick('(')).place(x=82, y=148, height=53, width=76)
closebtn=ttk.Button(root, text=")", command=lambda:btnClick(')')).place(x=160, y=148, height=53, width=76)
btnClear=ttk.Button(root, text="C", command=btnClearDisplay).place(x=82, y= 203, height=53, width=76)
Backspace = ttk.Button(root, text='', command=backspace).place(x=160, y=203, height=53, width=76)
btndot=ttk.Button(root, text=".", command=lambda:btnClick('.')).place(x=160, y=423, height=53, width=76)

Divsion=ttk.Button(root, text="", command=lambda:btnClick("/")).place(x=238, y=148, height=53, width=76)
Multiple=ttk.Button(root, text="", command=lambda:btnClick("*")).place(x=238, y=203, height=53, width=76)
Subtraction=ttk.Button(root, text="", command=lambda:btnClick("-")).place(x=238, y=258, height=53, width=76)
Addition=ttk.Button(root, text="",  command=lambda:btnClick("+")).place(x=238, y=313, height=53, width=76)
btnsquare=ttk.Button(root, text="x²", command=lambda:square()).place(x=4, y=203, height=53, width=76)
equal=ttk.Button(root, text="", command=btnEqualsInput).place(x=238, y=368, height=108, width=76)

root.bind('<Return>', btnEqualsInput)
root.bind('<BackSpace>', backspace)

root.mainloop()
from tkinter import BooleanVar, ttk, Label, StringVar
import tkinter as tk
import darkdetect
import sv_ttk
import ntkutils

def btnClick(numbers, event=None):
    global operator
    tex_input2.set('')
    operator=operator+str(numbers)
    tex_input.set(operator)

def btnClearDisplay():
    global operator
    tex_input2.set("")
    tex_input.set("0")
    operator=""

def btnEqualsInput(event=None):
    try:
        global operator
        sumup=str(eval(operator))
        tex_input2.set(operator)
        tex_input.set(sumup)
        operator=""
    except:
        tex_input.set("Error")
        operator=""

def backspace(event=None):
        global operator
        operator = operator[:-1]
        tex_input2.set("")
        tex_input.set(operator)

def aot():
    if always_on_top.get() == 1:
        root.attributes('-topmost', True)
    else:
        root.attributes('-topmost', False)

def square():
    try:
        global operator
        tex_input2.set(operator + '²')
        ans = float(operator)
        squr = ans*ans
        tex_input.set(str(squr))
        operator =""
    except:
        tex_input2.set("")
        tex_input.set("Error")
        operator=""

btnwidth = 76
zerowidth = btnwidth*2+2
btnheight = 53

root=tk.Tk()
root.resizable(False, False)
root.geometry('318x480')
root.title('')
root.iconbitmap(r'Calculator.ico')
ntkutils.placeappincenter(root)

if darkdetect.theme() == "Light":
    sv_ttk.set_theme("dark")
    ntkutils.dark_title_bar(root)
    ntkutils.blur_window_background(root)
    btnwidth = 74
    zerowidth = btnwidth*2+4
    btnheight = 51
else:
    sv_ttk.set_theme("light")
    ntkutils.blur_window_background(root)    
            
operator=""
tex_input= StringVar()
tex_input2 = StringVar()
tex_input.set("0")
txtDisplay = Label(root, textvariable=tex_input, font=('Segoe UI Variable Display Semibold','35'),anchor="e",width=11).place(x=0, y=60)
txtDisplay2 =Label(root,textvariable=tex_input2, font=('Segoe UI Variable Display Semibold','15'),anchor="e",width=11, fg='#707476').place(x=162,y=30)

always_on_top = BooleanVar()
alwaysontop=ttk.Checkbutton(root, text="", variable = always_on_top,onvalue=1, offvalue=0, style="Toggle.TButton",command=lambda:aot()).place(x=4, y= 148, height=btnheight, width=btnwidth)
btnsquare=ttk.Button(root, text="x²", command=lambda:square()).place(x=4, y= 203, height=btnheight, width=btnwidth)
btn7=ttk.Button(root, text="7", command=lambda:btnClick(7)).place(x=4, y= 258, height=btnheight, width=btnwidth)
btn4=ttk.Button(root, text="4", command=lambda:btnClick(4)).place(x=4, y= 313, height=btnheight, width=btnwidth)
btn1=ttk.Button(root, text="1", command=lambda:btnClick(1)).place(x=4, y= 368, height=btnheight, width=btnwidth)

openbtn=ttk.Button(root, text="(", command=lambda:btnClick('(')).place(x=82, y= 148, height=btnheight, width=btnwidth)
btnClear=ttk.Button(root, text="C", command=btnClearDisplay).place(x=82, y= 203, height=btnheight, width=btnwidth)
btn8=ttk.Button(root, text="8", command=lambda:btnClick(8)).place(x=82, y= 258, height=btnheight, width=btnwidth)
btn5=ttk.Button(root, text="5", command=lambda:btnClick(5)).place(x=82, y= 313, height=btnheight, width=btnwidth)
btn2=ttk.Button(root, text="2", command=lambda:btnClick(2)).place(x=82, y= 368, height=btnheight, width=btnwidth)
btn0=ttk.Button(root, text="0", command=lambda:btnClick(0)).place(x=4, y= 423, height=btnheight, width=zerowidth)

closebtn=ttk.Button(root, text=")", command=lambda:btnClick(')')).place(x=160, y= 148, height=btnheight, width=btnwidth)
Backspace = ttk.Button(root, text='', command=backspace).place(x=160, y= 203, height=btnheight, width=btnwidth)
btn9=ttk.Button(root, text="9", command=lambda:btnClick(9)).place(x=160, y= 258, height=btnheight, width=btnwidth)
btn6=ttk.Button(root, text="6", command=lambda:btnClick(6)).place(x=160, y= 313, height=btnheight, width=btnwidth)
btn3=ttk.Button(root, text="3", command=lambda:btnClick(3)).place(x=160, y= 368, height=btnheight, width=btnwidth)
btndot=ttk.Button(root, text=".", command=lambda:btnClick('.')).place(x=160, y= 423, height=btnheight, width=btnwidth)

Divsion=ttk.Button(root, text="", command=lambda:btnClick("/")).place(x=238, y= 148, height=btnheight, width=btnwidth)
Multiple=ttk.Button(root, text="", command=lambda:btnClick("*")).place(x=238, y= 203, height=btnheight, width=btnwidth)
Subtraction=ttk.Button(root, text="", command=lambda:btnClick("-")).place(x=238, y= 258, height=btnheight, width=btnwidth)
Addition=ttk.Button(root, text="",  command=lambda:btnClick("+")).place(x=238, y= 313, height=btnheight, width=btnwidth)
equal=ttk.Button(root, text="", command=btnEqualsInput).place(x=238, y= 368, height=btnheight*2+2, width=btnwidth)

root.bind('<Return>', btnEqualsInput)
root.bind('<BackSpace>', backspace)

root.mainloop()
from tkinter import ttk
from tkinter import *
from BlurWindow.blurWindow import *
import ctypes
import darkdetect

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
     tex_input.set("Error")
     operator=""

def change_theme():
    if cal.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        cal.tk.call("set_theme", "light")
        bg_color = ttk.Style().lookup(".", "background")
        cal.wm_attributes("-transparent", bg_color)
        HWND = ctypes.windll.user32.GetForegroundWindow()
        GlobalBlur(HWND, Acrylic=True, Dark=False, hexColor=f"{bg_color}")
        cal.update()
    else:
        cal.tk.call("set_theme", "dark")
        bg_color = ttk.Style().lookup(".", "background")
        cal.wm_attributes("-transparent", bg_color)
        HWND = ctypes.windll.user32.GetForegroundWindow()
        GlobalBlur(HWND, Acrylic=True, Dark=True, hexColor=f"{bg_color}")
        cal.update()

cal = Tk()
cal.title('Fluent Calculator')

operator=""
tex_input= StringVar()
cal.geometry('238x338')
cal.iconbitmap("Calculator.ico")

cal.grid_columnconfigure(0,weight=1)
cal.grid_columnconfigure(1,weight=1)
cal.grid_columnconfigure(2,weight=1)
cal.grid_columnconfigure(3,weight=1)

#Entry to show result
txtDisplay = ttk.Entry(cal, textvariable=tex_input, font='50', justify='right').grid(columnspan=4, pady=8, ipadx=9, ipady= 1)

#First Column
btnM=ttk.Button(cal, text="(", command=lambda:btnClick('(')).grid(row=1, column=0, padx= 8, pady= 8, ipadx=7, ipady=1)
btn7=ttk.Button(cal, text="7", command=lambda:btnClick(7)).grid(row=2, column=0, padx= 8, pady= 5, ipadx=4, ipady=5)
btn4=ttk.Button(cal, text="4", command=lambda:btnClick(4)).grid(row=3, column=0, padx= 8, pady= 5, ipadx=4, ipady=5)
btn1=ttk.Button(cal, text="1", command=lambda:btnClick(1)).grid(row=4, column=0, padx= 8, pady= 5, ipadx=5, ipady=5)
btn1=ttk.Button(cal, text="0", command=lambda:btnClick(0)).grid(row=5, column=0, padx= 8, pady= 5, ipadx=4, ipady=5)

#Second Column
btnM=ttk.Button(cal, text=")", command=lambda:btnClick(')')).grid(row=1, column=1, padx= 8, pady= 8, ipadx=7, ipady=1)
btn8=ttk.Button(cal, text="8", command=lambda:btnClick(8)).grid(row=2, column=1, padx= 0, pady= 0, ipadx=4, ipady=5)
btn5=ttk.Button(cal, text="5", command=lambda:btnClick(5)).grid(row=3, column=1, padx= 0, pady= 0, ipadx=4, ipady=5)
btn2=ttk.Button(cal, text="2", command=lambda:btnClick(2)).grid(row=4, column=1, padx= 0, pady= 0, ipadx=4, ipady=5)
btnClear=ttk.Button(cal, text="C", style="Accent.TButton", command=btnClearDisplay).grid(row=5, column=1, padx= 10, pady= 0, ipadx=3, ipady=5)

#Thỉrd Column
btnM=ttk.Button(cal, text=".", command=lambda:btnClick('.')).grid(row=1, column=2, padx= 8, pady= 8, ipadx=7, ipady=1)
btn9=ttk.Button(cal, text="9", command=lambda:btnClick(9)).grid(row=2, column=2, padx= 0, pady= 0, ipadx=4, ipady=5)
btn6=ttk.Button(cal, text="6", command=lambda:btnClick(6)).grid(row=3, column=2, padx= 0, pady= 0, ipadx=4, ipady=5)
btn3=ttk.Button(cal, text="3", command=lambda:btnClick(3)).grid(row=4, column=2, padx= 0, pady= 0, ipadx=4, ipady=5)
equal=ttk.Button(cal, text="=", style="Accent.TButton", command=btnEqualsInput).grid(row=5, column=2, padx= 10, pady= 0, ipadx=2, ipady=5)

photo = PhotoImage(file = r"Assets.png")

#Fourth Column
backspace = ttk.Button(cal, image=photo).grid(row=1, column=3, padx=8, pady= 0, ipady= 4)
Addition=ttk.Button(cal, text="+",  command=lambda:btnClick("+")). grid(row=2, column=3, padx= 8, pady= 0, ipadx=3, ipady=5)
Subtraction=ttk.Button(cal, text="-", command=lambda:btnClick("-")). grid(row=3, column=3, padx= 8, pady= 0, ipadx=4, ipady=5)
Multiple=ttk.Button(cal, text="x", command=lambda:btnClick("*")). grid(row=4, column=3, padx= 8, pady= 0, ipadx=4, ipady=5)
Divsion=ttk.Button(cal, text="÷", command=lambda:btnClick("/")). grid(row=5, column=3, padx= 8, pady= 0, ipadx=3, ipady=5)

cal.tk.call("source", "sun-valley.tcl")
cal.tk.call("set_theme", "light")

#Min width for the calculator
cal.update()
cal.minsize(cal.winfo_width(), cal.winfo_height())
x_cordinate = int((cal.winfo_screenwidth() / 2) - (cal.winfo_width() / 2))
y_cordinate = int((cal.winfo_screenheight() / 2) - (cal.winfo_height() / 2))
cal.resizable(False, False)

bg_color = ttk.Style().lookup(".", "background")
cal.wm_attributes("-transparent", bg_color)
HWND = ctypes.windll.user32.GetForegroundWindow()
if   darkdetect.isDark():
    cal.tk.call("set_theme", "dark")
    bg_color = ttk.Style().lookup(".", "background")
    cal.wm_attributes("-transparent", bg_color)
    HWND = ctypes.windll.user32.GetForegroundWindow()
    GlobalBlur(HWND, Acrylic=True, Dark=True, hexColor=f"{bg_color}")
    cal.update()
else:
    cal.tk.call("set_theme", "light")
    bg_color = ttk.Style().lookup(".", "background")
    GlobalBlur(HWND, Acrylic=True, Dark=False, hexColor=f"{bg_color}")

cal.mainloop()
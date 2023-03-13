#Graphical user interface tkinter
#Calculator
#libraries
import tkinter as tk
import tkinter.ttk as ttk
#root for the program
window = tk.Tk()
#sets title for the program
window.title("Calculator App Using Tkinter")
#sets the size of the window to be displayed
# window.configure(width=300,height=300,background="red")
#Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return current value if None is given.
window.geometry('400x200')

#resizable - Instruct the window manager whether this width can be resized in WIDTH or HEIGHT. Both values are boolean values.
# window.resizable(False,False)
#min size of the window
window.minsize(200, 100)
#max size of the window
window.maxsize(300, 200)
#ttk - Ttk wrapper.

# This module provides classes to allow using Tk themed widget set.

# Ttk is based on a revised and enhanced version of
# TIP #48 (http://tip.tcl.tk/48) specified style engine.

# Its basic idea is to separate, to the extent possible, the code implementing a widget's behavior from the code implementing its appearance. Widget class bindings are primarily responsible for maintaining the widget state and invoking callbacks, all aspects of the widgets appearance lies at Themes.
label = ttk.Label(window,text="Calculator")
# label.pack()
#button
# button.pack()
# button = ttk.Button(window,text="h")

expression = ''

text = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    text.set(expression)

def clr():
    global expression
    expression = ''
    text.set(expression)

def equal():
    equal_txt = str(eval(expression))
    text.set(equal_txt)
#entry field
entry = ttk.Entry(window,justify='right',textvariable=text)
entry.grid(row=0,columnspan=4,sticky='nsew')
button_7 = ttk.Button(window,text=7,command=lambda:press(7))
button_7.grid(row=1,column=0)
button_8 = ttk.Button(window,text=8,command=lambda:press(8))
button_8.grid(row=1,column=1)
button_9 = ttk.Button(window,text=9,command=lambda:press(9))
button_9.grid(row=1,column=2)
button_d = ttk.Button(window,text='/',command=lambda:press('/'))
button_d.grid(row=1,column=3)


button_4 = ttk.Button(window,text=4,command=lambda:press(4))
button_4.grid(row=2,column=0)
button_5 = ttk.Button(window,text=5,command=lambda:press(5))
button_5.grid(row=2,column=1)
button_6 = ttk.Button(window,text=6,command=lambda:press(6))
button_6.grid(row=2,column=2)
button_m = ttk.Button(window,text='*',command=lambda:press('*'))
button_m.grid(row=2,column=3)


button_1 = ttk.Button(window,text=1,command=lambda:press(1))
button_1.grid(row=3,column=0)
button_2 = ttk.Button(window,text=2,command=lambda:press(2))
button_2.grid(row=3,column=1)
button_3 = ttk.Button(window,text=3,command=lambda:press(3))
button_3.grid(row=3,column=2)
button_s = ttk.Button(window,text='-',command=lambda:press('-'))
button_s.grid(row=3,column=3)


button_0 = ttk.Button(window,text=0,command=lambda:press(0))
button_0.grid(row=4,column=0)
button_dot = ttk.Button(window,text='.',command=lambda:press('.'))
button_dot.grid(row=4,column=1)
button_ac = ttk.Button(window,text='C',command=clr)
button_ac.grid(row=4,column=2)
button_p = ttk.Button(window,text='+',command=lambda:press('+'))
button_p.grid(row=4,column=3)
#column span takes 4 columns to display the button
button_equals = ttk.Button(window,text='=',command=equal)
button_equals.grid(row=5,columnspan=4,sticky='nsew')
#opens the window
window.mainloop()
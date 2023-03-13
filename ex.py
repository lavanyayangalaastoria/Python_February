import tkinter as tk
from tkinter import *


def calculate():
    input_value = input_entry.get()
    if input_value:
        try:
            result = eval(input_value)
        except:
            result_label.config(text="Error")
        else:
            result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Result: ")

def btn_click(number):
    current = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, str(current) + str(number))

def btn_clear():
    input_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

input_frame = tk.Frame(root)
input_frame.pack()

result_frame = tk.Frame(root)
result_frame.pack()

input_entry = tk.Entry(input_frame, width=35, borderwidth=5)
input_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

result_label = tk.Label(result_frame, text="Result: ")
result_label.pack()

# Create buttons
btn_1 = tk.Button(input_frame, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn_2 = tk.Button(input_frame, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn_3 = tk.Button(input_frame, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn_4 = tk.Button(input_frame, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn_5 = tk.Button(input_frame, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn_6 = tk.Button(input_frame, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn_7 = tk.Button(input_frame, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn_8 = tk.Button(input_frame, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn_9 = tk.Button(input_frame, text="9", padx=40, pady=20, command=lambda: btn_click(9))

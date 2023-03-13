from pywebio.input import *
from pywebio.output import *
def web_app_calculator():
    first_number = input("Enter the first number",type="number")
    second_number = input("Enter the second number",type="number")
    output = 0 
    operator = radio("Choose Mathematical operator name: ",options=['+','-','/','%','*'])
    operator_name = ""
    if operator == "+":
        operator_name = "Addition"
        output = first_number + second_number
    elif operator == "-":
        operator_name = "Subtraction"
        output = first_number - second_number
    elif operator == '/':
        operator_name = "Division"
        output = first_number / second_number
    elif operator == '%':
        operator_name = "Percentage"
        output = first_number % second_number
    else:
        operator_name = "Multiplication"
        output = first_number * second_number
    put_text("The operator selected is: %s and the output is: %.1f" %(operator_name,output))
web_app_calculator()
while True:
    choice = input("Do you want continue? \n 1.Yes. \n 2.No.\n")
    if choice == "1":
        print("Your choice is:",choice)
        web_app_calculator()
    else:
        break


def addition(num1,num2):
    return num1 + num2


def subtraction(num1,num2):
    return num1 - num2


def multiplication(num1,num2):
    return num1 * num2


def division(num1,num2):
    return num1 / num2

def calculation():
    num1 = input("Enter first number:")
    if(num1.isdigit()):
        num1 = float(num1)
    else:
        print("Invalid input")
        quit()
    num2 = input("Enter second number:")
    if(num2.isdigit()):
        num2 = float(num2)
    else:
        print("Invalid input")
        quit()
    choice = input("Enter choice \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n")
    if choice == "1":
        print("The output for Addition is: ", addition(num1,num2))
    elif choice == "2":
        print("The output for Subtraction is: ", subtraction(num1,num2))
    elif choice == "3":
        print("The output for Multiplication is: ", multiplication(num1,num2))
    elif choice == "4":
        print("The output for Division is: ", division(num1,num2))
    else:
        print("Enter Valid Choice")
calculation()

while True:
    choice = input("Do you want continue? \n 1.Yes. \n 2.No.\n")
    if choice == "1":
        print("Your choice is:",choice)
        calculation()
    else:
        break

list_declaration = ['megha','lavanya','priya','sridevi','ramadevi','anuja','jaishree''chitranjan','abhishek']
print(list_declaration)
#we can change list in this manner.
print(list_declaration[0])
list_declaration[1] = 'o'
print(list_declaration)
#lists allow duplicates.
print(len(list_declaration))
#lists can contain different datatypes.
lis1 = ['f',4,'jj']
print(lis1)

print(type(lis1))
thislist = list((3,'k',"m",'k'))
print(type(thislist))
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist=["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3]=["blackcurrent","watermelon"]
print(thislist)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

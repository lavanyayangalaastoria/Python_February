#looping through array
# for char in 'banana':
#     print(char)
# #find length of the string
# word = "HELLO    "
# print(len(word))
# #check string.
# check = "Hello how are you"
# print('Hello' not in check)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrent", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1,tuple2,tuple3)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

try:
   print(x)
except:
   print("Something went wrong")
finally:
   print("The 'try except' is finished")


try:
    print(x)
except:
    print("An exception occurred")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
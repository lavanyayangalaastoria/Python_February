

# 1.local variable cannot be accessed by global variable.
# def test():
#     a = 'local'
# test()
# print(a)




# 2.Local variables cannot be accessed from other local scope.

# def test1():
#     a = 'local test1'
# def test2():
#     test1()
#     print(a)
# test2()
#3.global variables can be accessed by any local scope.

a ='global'
def test():
    print(a)
test()

#3
a ='global'
def test():
    a = 'local'
    print(a)
test()



#4.local and global variables can share the same name.
a = 'global'

def func():
    a = 'local'
print(a)
func()

#5.Global variables can be modified inside a local scope using global keyword

a = 'global'
def test():
    global a
    a = 'local'
print("Using global variables:",a)
test()
print("Using global variable:",a)


a = 20 #global
def display():
    b = 30 #local
    print("Value is",a)
    print("Value is",b)
display()
c = 40
print("Value is",c)
print("Value is ",a)





# a = 20
# def function():
#     b = 30
#     print("Value is:",a)
#     print("Value is",b)
# function()
# print("Value is",a)
# print("Value is",b)






















a = 20
def display():
    print("Local value is",a)
display()
print("Global Value is",a)




























































# x=88
# def harry():
#     x = 20
#     def rohan():
#         global x 
#         x = 99
#     print("Before calling Rohan",x)
#     rohan()
    
#     print("After calling Rohan",x)
# harry()

# print(x)





# # l = 10 #Global
# # m=5
# # def function1(n):
# #     global l
# #     l = 5 #local
# #     m = 6 #local
# #     print(l,m)
# #     print(n,"I have printed")
# # function1("This is me")
# # print(l,m)

class Person:
    def __init__(self):
        self.name = "Jack Matte"

    def bio(self):
        self.addr = "Bakers street, London"
        self.taxInfo = "HUAPK29971"
        self.contact = "01-777-523-342"
        #print(self.addr, self.taxInfo, self.contact)

    def interest(self):
        self.favFood = "Chinese"
        self.__hobbies = "Python Programming"
        self._bloodGroup = "A+"
        #print(self.favFood, self.hobbies, self.bloodGroup)
        print(self._bloodGroup,self.__hobbies)








obj = Person()
print(obj.name)

obj.bio()
obj.interest()
print(obj.favFood)
print()
class ParentClass:
    string = "Python Programming Language"
    def display(self):
        return self.string
class ChildClass(ParentClass):
    pass
child = ChildClass()
print(child.display())

class User:
    pass
# user1 is an instance or object of class
user1 = User()
# fields : Data attached to an object
# should not capitalise name of fields
user1.first_name ='lavanya'
user1.last_name = 'yangala'
print(user1.first_name)
print(user1.last_name)
# seperate names with underscore
first_name ='Megha'
last_name='Ahirwar'
print(first_name,last_name)
print(user1.first_name,user1.last_name)
user2 = User()
user2.first_name = 'Rama'
user2.last_name='Devi'
#class features
#methods
#initialisation
#doctext
#function inside a class is initialization and init
class user:
    def __init__(self,full_name,birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
user = user("rani","19710808")
print(user.name)
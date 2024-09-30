# # Creating Class 
# class Person :
#     name = "Ajay"
#     occupation = "Web Developer"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a = Person() # Object Created 
# b = Person() # Object Created 
# c = Person() # Object Created 
# d = Person() # Object Created 

# b.name = "Vishu"
# b.occupation = "Software Developer"

# c.name = "Rohan"
# c.occupation = "Coder"

# d.name = "Harsh"
# d.occupation = "App Developer"

# a.info() 
# b.info() 
# c.info() 
# d.info() 




# Using Constructor 
class Student :
    def __init__(self , name , id , course): # Parametrisied Constructor 
        self.name = name
        self.id = id
        self.course = course

    def details(self):
        print(f" Name : {self.name} Id : {self.id} Course : {self.course}")

a = Student("Ajay", 23 , "BCA")
b = Student("Vishu", 24 , "BCA")
c = Student("Harsh", 25 , "Bsc")
d = Student("Mayank", 26 , "BA")

a.details()
b.details()
c.details()
d.details()
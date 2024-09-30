# # Super Keyword in Python

# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# class Faculty (Student):
#     def __init__(self,name,id,course):
#         super().__init__(name,id)
#         self.course = course

# A = Faculty("Anurag", 3794, "Java")
# print(A.name)
# print(A.id)
# print(A.course)




# Magic/Dunder Method in Python
# # __Len__
# class Ajay:
#     def __init__(self,name):
#         self.name = name

#     def __len__(self):
#         l = 0
#         for l in self.name:
#             l +=l
#         return l
    
# a = Ajay("Ajay")
# print(len(a.name))







# # __str__ and __rep__ and __call__
# from Day_22 import Ajay

# a = Ajay("Ajay")
# print(str(a))
# print(repr(a))
# a()








# Overloading in Python
class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id
        self.company_name ="Google"

    def display(self):
        print(f"\nEmployee Name : {self.name}\nEmployee id : {self.id}\nEmployee Company : {self.company_name}")

class Student (Employee):
    def __init__(self,name,id,collage_name):
        super().__init__(name,id)
        self.collage_name = collage_name
    
    def display(self):
        print(f"Student Name : {self.name}\nStudent id : {self.id}\nStudent Collage :{self.collage_name} ")

s = Student("Ajay", 4566, "IIT Roorkee")
s.display()
e = Employee("Sundram", 45)
e.display()
# # Operator Overloading in Python
# class Vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i {self.j}j {self.k}k"
    
#     def __add__(self, a):
#         return Vector(self.i+a.i , self.j+a.j , self.k+a.k)
    
# v1 = Vector(6,3,8)
# print(v1)

# v2 = Vector(2,4,1)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))


# # Single Inheritance in Python
# class Animal:
#     def __init__(self,name,leg):
#         self.name = name
#         self.leg = leg 

#     def animal_sound(self,sound):
#         self.sound = sound
#         print(f"Sound of {self.name} is {self.sound}")

# class Dog(Animal):
#     def __init__(self,name,leg,teeth):
#         Animal.__init__(self,name,leg)
#         self.teeth = teeth

#     def properties(self):
#         print(f"Name of Animal : {self.name}\nLegs : {self.leg}\nTeeth : {self.teeth}")


# d = Dog("Dog",4,"sharp")
# d.properties()
# d.animal_sound("Bark")


# Multiple Inheritance in Python
class Student:
    def __init__(self,name,id,course):
        self.name = name
        self.id = id
        self.course = course

    def details(self):
        print(f"Name of Student : {self.name}\nStudent id : {self.id}\nStudent Course : {self.course}")

class Hobby: 
    def __init__(self,hobby):
        self.hobby = hobby

    def display(self):
        print(f"Hobby is : {self.hobby}")

class Collage(Student, Hobby):
    collage_name = "IIT Roorkee"
    
    def __init__(self,name,id,course,hobby):
       Student.__init__(self,name,id,course)
       Hobby.__init__(self,hobby)

s = Collage("Ajay",453,"BCA","Badminton")
s.details()
s.display()
print(Collage.collage_name)
# # Multilevel Inheritance in Python
# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species  = species

#     def details(self):
#         print(f"Name of Animal : {self.name}\nSpecie of Animal : {self.species}")

# class Dog (Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name , species = "Dog")
#         self.breed = breed

#     def details(self):
#         Animal.details(self)
#         print(f"Breed of Dog : {self.breed}")

# class GoldenRetriver (Dog):
#     def __init__(self,name,colour):
#         Dog.__init__(self,name,breed = "GoldenRetriver")
#         self.colour = colour

#     def details(self):
#         Dog.details(self)
#         print(f"Colour of GoldenRetriver : {self.colour}")

# g = GoldenRetriver("Tommy","Black")
# g.details()


# # Hybrid Inheritance in Python
# class A : 
#     def display(self):
#         print("Inside Class A ")

# class B (A) : 
#     def display(self):
#         A.display(self)
#         print("Inside Class B ")

# class C (A) : 
#     def display(self):
#         A.display(self)
#         print("Inside Class C ")
        
# class D (B,C) : 
#     def display(self):
#         B.display(self)
#         C.display(self)
#         print("Inside Class D ")

# d = D()
# d.display()





# # Hirerical Inheritance in Python
# class BaseClass:
#     def display(self):
#         print("Inside Base Class")

# class Dedrived1(BaseClass):
#     def display(self):
#         BaseClass.display(self)
#         print("Inside Derived1 Class")

# class Dedrived2(BaseClass):
#     def display(self):
#         BaseClass.display(self)
#         print("Inside Derived2 Class")

# class Dedrived3(Dedrived1):
#     def display(self):
#         Dedrived1.display(self)
#         print("Inside Derived3 Class")


# d3 = Dedrived3()
# d3.display()





# # Time Module in Python 
# import time

# init = time.time()
# for i in range(9000):
#     print(i)
# t1 = time.time() - init

# while i < 9000:
#     print(i)
#     i = i+1
# t2 = time.time()- init
# print("Time taken by For Loop",t1)
# print("Time taken by While Loop",t2)


# Time . Sleep
import time
print("Ajay")
time.sleep(3)
print("Time")

t = time.localtime()
format = time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(format)
# # Decorators in Python
# def greet(fun):
#     def decorated_Fx(*args , **kwargs):
#         print("Good Evening")
#         fun(*args , **kwargs)
#         print("Thanks for using \n")
#     return decorated_Fx
# @greet
# def sub(a,b):
#     print(a-b)
# def sum(a,b):
#     print(a+b)

# sub(5,4)
# greet(sum)(2,4)


# # Getter  and  Setter 
# class aj:
#     def __init__(self,a):
#         self.a = a

#     def show(self):
#         print("Value is :",self.a)

#     @property
#     def getter(self):
#         return self.a*2
    
#     @getter.setter
#     def getter(self , a):
#         self.a = a
      

# b = aj(10)
# b.a = 40
# print(b.getter)
# b.show()



# Inhritance 

class Model:
    def __init__(self, id , name):
        self.id = id
        self.name = name
    def show(self):
        print(f"\nName of {self.id} is {self.name}")


class Faculty(Model):
    salary = 10000
    def details(self):
        print(f"Salary is {self.salary}")

m = Model(23, "Rishu")
m.show()

f1 = Faculty(68, "Ritu")
f1.show()
f1.details()
    


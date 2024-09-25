# # Class Methods in python
# class Company:
#     company_name = "Google"
#     def disp(self):
#         print(f"Name of Employee is : {self.name}\nCompany Name : {self.company_name}\n")

#     @classmethod
#     def change(cls, comp_name):
#         cls.company_name = comp_name


# emp1 = Company()
# emp1.name = "Rishi"
# emp1.disp()

# emp2 = Company()
# emp2.name = "Ritik"
# emp2.change("Twitter")
# emp2.disp()
# print(Company.company_name)

# # Class Method as Alternative Constructor
# class Student :
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     @classmethod
#     def modified(self,string):
#         return self(string.split("-")[0], int(string.split("-")[1]))
    
# s1 = Student("Ajay", 23)
# print(s1.name)
# print(s1.id)


# string = "Vishu-34"
# s2 = Student.modified(string)
# print(s2.name)
# print(s2.id)


# # dir() Method in Python
# a = [4,5,2,2]
# print(dir(a))



# # __dict__ Attribute in Python
# class Student:
#     def __init__(self, name, id , fees , course):
#         self.name = name
#         self.id = id
#         self.fees = fees
#         self.course = course

# s = Student("Rajnish", 46, 50000,"BCA")
# print(s.__dict__) 



# help() Method in Python
# class Student:
#     def __init__(self, name, id , fees , course):
#         self.name = name
#         self.id = id
#         self.fees = fees
#         self.course = course

# s = Student("Rajnish", 46, 50000,"BCA")
# print(help(Student)) 


class Ajay:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return (f"This the  {self.name}  Class")
    
    def __repr__(self):
        return (f"This the  {self.name}  Class 'repr'")
    
    def __call__(self):
        print("This __call__ ")

    def __len__(self):
        l = 0
        for l in self.name:
            l +=l
        return l
    
a = Ajay("Ajay")



            
# # There are three Access Modifiers in Python
# # 1. Public Access Modifier (By default)
# class Employee:
#     def __init__(self):
#         self.name = "Ajay"
#         self.age = 19

# obj = Employee()
# print("\nPublic Access Modifier")
# print(obj.name)
# print(obj.age)


# # 2. Private Access Modifier
# # Name Mangling 
# class Employee:
#     def __init__(self):
#         self.__name = "Ajay"
#         self.__age = 19

# obj1 = Employee()
# print("\nPrivate Access Modifier(Name Mangling)")
# print(obj1._Employee__name)
# print(obj1._Employee__age)


# # 3. Protected Access Modifier
# class Employee:
#     def __init__(self):
#         self._name = "Ajay"
#         self._age = 19

# obj2 = Employee()
# print("\nProtected Access Modifier")
# print(obj2._name)
# print(obj2._age)


# # Static Method 
# class Student:
#     def __init__(self):
#         self.firstname = "Ajay"
#         self.middlename = "Pratap Singh"
#         self.lastname = "Sengar"

#     def display(self):
#         print(f"First Name : {self.firstname}\nMiddle Name : {self.middlename}\nLast Name : {self.lastname}")
#     @staticmethod
#     def percentage(marks):
#         return (marks/500)*100
    
# obj3 = Student()
# obj3.display()

# print("\nStatic Method")
# print(Student.percentage(467))




# Instance Variable and Class Variable 
class Company:
    company_name = "Microsoft"
    employee_id = 0

    def __init__(self,name):
        self.name = name
        Company.employee_id += 1

    def display(self):
        print(f"Name of Employee : {self.name}\nEmployee Company Name : {self.company_name}\nEmployee id : {self.employee_id}\n")

emp1 = Company("Rohan")
emp1.display()

emp2 = Company("Shubhi")
Company.company_name = "Google"
emp2.display()

emp3 = Company("Ronak")
emp3.display()

        
        
"""
There are Two Types of Functions in Python
1.Built in Function
2.User Define Function

"""

# print("User Define Function ")
# def evenOdd(n):
#     if(n%2 == 0):
#         print("Number is Even")
#     else:
#         print("Number is Odd")
# evenOdd(5)
# evenOdd(45)
# evenOdd(90)
# evenOdd(67)
# evenOdd(78)
# evenOdd(68)












# print("Return Statement in Function ")
# def cube(n):
#     c = n*n*n
#     return c
# def square(n):
#     s = n*n
#     return s
# c1 = cube(6)
# c2 = cube(5)
# c3 = cube(7)
# c4 = cube(8)
# c5 = cube(9)
# print("Printing Cubes ")
# print("Cube of 6 is",c1)
# print("Cube of 5 is",c2)
# print("Cube of 7 is",c3)
# print("Cube of 8 is",c4)
# print("Cube of 9 is",c5)
# s1 = square(6)
# s2 = square(7)
# s3 = square(8)
# s4 = square(9)
# s5 = square(10)
# print("Printing Squares ")
# print("Square of 6 is ",s1)
# print("Square of 7 is ",s2)
# print("Square of 8 is ",s3)
# print("Square of 9 is ",s4)
# print("Square of 10 is ",s5)



"""
Types of Python Function Arguments
1.Default argument
2.Keyword arguments 
3.Positional arguments
4.Arbitrary arguments 

"""


print("Default Argument")
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)

print("\nKeyword Arguments")
def student(firstname, lastname):
    print(firstname, lastname)
student(firstname='Ajay', lastname='Sengar')
student(lastname='Sengar', firstname='Ajay')

print("\nPositianal Arguments")
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
print("Case-1:")
nameAge("Ajay", 19)
print("\nCase-2:")
nameAge(19, "Ajay")

print("\nArbitrary arguments")
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'Ajay Code')

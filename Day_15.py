# # How importing works in Python
# import math
# print("\nImporting 'Math' Library")
# print("Using sqrt : ",math.sqrt(9))
# print("Using floor : ",math.floor(3.675))
# print("Using sin : ",math.sin(0))
# print("Using cos : ",math.cos(0))

# # Use of from keyword in Python
# # It bring specific function from that library
# from math import pi
# print("\nUsing of 'from' Keyword")
# area = pi * (5**2)
# print("\nArea of Circle : ",area)

# # Use of * 
# from math import*
# print("Using of '*' ")
# print("\nIt Brings all functions of that library")
# print("Using Pow : ",math.log(5))

# Use of as keyword in Pyhton
import math as m
print("Using of 'as' Keyword ")
print("Using log : ",m.log(2))

# Using dir in Python 
# it prints all methods that are present in that library
import math
print("\nUsing of 'dir' Keyword")
print(dir(math))

# Importing my files method 
import ajay as a 
print("\nImporting my file and using its method")
a.greeting()
print(a.aj)


# # Importing Vishu 
# import Vishu as v
# print("\nImproting 'Vishu'")
# print(__name__)
# v.sum(10,45)
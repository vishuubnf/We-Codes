# # F-String in Python
# name = input("Enter Your Name : ")
# country = input("Enter Your Country : ")
# print(f"Hey my name is {name} and I am from {country}")
# course = "BCA"
# print("\nWithout f-String ")
# sample ="I pursuing {}  "
# print(sample.format(course))

















# # Doc String in Python
# def sum(a,b):
#     '''
# This Function Takes Two Variable as input
# and Calculate them and return Sum
#     '''
#     return (a+b)
# a = int(input("Enter First Integer Value : "))
# b = int(input("Enter Second Integer Value : "))
# s =sum(a,b)
# print("Sum is : ",s)
# print(sum.__doc__)














# PEP 8 in Python
# The Zen of Python
# import this












# Recursion in Python
# def fib(n):
#     if(n==0 ):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))

# n =int(input("Enter the Integer Value :"))
# print("Printing Fibonaci :",fib(n))
    

















import time
t = time.strftime('%H: %M: %S')
print("Time Zone Of India")
print(t)
h = int(time.strftime('%H'))
print("\nPrint Greeting According to Time")
print("Time :",h)
if(h>=0 and h<12):
    print("Good Morning Sir")
elif(h>=12 and h<16):
    print("Good Afternoon Sir")
elif(h>=16 and h<19):
    print("Good Evening Sir")
else:
    print("Good Night Sir")
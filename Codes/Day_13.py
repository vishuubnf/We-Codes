# # Using of Short Hand if else 
# # It Basically reduces the line of codes but not efficient to read 
# # We use only in simple programms 

# a = int(input("Enter Integer Value : "))
# print("Even") if(a%2 == 0) else print("Odd")

# # Second 
# a = int(input("\nEnter Integer Value : "))
# b = int(input("Enter Integer Value : "))
# print("A is greater") if(a>b) else print("Both equal") if(a == b) else print("B is greater")

# # Third
# print("\nGive Result in Boolean")
# a = int(input("Enter Integer Value : "))
# res = 1 if(a%2 == 0) else 0
# print(res)







# Without using Enumeraion in Python
print("\nWithout using Enumeraion in Python")
marks = [83,93,94,85,47,24,99,80]
index = 0
for mark in marks:
    if(mark > 80):
        print("Performance is Good")
        print(mark)
index = index +1 

# Using Enumeraion in Python
print("\nUsing Enumeraion in Python")
marks = [83,93,94,85,47,24,99,80]
for index, mark in enumerate(marks):
    if(mark > 80):
        print("Performance is Good")
        print(mark)

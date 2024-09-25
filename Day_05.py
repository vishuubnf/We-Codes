"""
There are two Loops in Python
1. For Loop
2. While Loop

Syntax of For Loop
for iterator_var in sequence:
    statements(s)

Syntax of While Loop
while expression:
    statement(s)

"""


# For Loop Program in Python
# print("Printing Table ")
# t = int(input("Enter Number : "))
# for i in range(1,11):
#     print(i,"*",t, " = ", i*t)









# Printing String , Tuple , List , Dictionary , Set Elements 
# print("List Iteration")
# l = ["Ajay", "Pratap", "Singh" , "Sengar"]
# for i in l:
#     print(i)
# print("\nTuple Iteration")
# t = ("Ajay", "Pratap", "Singh", "Sengar")
# for i in t:
#     print(i)
# print("\nString Iteration")
# s = "Ajay"
# for i in s:
#     print(i)
# print("\nDictionary Iteration")
# d = dict()
# d['Ajay'] = 23120193
# d['Vishu'] = 23120194
# for i in d:
#     print("%s  %d" % (i, d[i]))
# print("\nSet Iteration")
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i),






# While Loop in Python
# print("\nPrinting Numbers ")
# i = 0
# while(i<11):
#     print(i)
#     i = i+1

















    


'''
Syntax of While Loop with Else Statement
while condition:
     # execute these statements
else:
     # execute these statements
'''

# print("Printing Greeting ")
# i=0
# while(i<5):
#     print("Good Morning")
#     i=i+1
# else:
#     print("Inside the else block")














# Using Break and Continue in For Loop with Else Statemnet
for i in range(1,11):
    if(i==8):
        print("Break Statement Hit")
        break
    if(i==5):
        print("Continue Statement Hit")
        continue
    print(i)
else:
    print("Code Run Successfuly")
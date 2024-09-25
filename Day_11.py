# # Using else with for loop
# for i in range(5):
#     print(i)
# else:
#     print("For Loop is Over and Else is Running\n")






# # Now One in For Loop Twist
# # If i use beak in loop then the program will successfuly compleated so it will not move to else statement
# for i in range(5):
#     print("Iteratrion No {} Printed".format(i+1))
#     if(i == 2):
#         break
# else:
#     print("For Loop is Over and Else is Running")




# # Using try and except to handel errors
# # Exception Handling
# a = input("Enter the value :")
# print("Multipliction of {} ".format(a))
# try:
#     for i in range(1,11):
#         print("{} X {} = {}".format(int(a),i,int(a)*i))
# except:
#     print("Invalid Input!")
#     print("Please Try Again")













# Using Multiple Errors 
a = input("Enter the index :")
try:
    l = [3,5,7,9,2,5]
    print(l[int(a)])
except ValueError:
    print("Invalid Input!")
    print("Please Try Again")
except IndexError:
    print("Index Not Found!")
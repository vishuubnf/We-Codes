# # if else statement in Python
# a = int(input("Enter the Nunber : "))
# if(a > 0):
#     print("Number is Positive")
# else:
#     print("Number is Negative")





# # if else statement in Python
# print("\n\nCommand of Alexa ")
# budget = int(input("Alexa : Enter Your Budget : "))
# apple = 120
# print("Apple Price : ",apple)
# if(budget > apple):
#     print("Alexa : 1kg Apple Added in your cart ")
# else:
#     print("Alexa : Your Budget is not Sufficient to buy Apple")


 

# # elif statement in Python
# print("\n\nProgram of Children | Teenager | Adult")
# age = int(input("Enter Your Age : "))
# if(age < 13):
#     print("Children ")
# elif(age >= 13 and age < 18):
#     print("Teenager")
# else:
#     print("Adult")    



# # Greeting Programm
# time = int(input("Enter Railway Time : "))
# if(time >= 5 and time < 12):
#     print("Good Morning Sir")
# elif(time >= 12 and time <= 18):
#     print("Good Afternoon Sir")
# else:
#     print("Good Evening Sir")



# Match Case in Python
print("Voter Machine Program")
vote= int(input("Press 1 : To Vote BJP\nPress 2 : To Vote Congress\nPress 3 : To Vote Sapa\nPress 4 : To Vote BSP\n"))
match vote:
    case 1 :
        print("Congratulations You Voted to BJP")
    case 2 :
        print("Congratulations You Voted to Congress")
    case 3 :
        print("Congratulations You Voted to Sapa")
    case 4 :
        print("Congratulations You Voted to BSP")
    case _ :
        print("Invalid Press Again")

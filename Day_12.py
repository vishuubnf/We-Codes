# # Using of Finally Keyword in Python
# # Finally is used to give a Error Message
# # It always runs irespetive of any thing 
# # Lets explore it 
# def f():
#     try:
#         l =[3,6,2,6,8]
#         a= input("Enter the index :")
#         print(l[int(a)])
#         return 1
#     except:
#         print("Index out of bound!")
#         return 0
#     finally:
#         print("I always run!")
# x = f()
# print(x)





# # Raising Coustum Errors in Python
# # We can raise coustom errors 
# a = input("Enter Value Between 10 and 20 ")
# if(int(a)<10 or int(a)>20):
#     raise ValueError("Value is out of bound")
# else:
#     print(a)









#KBC game in Python
questions = [
[
"Who is the founder of  C Language ? ","Denis Ritchi","Raman Rao","Pranav Raman","Van o Guido",1
],
[
"Current Railway Minister of India is ","Mamta Banarjee","Ram Vilash","Ashwini Vaishnaw", "Piyush Goyal",3
],[
"Which god is also known as Gauri Nandan?","Agni","Indra","Hanuman","Ganesha",4
],[
"What does not grow on tree according to a popular Hindi saying","Money","Flowers","Leaves","Fruits",1
],[
"Which city is known as the Pink City of India?","Banglore","Maysore","Jaipur","Kochi",3
],[
"Who wrote India's National Anthem?","Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan",1
],[
"How many major religions are there in India?",6,7,8,9,1
],
]

levels  =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1280000,2560000,5120000]

i=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"Question {i+1} {questions[i]}")
    print(f"a{question[1]}                 b.{question[2]}")   
    print(f"a{question[3]}                 b.{question[4]}\n\n")   
 
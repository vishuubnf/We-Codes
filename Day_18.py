# What is lamda function 
# Its is a small anonymous function without name

# cube = lambda a : a*a*a
# print(cube(2))

# # We can paas function to fuction 

# def result(average , s):
#     return average*s
# average = lambda x, y, z : (x+y+z)/3
# print(result(average(2,3,4),100))

# # Using lambda
# def result(average , s):
#     return average(2,3,4)*s
# print(result(lambda x, y, z : (x+y+z)/3,100))


# # MAP
# print("\nUsing Map Function")
# def square(a):
#     return a*a 
# l = [2,4,5,7,8]
# print(list(map(square,l)))

# # MAP WITH LAMBDA
# print("\nUsing Map Function with Lambda")
# print(list(map(lambda a: a*a,l)))

# # FILTER 
# print("\nUsing Filter Function")
# def even(a):
#     return a%2 == 0
# l = [2,4,5,7,8]
# print(list(filter(even,l)))

# # FILTER WITH LAMBDA
# print("\nUsing Filter Function with Lambda")
# l = [2,4,5,7,8]
# print(list(filter(lambda a: a%2 == 0,l)))

# # REDUCE 
# from functools import reduce
# print("\nUsing Reduce Function")
# l = [2,4,5,7,8]
# def sum(a,b):
#     return a+b
# print((reduce(sum,l)))


# 'is' vs '=='
print("\nList a 'is' vs '==' b")
a = [2,3,4]
b = [2,3,4]
print(a is b)
print(a == b)

print("\nTuple a 'is' vs '==' b")
a = (2,3,4)
b = (2,3,4)
print(a is b)
print(a == b)
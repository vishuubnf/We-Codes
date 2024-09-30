# # Sets in Python
# # In Set Repeated Values are not displayed
# a = {2,4,4,5,6,7,8,9,10}
# print("Set : ",a)

# # Set can cointain different type of data
# p = {"Ajay",3,'J',3.14,True,5,7,8,9}
# print("Set :",p)

# # Printing Set Elements using for loop
# r = {"Ajay","Sengar",'G',4,6,7.6}
# for value in r :
#     print("Set :",value)












# # Set Theory Operations 
# s1 = {"Ajay","Sengar",'G',4,6,7.6}
# s2 = {3,5,"Sengar",}
# res = s1.union(s2)
# print("Union of Sets :",res)
# s1.update(s2)
# print("Updated Set1 :",s1)

# s1 = {"Ajay","Sengar",'G',4,6,7.6}
# s2 = {3,5,"Sengar",}
# res = s1.intersection(s2)
# print("\nIntersection of Sets :",res)
# s1.intersection_update(s2)
# print("Updated Set1 :",s1)









# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s2 = {3,5,"Sengar",}
# res = s1.symmetric_difference(s2)
# print("\nSymmetric Difference of Sets :",res)
# s1.symmetric_difference_update(s2)
# print("Updated Set1 :",s1)

# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s2 = {3,5,"Sengar",}
# res = s1.difference(s2)
# print("\nDifference of Sets :",res)
# s1.difference_update(s2)
# print("Updated Set1 :",s1)









# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s2 = {3,5,"Sengar",}
# res = s1.isdisjoint(s2)
# print("\nIs Disjoint Sets :",res)

# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s2 = {3,"Sengar",}
# res = s1.issuperset(s2)
# print("\nIs Super Sets :",res)

# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s2 = {3,"Sengar",}
# res = s2.issubset(s1)
# print("\nIs Subset Sets :",res)

# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s1.add("Singh")
# print("\nAdded Set :",s1)







# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s1.remove("Sengar")
# print("\nRemoved Set :",s1)

# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# s1.discard("Singh")
# print("\nDiscard Set :",s1)

# s1 = {"Ajay","Sengar",'G',3,6,7.6}
# item =s1.pop()
# print("\nPoped Set :",s1)
# print(item)

s1 = {"Ajay","Sengar",'G',3,6,7.6}
del s1

s1 = {"Ajay","Sengar",'G',3,6,7.6}
s1.clear()
print("\nCleared Set :",s1)

s1 = {"Ajay","Sengar",'G',3,6,7.6}
if "Sengar" in s1:
    print("\nSengar is Present in Set")
else:
    print("\nSengar is not Present in Set")
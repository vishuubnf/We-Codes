# Dictionary in Python
# a = {"Name": "Ajay", "Age": 19 , "Eligibility":True}
# print("Printing Dictionary ")
# print(a)
# print(type(a))

# print("\nPrinting Key of Dictionary ")
# print(a.keys())

# print("\nPrinting Values of Dictionary ")
# print(a.values())
# print(a["Name"])
# print(a["Age"])
# print(a["Eligibility"])

# print("\nPrinting Values of Dictionary Using get()")
# print(a.get("Name"))
# print(a.get("Age"))
# print(a.get("Eligibility"))





# print("\nPrinting Values Using Loop")
# for value in a:
#     print(a[value])

# print("\nPrinting Items of Dictionary")
# print(a.items())

# print("\nPrinting items of Dictionary usig Loop")
# for keys,value in a.items():
#     print(f"The {keys} is {value}")









print("Using Dictionary Methods")
# print("\nUpdate Method ")
ep = {"Ritik":123, "Rohan":145, "Ram":453}
ep1 = {"Nilesh":435, "Shyam":473}
# print(ep)
# print(ep1)
# ep.update(ep1)
# print(ep)

# print("\nUsing Pop Method ")
# ep.pop("Ritik")
# print(ep)

# print("\nUsing Pop Item Method ")
# ep.popitem()
# print(ep)







print("\nUsing Del Method ")
del ep["Ram"]
print(ep)
del ep

print("\nUsing Clear Method")
ep.clear() # This will throw error



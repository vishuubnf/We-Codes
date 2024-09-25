# FILE HANDELING

# # Reading File
# f = open('aj.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# Writing File
# f = open('aj2.txt', 'w')
# f.write('Hello')
# f.close()

# Appending File
# f = open('aj.txt', 'a')
# f.write('Hello')
# f.close()

# # Appending File 'with'
# with open('aj.txt', 'a')as f:
#     f.write('Hey How are you')



# ReadLine Method
# f = open('aj2.txt', 'r')
# i =  0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of Student {i} in Maths {m1}")
#     print(f"Marks of Student {i} in Maths {m2}")
#     print(f"Marks of Student {i} in Maths {m3}")
#     print(line)

# Write Line Method
# f = open('aj3.txt','w')
# line = ['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n']
# f.writelines(line)
# f.close()

# Seek and Tell Method 
# f = open('aj3.txt', 'r')
# f.seek(2)
# print(f.tell())
# data = f.read(5)
# print(data)


# Truncate Method
with open('aj.txt', 'w') as f:
    f.write("Hey How Are You")
    f.truncate(6)
with open('aj.txt', 'r') as f:
    print(f.read())

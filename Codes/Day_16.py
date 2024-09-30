# import os
# print("Creating Folders")
# for folder in range(0,30):
#     os.mkdir(f"{folder+1}. Day")







import os
print("Removing Folders")
for folder in range(0,30):
    os.rmdir(f"{folder+1}. Test")

# import os
# print("Renaming Folders")
# for folder in range(0,30):
#     os.rename(f"{folder+1}. Day", f"{folder+1}. Test")


# Local Variable || Global Variable
# How to change Global Variable

a = 10    # Global Variable
print("Global Variable ",a)

def fun():
    b = 20 # Local Variable
    print("Local Variable ", b)
    global a 
    a = 25

fun()
print("Changed Global Variable ",a)



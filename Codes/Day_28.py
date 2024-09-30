# # Function Caching 
# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def fun(a):
#     time.sleep(3)
#     return a*a

# print(fun(4))
# print("Run for 4")
# print(fun(6))
# print("Run for 6")
# print(fun(8))
# print("Run for 8")

# print(fun(4))
# print("Run for 4")
# print(fun(6))
# print("Run for 6")
# print(fun(8))
# print("Run for 8")


# Regular Expression in Python
import re

pattern = r"[A-Z]jay"
text = """
 Ghost of Tsushima DIRECTOR'S CUT
 
 Ajay 
 Build
 Windows
 Distribution platform
 Game directory
 Working directory
 Run ID
 Djay
 Memory statistics
   Total RAM 
  Avail RAM 
   Total virtual memory 
   Avail virtual memory 
   Total page file 
   Avail page file 
 Raja Initializing Successfully initialized Currently connected to 0 remote sessions
 End previously existing file batch, did the game quit abnormally while saving PreInit
Ajay


"""

# match = re.search(pattern , text)
# print(match)

match = re.finditer(pattern,text)
for matches in match:
    print(matches.span())

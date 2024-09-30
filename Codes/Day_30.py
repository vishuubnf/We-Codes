# Multitreading in Python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def fun(sec):
    print(f"Time taken to run this code {sec} seconds")
    time.sleep(sec)
time1 = time.perf_counter()
# Normal Method
fun(1)
fun(2)
fun(3)
time2 = time.perf_counter()
print("Time Taken by Normal Method : ",time2 - time1)
print("\n")

time3 = time.perf_counter()
# Using Threading
t1 = threading.Thread(target = fun, args = [1])
t2 = threading.Thread(target = fun, args = [2])
t3 = threading.Thread(target = fun, args = [3])
t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()
time4 = time.perf_counter()
print("Time Taken by Threaded Method : ",time4 - time3)
print("\n")

def ThreadPool():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(fun, 1)
        future2 = executor.submit(fun, 2)
        future3 = executor.submit(fun, 3)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        print("\n")

        l = [3,5,6,7,1]
        results = executor.map(fun,l)
        for result in results:
            print(result)
ThreadPool()
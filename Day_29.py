# Asyncio in Python
import time
import asyncio
from urllib import response
# import requests


async def funtion1():
    await asyncio.sleep(1)
    print("func 1")
async def funtion2():
    await asyncio.sleep(2)
    print("func 2")
async def funtion3():
    await asyncio.sleep(1)
    print("func 3")

async def main():
    L = await asyncio.gather(
        funtion1(),
        funtion2(),
        funtion3()
    )
    print(L)
#     task = asyncio.create_task(funtion1())
#     await funtion2()
#     await funtion3()

asyncio.run(main())



import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")
    return "Result 1"


async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")
    return "Result 2"


# async def main():
#     results = await asyncio.gather(
#         task1(),
#         task2()
#     )
#     print(type(results))

async def main():
    result1 = await task1()
    result2 = await task2()
    
    print([result1, result2])    


asyncio.run(main())
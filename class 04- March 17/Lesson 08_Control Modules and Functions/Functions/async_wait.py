import asyncio
async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("Bye!")


asyncio.run(say_hello())
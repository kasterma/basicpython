import asyncio
from contextvars import ContextVar

cv = ContextVar("cv")

async def ff(x):
    v = cv.get(666)
    print(f"f({x}) -> {v}")
    cv.set(11)

async def f():
    while True:
        await ff(" f ")
        await asyncio.sleep(1)

async def gg(x):
    v = cv.get(555)
    print(f"g({x}) -> {v}")
    cv.set(22)


async def g():
    while True:
        await ff("g")
        await gg("g")
        await asyncio.sleep(0.4)

async def main():
    ff = asyncio.create_task(f())
    gg = asyncio.create_task(g())
    #ff = asyncio.Task(f())
    #gg = asyncio.Task(g())
    #await asyncio.gather(ff, gg)
    await asyncio.sleep(20)

if __name__ == "__main__":
    asyncio.run(main())

import logging
import sys
import asyncio
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger("ex2")


class LoggingLock(asyncio.Lock):
    async def acquire(self):
        log.info("Getting lock")
        await super().acquire()
        log.info("Have lock")

    def release(self):
        super().release()
        log.info("Released")


async def f(lock, label, n=10):
    for i in range(n):
        async with lock:
            log.info(f"{label}({i}):{time.monotonic()}")
            await asyncio.sleep(0.5)


async def main():
    lock_0 = LoggingLock()
    f0 = asyncio.create_task(f(lock_0, "one"))
    f1 = asyncio.create_task(f(lock_0, "two"))

    await asyncio.gather(f0, f1)


asyncio.run(main())

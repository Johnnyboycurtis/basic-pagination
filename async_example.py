import asyncio
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from random import randint
from pagination import models

async def task(i):
    x = randint(0, 10)
    pid = os.getpid()
    print("{}. (PID: {}) sleeping for {} seconds".format(i, pid, x))
    await asyncio.sleep(x)
    print("{}. (PID: {}) slept for {} seconds".format(i, pid, x))
    instance = models.Example(iteration = i, pid = pid, randint = x)
    instance.save()
    return (i, pid, x)


async def main():
    results = []
    for i in range(10):
        try:
            out = await asyncio.wait_for(task(i), timeout=5)
            results.append(out)
        except asyncio.TimeoutError:
            print("timeout!!")
    
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
#!/usr/bin/env python3
'''Write an asynchronous coroutine that takes in an integer argument
'''

import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    delays = await asyncio.gather(wait_random(), wait_random(5), wait_random(20))
    print("Random Delays:", delays)


asyncio.run(main())


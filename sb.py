import asyncio
import random
import sys

from seleniumbase import SB


sys.argv.append("-n")


async def main():
    asyncio.create_task(start())
    asyncio.create_task(start())


async def start():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sb_start)


def sb_start():
    with SB(test=True, uc=True, xvfb=True, port=str(random.randint(0, 9999))) as sb:
        sb.uc_open_with_reconnect("https://google.com")
        sb.wait(5)
        sb.save_screenshot(name=f"{random.randint(0, 1000)}.png")


asyncio.run(main())

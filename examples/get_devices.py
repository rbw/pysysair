import asyncio

from pysysair import SystemairClient


async def main():
    client = SystemairClient()
    async for device in client.get_devices():
        print(device)


asyncio.run(main())

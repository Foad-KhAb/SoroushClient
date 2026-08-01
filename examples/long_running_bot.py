import asyncio

from soroushclient.client.base import SoroushClient


async def main():
    client = SoroushClient(session_file="example.json")

    @client.on_update
    async def handler(update):
        print("Got update:", update)

    await client.start(run_in_background=True)

    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await client.stop()


asyncio.run(main())

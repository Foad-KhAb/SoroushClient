import asyncio

from soroushclient.client.base import SoroushClient


async def main():
    client = SoroushClient(session_file="example.json")

    async with client:
        dialogs = await client.get_all_dialogs()
        for entry in dialogs:
            print(entry["dialog"], "->", entry["input_peer"])


asyncio.run(main())

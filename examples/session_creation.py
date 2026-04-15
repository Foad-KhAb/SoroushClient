import asyncio

from soroushclient.client.base import SoroushClient


async def main():
    session_file = "example.json"
    s = SoroushClient(session_file=session_file)
    await s.start_phone_auth()
    print("session created!")
asyncio.run(main())



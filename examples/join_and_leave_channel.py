import asyncio

from soroushclient.client.base import SoroushClient
from soroushclient.tl.generated import InputChannel


async def main():
    client = SoroushClient(session_file="example.json")

    async with client:
        # Join via an invite link (accepts full URL, bare path, or raw hash)
        await client.join_by_link("https://splus.ir/joingroup/ABC123")

        # Replace with a real channel id/access_hash, e.g. from client.resolve_username()
        channel = InputChannel(channel_id=123456, access_hash=0)

        full = await client.get_full_channel(channel)
        print(full)

        await client.leave_channel(channel)


asyncio.run(main())

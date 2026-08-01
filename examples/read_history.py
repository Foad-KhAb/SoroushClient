import asyncio

from soroushclient.client.base import SoroushClient
from soroushclient.tl.generated import InputPeerChannel


async def main():
    client = SoroushClient(session_file="example.json")

    async with client:
        # Replace with a real channel id/access_hash, e.g. from client.resolve_username()
        peer = InputPeerChannel(channel_id=123456, access_hash=0)

        history = await client.get_history(peer=peer, limit=20)
        for message in history.messages:
            print(message.id, getattr(message, "message", ""))


asyncio.run(main())

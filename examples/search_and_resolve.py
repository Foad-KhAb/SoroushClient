import asyncio

from soroushclient.client.base import SoroushClient
from soroushclient.tl.generated import PeerChannel, PeerUser


async def main():
    client = SoroushClient(session_file="example.json")

    async with client:
        found = await client.search("soroush", limit=10)

        users_by_id = {u.id: u for u in found.users}
        chats_by_id = {c.id: c for c in found.chats}

        for peer in found.results:
            if isinstance(peer, PeerUser):
                print("user:", users_by_id[peer.user_id])
            elif isinstance(peer, PeerChannel):
                print("channel:", chats_by_id[peer.channel_id])

        resolved = await client.resolve_username("soroush")
        print("resolved peer:", resolved.peer)


asyncio.run(main())

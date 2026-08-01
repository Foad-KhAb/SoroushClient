# SoroushClient

An async MTProto client for [Soroush Plus](https://splus.ir), written in pure Python.

## Features

- Async, websocket-based MTProto transport with automatic reconnect
- Phone number login (send/verify OTP), including an interactive CLI flow
- Dialogs, chats, channels, and message history
- Persistent session storage to a local JSON file
- Update handlers for receiving realtime events

## Installation

```bash
pip install soroushclient
```

Requires Python 3.11+.

## Quickstart

```python
import asyncio
from soroushclient import SoroushClient


async def main():
    client = SoroushClient(api_id=YOUR_API_ID, api_hash="YOUR_API_HASH")

    async with client:
        await client.send_code("989xxxxxxxxx")
        code = input("Enter the code you received: ")
        await client.sign_in(code)

        dialogs = await client.get_dialogs()
        print(dialogs)


asyncio.run(main())
```

Once signed in, the session is saved to `soroush.json` (configurable via
`session_file=`) so subsequent runs skip the login step.

### Interactive phone login

```python
import asyncio
from soroushclient import SoroushClient


async def main():
    client = SoroushClient()
    await client.start_phone_auth()  # prompts for phone number and OTP on stdin
    print("session created!")


asyncio.run(main())
```

See [`examples/session_creation.py`](examples/session_creation.py) for a
minimal runnable script.

## Long-running clients

`SoroushClient` can also run in the background with an update handler and
automatic reconnect:

```python
client = SoroushClient()

@client.on_update
async def handler(update):
    print("Got update:", update)

await client.start(run_in_background=True)
```

## Development

```bash
pip install -e .
pre-commit install
```

Linting/formatting is handled by `ruff`, `black`, and `isort` via
`pre-commit` (see `.pre-commit-config.yaml`).

## License

MIT — see [LICENSE](LICENSE).

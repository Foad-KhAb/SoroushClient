<div align="center">

# SoroushClient 🚀

**An async MTProto client for [Soroush Plus](https://splus.ir), written in pure Python**

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.21-blue)](https://pypi.org/project/soroushclient/)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](pyproject.toml)
[![Transport](https://img.shields.io/badge/transport-WebSocket%20%7C%20MTProto-informational)](soroushclient/network)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**[English](README.md)** | **[فارسی](README.fa.md)**

</div>

> **Important**
> This is an unofficial, third-party MTProto client for Soroush Plus. It is not
> affiliated with or endorsed by SPlusThon. Respect Soroush Plus's terms of
> service and rate limits, keep your `api_hash`/session files private, and
> never commit them to source control.

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

## More examples

The [`examples/`](examples) directory has runnable scripts for common tasks:

| Script | What it shows |
| --- | --- |
| [`session_creation.py`](examples/session_creation.py) | Interactive phone login, creating a session file |
| [`list_dialogs.py`](examples/list_dialogs.py) | Fetching all dialogs (chats/channels/users) |
| [`read_history.py`](examples/read_history.py) | Reading message history from a channel |
| [`search_and_resolve.py`](examples/search_and_resolve.py) | Global search and resolving a `@username` |
| [`join_and_leave_channel.py`](examples/join_and_leave_channel.py) | Joining via invite link, fetching full channel info, leaving |
| [`long_running_bot.py`](examples/long_running_bot.py) | Running in the background with an update handler |

Each script expects an existing session file (`example.json`, created by
`session_creation.py`) and placeholder channel/user IDs — replace those with
real values from `search()` or `resolve_username()`.

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

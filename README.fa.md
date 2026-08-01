<div align="center">

# SoroushClient 🚀

**کتابخانه‌ی ناهمگام (async) پایتون برای MTProto سروش‌پلاس، به‌صورت pure Python**

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.21-blue)](https://pypi.org/project/soroushclient/)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](pyproject.toml)
[![Transport](https://img.shields.io/badge/transport-WebSocket%20%7C%20MTProto-informational)](soroushclient/network)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**[English](README.md)** | **[فارسی](README.fa.md)**

</div>

> **نکته مهم**
> این کتابخانه یک کلاینت غیررسمی و شخص‌ثالث برای MTProto سروش‌پلاس است و
> هیچ ارتباطی با SPlusThon ندارد. قوانین و محدودیت‌های سروش‌پلاس را رعایت
> کنید، `api_hash` و فایل‌های session را محرمانه نگه دارید و هرگز آن‌ها را
> در گیت/سورس‌کنترل منتشر نکنید.

## امکانات

- ترابری (transport) ناهمگام مبتنی بر WebSocket برای MTProto، با اتصال مجدد خودکار
- ورود با شماره تلفن (ارسال/تأیید کد یک‌بارمصرف)، همراه با یک روند تعاملی در خط فرمان
- دسترسی به دیالوگ‌ها، چت‌ها، کانال‌ها و تاریخچه پیام‌ها
- ذخیره‌سازی پایدار session در یک فایل JSON محلی
- هندلرهای دریافت رویداد برای آپدیت‌های بلادرنگ (realtime)

## نصب

```bash
pip install soroushclient
```

نیازمند پایتون نسخه 3.11 یا بالاتر است.

## شروع سریع

```python
import asyncio
from soroushclient import SoroushClient


async def main():
    client = SoroushClient(api_id=YOUR_API_ID, api_hash="YOUR_API_HASH")

    async with client:
        await client.send_code("989xxxxxxxxx")
        code = input("کد دریافتی را وارد کنید: ")
        await client.sign_in(code)

        dialogs = await client.get_dialogs()
        print(dialogs)


asyncio.run(main())
```

پس از ورود موفق، session در فایل `soroush.json` ذخیره می‌شود (قابل تنظیم
با پارامتر `session_file=`) تا در اجراهای بعدی نیازی به ورود مجدد نباشد.

### ورود تعاملی با شماره تلفن

```python
import asyncio
from soroushclient import SoroushClient


async def main():
    client = SoroushClient()
    await client.start_phone_auth()  # شماره تلفن و کد را از ورودی می‌گیرد
    print("session created!")


asyncio.run(main())
```

فایل [`examples/session_creation.py`](examples/session_creation.py) یک
اسکریپت آماده و کوچک برای همین منظور است.

## نمونه‌کدهای بیشتر

پوشه‌ی [`examples/`](examples) شامل اسکریپت‌های آماده برای کارهای رایج است:

| اسکریپت | کاربرد |
| --- | --- |
| [`session_creation.py`](examples/session_creation.py) | ورود تعاملی با شماره تلفن و ساخت فایل session |
| [`list_dialogs.py`](examples/list_dialogs.py) | دریافت تمام دیالوگ‌ها (چت/کانال/کاربر) |
| [`read_history.py`](examples/read_history.py) | خواندن تاریخچه پیام‌های یک کانال |
| [`search_and_resolve.py`](examples/search_and_resolve.py) | جست‌وجوی سراسری و resolve کردن `@username` |
| [`join_and_leave_channel.py`](examples/join_and_leave_channel.py) | عضویت با لینک دعوت، دریافت اطلاعات کامل کانال، خروج |
| [`long_running_bot.py`](examples/long_running_bot.py) | اجرا در پس‌زمینه همراه با هندلر آپدیت |

هر اسکریپت به یک فایل session موجود (`example.json`، ساخته‌شده توسط
`session_creation.py`) و شناسه‌های نمونه برای کانال/کاربر نیاز دارد —
این مقادیر را با مقادیر واقعی از `search()` یا `resolve_username()`
جایگزین کنید.

## کلاینت‌های دائمی (long-running)

`SoroushClient` می‌تواند در پس‌زمینه و همراه با یک هندلر آپدیت و اتصال
مجدد خودکار اجرا شود:

```python
client = SoroushClient()

@client.on_update
async def handler(update):
    print("Got update:", update)

await client.start(run_in_background=True)
```

## توسعه

```bash
pip install -e .
pre-commit install
```

لینت و فرمت کد با `ruff`، `black` و `isort` از طریق `pre-commit` انجام
می‌شود (به فایل `.pre-commit-config.yaml` نگاه کنید).

## مجوز

MIT — فایل [LICENSE](LICENSE) را ببینید.

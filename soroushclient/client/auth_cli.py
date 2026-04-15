from __future__ import annotations

import asyncio
import time
from typing import TYPE_CHECKING

from colorama import Fore
from soroushclient.errors.base import RpcError

if TYPE_CHECKING:
    from soroushclient.client.base import SoroushClient


class PhoneLoginCLI:
    """
    CLI for phone-based login using soroushclient.
    Default UI language is English.
    If the user types 'fin', all subsequent messages are shown using the provided
    Fingilish (fa) strings. If the user types 'en', UI returns to English strings.
    """

    def __init__(self, client: SoroushClient):
        self.client = client
        self.fingilish_mode = False  # off by default

    # ---------------------------
    # Output & input helpers
    # ---------------------------
    def _print(self, en: str, fa: str, color=Fore.WHITE):
        msg = fa if self.fingilish_mode else en
        print(color + msg)

    def _input(self, en_prompt: str, fa_prompt: str, color=Fore.WHITE) -> str:
        prompt = fa_prompt if self.fingilish_mode else en_prompt
        return input(color + prompt)

    # ---------------------------
    # Flow
    # ---------------------------
    async def start(self):
        while True:
            phone_number = await self._request_phone_number()
            resp = await self._send_login_request(phone_number)
            if not resp:
                continue
            success = await self._handle_code_entry(resp)
            if success:
                break

    async def _request_phone_number(self):
        # Explain both in EN (default) and FA (for fin mode)
        self._print(
            "📱 Enter your phone number in international format:\n"
            "   Example for Iran: 98XXXXXXXXXX (without the + sign)\n"
            "   Type 'fin' anytime to switch to Fingilish\n",
            "📱 Shomare telefon ro be format beynolmelali vared kon:\n"
            "   Mesal baraye Iran: 98XXXXXXXXXX (bedone +)\n"
            "   Agar mikhay zaban en beshe bezan: en\n",
            Fore.CYAN,
        )
        while True:
            raw = self._input("Phone number: ", "Shomare: ", Fore.YELLOW)
            raw = raw.replace("+", "").strip()

            low = raw.lower()
            if low == "fin":
                self.fingilish_mode = True
                self._print(
                    "✅ Fingilish mode ON.\n",
                    "✅ Halat Fingilish fa'al shod.\n",
                    Fore.GREEN,
                )
                continue
            if low == "en":
                self.fingilish_mode = False
                self._print(
                    "✅ English mode ON.\n",
                    "✅ Halat English fa'al shod.\n",
                    Fore.GREEN,
                )
                continue

            if raw.isdigit():
                return str(raw)

            self._print(
                "❌ Invalid phone number format. Please check and try again.\n",
                "❌ Format shomare dorost nist. Check kon va dobare emtehan kon.\n",
                Fore.MAGENTA,
            )

    async def _send_login_request(
        self,
        phone_number,
    ):
        try:
            resp = await self.client.send_code(phone_number)
        except Exception as e:
            self._print(
                f"⚠️ error while starting phone auth: {e}\n",
                f"⚠️ Khata dar zaman ersal darkhast auth: {e}\n",
                Fore.RED,
            )
            return None

        return resp

    async def _handle_code_entry(self, resp):
        expiration_timestamp = time.time() + resp.timeout

        self._print("✅ Code sent!", "✅ code ersal shod!", Fore.GREEN)
        self._print(
            "🔑 Enter your code. Available commands:\n"
            "   'restart' - enter your phone number again\n"
            "   'fin'     - enable Fingilish mode\n"
            "   'en'      - switch back to English\n",
            "🔑 Code ra vared kon. dasturat:\n"
            "   'restart' - Vorood-e dobare shomare\n"
            "   'fin' - Raftan be zaban fingilishi\n"
            "   'en' - Raftan be zaban en\n",
            Fore.CYAN,
        )

        while True:
            if time.time() > expiration_timestamp:
                self._print(
                    "⌛ Code expired. Restarting phone entry...\n",
                    "⌛ Zaman code tamoom shod. Bargasht be marhale shomare...\n",
                    Fore.RED,
                )
                return False

            try:
                remaining_time = expiration_timestamp - time.time()

                self._print(
                    f"⏳ Time left before expiration: {int(remaining_time)} sec",
                    f"⏳ Zaman baghi mande ta enghaza: {int(remaining_time)} sanie",
                    Fore.YELLOW,
                )

                try:
                    code = await asyncio.wait_for(
                        asyncio.to_thread(
                            self._input,
                            "Enter code: ",
                            "Code ra vared kon: ",
                            Fore.BLUE,
                        ),
                        timeout=remaining_time,
                    )
                except asyncio.TimeoutError:
                    self._print(
                        "⏰ Code entry timed out. Please try again.\n",
                        "⏰ Mohlat vared kardan code tamoom shod. Mojadadan talash konid.\n",
                        Fore.RED,
                    )
                    return False

                code = code.strip().lower()

                # language toggles first
                if code == "fin":
                    self.fingilish_mode = True
                    self._print(
                        "✅ Fingilish mode ON.",
                        "✅ Halat Fingilish fa'al shod.",
                        Fore.GREEN,
                    )
                    continue
                if code == "en":
                    self.fingilish_mode = False
                    self._print(
                        "✅ English mode ON.",
                        "✅ Halat English fa'al shod.",
                        Fore.GREEN,
                    )
                    continue

                if code == "restart":
                    self._print(
                        "🔄 Restarting phone entry...\n",
                        "🔄 Bargasht be marhale vared kardane shomare...\n",
                        Fore.MAGENTA,
                    )
                    return False

                # Validate the code (with AiobaleError handling)
                try:
                    res = await self.client.sign_in(code)
                    print(res)
                except Exception as e:
                    self._print(
                        f"⚠️ error while validating code: {e}\n",
                        f"⚠️ Khata dar zamineh-e validate kardan code: {e}\n",
                        Fore.RED,
                    )
                    return False

                if isinstance(res, RpcError):
                    self._print(
                        f"You encountered an error with error_message {res.error_message}. Please try again.\n",
                        f"Khata dar zamineh-e validate kardan code: {res.error_message}\n",
                        Fore.RED,
                    )
                    return False

                await self._on_login_success(res)
                return True

            except Exception as e:
                self._print(
                    f"⚠️ Unexpected error: {e}\n",
                    f"⚠️ Khataye gheire montazer: {e}\n",
                    Fore.RED,
                )
                return False

    async def _on_login_success(self, res):
        self._print(
            f"🎉 Login successful! Welcome {res.user.first_name}",
            f"🎉 Vorood movafagh! Khosh amadid {res.user.last_name}",
            Fore.GREEN,
        )

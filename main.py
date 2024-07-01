from proxy import get_tor_session
from telebot.util import async_dec
import logging
import os
import sys
import pyTelegramBotAPI
import asyncio
import telebot
import dotenv
from telebot.async_telebot import AsyncTeleBot
logging.basicConfig(level=logging.INFO)
dotenv.load_dotenv()
bot_token = os.getenv("BOT")
ai_token = os.getenv("OPENAI")

USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
)
HEADERS = {"User-Agent": USER_AGENT,
           "Authorization": f"Bearer {ai_token}"}
bot = None

@async_dec()
async def main() -> None:
    bot = telebot.async_telebot.AsyncTeleBot(token =  bot_token, parse_mode = 'HTML')
    await bot.polling(non_stop=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

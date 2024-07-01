from proxy import get_tor_session
from telebot.util import async_dec
import logging
import os
import sys
import asyncio
import pyTelegramBotAPI
import dotenv
from main import *
from telebot.async_telebot import AsyncTeleBot
from
from main import bot, HEADERS
@async_dec()

@bot.message_handler(commands=['start'])
async def welcome(message):
    session = get_tor_session()
    response = session.post(url="https://api.openai.com/v1/chat/completions",
                            headers=HEADERS,
                            json={"messages": [{"role": "user", "content": message.text}], "model": "gpt-4o"},
                            timeout=9999).json()["choices"][0]["message"]["content"]
    await message.answer(
        text=str(response),
        parse_mode="MarkdownV2"
    )

@staticmethod
@bot.message_handler(commands=["stop"])
async def stop_dialog(message: types.Message, state: FSMContext):
        await state.finish()
        TG_BOT.messages = []
        await message.reply(text="Диалог остановлен")
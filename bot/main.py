import asyncio
import logging
import os
import sys
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()
bot = Bot(token=os.getenv("TOKEN"))

dp.message()
async def start_handler(message: Message):
    await message.answer("Salom")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


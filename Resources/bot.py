import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os



load_dotenv()
API_TOKEN = os.getenv("TOKEN")

if not API_TOKEN:
    raise ValueError("API token not found. Please set the TOKEN in your .env file.")


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start', 'help']))
async def command_start_handler(message: Message):
    await message.reply("Hi\nI am Jarvis !")

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    logging.info("Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

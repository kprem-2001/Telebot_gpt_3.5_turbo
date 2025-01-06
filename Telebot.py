import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
import openai


class Reference:
    """Class to store the previous response from ChatGPT API."""
    def __init__(self):
        self.response = ""


# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Bot token not found. Please set the TOKEN in your .env file.")
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set the OpenAI_API_KEY in your .env file.")

MODEL_NAME = 'gpt-3.5-turbo'
reference = Reference()

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Configure logging
logging.basicConfig(level=logging.INFO)


def clear_past():
    """Clear the stored ChatGPT response."""
    reference.response = ""


@dp.message(Command(commands=['start']))
async def start_handler(message: Message):
    """Handle the `/start` command."""
    await message.reply("Hi! I am your AI assistant. How can I help you?")


@dp.message(Command(commands=['clear']))
async def clear_handler(message: Message):
    """Handle the `/clear` command."""
    clear_past()
    await message.reply("All stored conversations have been cleared!")


@dp.message(Command(commands=['help']))
async def help_handler(message: Message):
    """Handle the `/help` command."""
    helper_text = """
Available Commands:
/start - Start the bot.
/clear - Clear the bot's memory of previous responses.
/help - Show this help message.
Simply type your question, and I'll answer using AI!
    """
    await message.reply(helper_text)


@dp.message()
async def chatgpt_handler(message: Message):
    """Process user input and generate a response using OpenAI's ChatGPT API."""
    try:
        logging.info(f"User Input: {message.text}")
        
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "assistant", "content": reference.response},
                {"role": "user", "content": message.text}
            ]
        )
        
        # Extract the response and save it
        reference.response = response['choices'][0]['message']['content']
        logging.info(f"ChatGPT Response: {reference.response}")
        
        # Send the response back to the user
        await message.answer(reference.response)

    except Exception as e:
        logging.error(f"Error in ChatGPT handler: {e}")
        await message.reply("Sorry, something went wrong. Please try again later.")


async def main():
    """Start the bot."""
    logging.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

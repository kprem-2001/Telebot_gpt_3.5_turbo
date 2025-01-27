# **Telegram Bot with GPT-3.5 Turbo**

## Overview

This project demonstrates a **Telegram Bot** powered by **OpenAI's GPT-3.5 Turbo API**, enabling intelligent and conversational interactions with users. The bot is designed to provide human-like responses to user queries, making it a versatile tool for various applications like customer support, personal assistants, and more.

## Project Highlights

- **API Integration**: Utilizes **OpenAI's GPT-3.5 Turbo API** for generating contextually relevant and accurate responses.
- **Telegram Bot**: Built using the `python-telegram-bot` library, making it easy to deploy and interact with.
- **Application**: This bot can be used for customer support, personal assistance, or even as a fun conversational tool.

## Features

- **AI-Powered Responses**: Generates human-like and contextually relevant responses using GPT-3.5 Turbo.
- **Easy to Use**: Simply run the bot using a single command, and it's ready to interact with users on Telegram.
- **Customizable**: Modify the bot's behavior by tweaking the code or adjusting API parameters like `temperature` and `max_tokens`.

## Installation

To get started with the project, follow the steps below:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/telebot.git
    cd telebot
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    - Create a `.env` file in the root directory.
    - Add your Telegram bot token and OpenAI API key to the `.env` file:

      ```plaintext
      TELEGRAM_BOT_TOKEN=your-telegram-bot-token
      OPENAI_API_KEY=your-openai-api-key
      ```

## Usage 🚀

To use this project, you can run it as a command-line tool.

### Command-line tool 💻

To start the bot, use the following command:

```bash
python telebot.py

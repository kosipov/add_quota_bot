# Import the python-telegram-bot library
import os

import telegram
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

# Define a function that handles text messages
def list_handler(update: Update, context) -> None:
    # Get the text message from the update object
    text = update.message.text
    # Split the text by whitespace characters
    values = text.split()
    # Wrap each value in single quotes and join them with commas
    result = ", ".join(f"'{value}'" for value in values)
    # Send the result back to the user
    update.message.reply_text(result)

bot_token = os.environ["BOT_TOKEN"]
# Create an updater object with your bot token
updater = Updater(bot_token)

# Register a handler for text messages
updater.dispatcher.add_handler(MessageHandler(Filters.text, list_handler))

# Start the bot
updater.start_polling()
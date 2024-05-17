import os
import sys
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the project root to the Python path
sys.path.append("..")
from loggram.loggram import Loggram
sys.path.remove("..")

# Get token and chat ID from environment variables
token = os.getenv("TELEGRAM_BOT_TOKEN")  # Ensure you have this set in your .env file
chat_id = os.getenv("TELEGRAM_CHAT_ID")  # Ensure you have this set in your .env file

if __name__ == "__main__":
    logger = Loggram(token, chat_id, verbose=True)

    try:
        abc  # Code that might raise an error
    except Exception as e:
        # Send simple message
        logger.send_traceback(str(e))

        # Send to a topic in a group
        # Make sure reply_to_message_id is a valid message ID in your Telegram group
        logger.send_traceback(str(e), reply_to_message_id=26113)

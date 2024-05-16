import sys
import time

sys.path.append("..") 
from loggram.loggram import Loggram
sys.path.remove("..")

token = "YOUR_TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_TELEGRAM_CHAT_ID"

if __name__=="__main__":
    logger = Loggram(token, chat_id)
    try:
        abc # Code that might raise an error
        ...

    except Exception as e:                
        # for send simple message
        logger.send_traceback(str(e))
        # for send to a topic in group
        logger.send_traceback(str(e),reply_to_message_id=26113)


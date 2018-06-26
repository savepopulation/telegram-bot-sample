import telepot
from pprint import pprint
import time
import datetime
from telepot.loop import MessageLoop

TOKEN = "your_bot_token_goes_here"
VALID_MESSAGE_TYPE = 'text'
VALID_CHAT_TYPE = 'private'
DEFAULT_ERROR = 'Please type /help for valid commands'
DEFAULT_PREFIX = '/'

COMMAND_HELP = "/help"
COMMAND_HELLO = "/hello"
COMMAND_TIME = "/time"
COMMAND_RESERVATION = "/reservation"

def handle_message(msg):
    pprint(msg)
    chat_type = msg['chat']['type']
    receiver_id = msg['chat']['id']
    if msg and chat_type == VALID_CHAT_TYPE:
        message = msg['text']
        if message and message.startswith(DEFAULT_PREFIX):
            if message == COMMAND_RESERVATION:
                show_keyboard = {'keyboard': [['21:00', '22:00'], ['23:00', '24:00']]}
                bot.sendMessage(receiver_id, 'Available times for reservation:', reply_markup=show_keyboard)
            else:
                bot.sendMessage(receiver_id, generate_response(message))
        else:
            bot.sendMessage(receiver_id, DEFAULT_ERROR)


def generate_response(msg):
    if msg == COMMAND_HELP:
        return "List of available commands:\n/hello\n/time\n/reservation"
    elif msg == COMMAND_HELLO:
        return "hi"
    elif msg == COMMAND_TIME:
        return datetime.datetime.now()
    else:
        return DEFAULT_ERROR



bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle_message).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)

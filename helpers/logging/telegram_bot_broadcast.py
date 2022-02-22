from urllib.request import urlopen
import requests
import aiohttp
import json
from shell_helpers import LogTypes


TOKEN = '5285902284:AAF3YFIFd3Ij6Bu6fxkStsx-Hn4hPzT4M7U'


class TelegramBotBroadcast:
    def __init__(self, **kwargs):
        self._chat_ids = kwargs['chat_ids'] if 'chat_ids' in kwargs else None
        self._mode = kwargs['mode'] if 'mode' in kwargs else LogTypes.Telegram_Lite
        self._messages_queue = []

URL_GET_USERS = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
URL_SEND = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


def get_chat_ids(url_get_users):
    response = urlopen(url_get_users).read().decode('utf-8')
    response = json.loads(response)
    chat_ids = []

    for chat in response['result']:
        chat_ids.append(chat['message']['chat']['id'])

    return chat_ids

def run():
    chat_ids = get_chat_ids(URL_GET_USERS)

    broadcast_messages = ['test message']

    for chat_id in chat_ids:
        for message in broadcast_messages:
            data = {
                'chat_id': chat_id,
                'text': message
            }
            requests.post(URL_SEND, data=data)

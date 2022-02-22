from helpers.exceptions import logging_exceptions as excepts
from shell_helpers import TelegramLogTypes
from urllib.request import urlopen
import requests
import aiohttp
import json
import telegram_send


TOKEN = '5132687398:AAG_SKgO5ZW0WmQIBSFRpi9rkV9em9EtDfw'
URL_GET_USERS = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
URL_SEND = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


class TelegramBotBroadcast:
    def __init__(self, **kwargs):
        self._chat_ids = kwargs['chat_ids'] if 'chat_ids' in kwargs else None
        self._mode = kwargs['mode'] if 'mode' in kwargs else TelegramLogTypes.Telegram_Lite
        self._messages_queue = []
        self._all_chat_ids = self.get_chat_ids()
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            if self._chat_ids is None:
                raise excepts.NoChatIDException
            if len(self._chat_ids) == 0:
                raise excepts.NoChatIDException
            for chat_id in self._chat_ids:
                if not chat_id in self._all_chat_ids:
                    raise excepts.InvalidChatIDException
            if self._mode is None:
                raise excepts.NoTelegramLogModeException
            if not self._mode in TelegramLogTypes:
                raise excepts.InvalidTelegramLogModeException
        except excepts.LogException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalLoggingException.evoke(e)

    def get_chat_ids(self):
        response = urlopen(URL_GET_USERS).read().decode('utf-8')
        response = json.loads(response)
        chat_ids = []

        for chat in response['result']:
            chat_ids.append(chat['message']['chat']['id'])

        return chat_ids

    def run(self):
        for chat_id in self._chat_ids:
            for message in self._messages_queue:
                data = {
                    'chat_id': chat_id,
                    'text': message
                }
                requests.post(URL_SEND, data=data)

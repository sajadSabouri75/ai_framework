from helpers.logging.logger import Logger
import urllib.request
from helpers.exceptions import logging_exceptions as excepts
from shell_helpers import TelegramLogTypes
import requests
import json
from fake_useragent import UserAgent
from datetime import datetime


TOKEN = '5279453653:AAFaXc5a2fSs8WII3JWJ_5XIH6Fu4Iuy82k'
URL_GET_USERS = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
URL_SEND = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


class TelegramBotBroadcast(Logger):
    def __init__(self, **kwargs):
        self._chat_ids = kwargs['chat_ids'] if 'chat_ids' in kwargs else None
        self._mode = kwargs['mode'] if 'mode' in kwargs else TelegramLogTypes.Telegram_Lite
        now = datetime.now()
        self._messages_queue = [f'broadcast initialized @ {now.strftime("%d/%m/%Y - %H:%M:%S")}']
        self._messages_queue.append(f'mode: {self._mode}')
        self._all_chat_ids = self.get_chat_ids()

        if self._chat_ids[0] == 'all':
            self._chat_ids = self._all_chat_ids

        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            if self._chat_ids is None:
                raise excepts.NoChatIDException
            if len(self._chat_ids) == 0:
                raise excepts.NoChatIDException
            list_of_not_found_ids = []
            for chat_id in self._chat_ids:
                if chat_id not in self._all_chat_ids:
                    list_of_not_found_ids.append(chat_id)
            if len(list_of_not_found_ids) > 0:
                raise excepts.InvalidChatIDException
            if self._mode is None:
                raise excepts.NoTelegramLogModeException
            if not self._mode in TelegramLogTypes:
                raise excepts.InvalidTelegramLogModeException
        except excepts.InvalidChatIDException as e:
            e.evoke(list_of_not_found_ids)
        except excepts.LogException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalLoggingException.evoke(e)

    def get_chat_ids(self):
        faker = UserAgent()
        request = urllib.request.Request(URL_GET_USERS)
        request.add_header('User-Agent', faker.random)
        response = urllib.request.urlopen(request).read().decode('utf-8')
        response = json.loads(response)
        chat_ids = []

        for chat in response['result']:
            chat_id = chat['message']['chat']['id']
            if chat_id not in chat_ids:
                chat_ids.append(chat_id)

        return chat_ids

    def flush(self):
        self.send_messages()

    def send_messages(self):
        faker = UserAgent()
        headers = {'User-Agent': faker.random}
        all_in_one_message = "".join([message + "\n" for message in self._messages_queue])
        print(all_in_one_message)
        for chat_id in self._chat_ids:
            data = {
                'chat_id': chat_id,
                'text': all_in_one_message
            }
            requests.post(URL_SEND, data=data, headers=headers)

    def define_framework(self):
        self._messages_queue.append(f'>> AI Framework running')

    def define_connection(self, tag):
        if tag == 'start':
            self._messages_queue.append(f'<connection>')
        elif tag == 'end':
            self._messages_queue.append(f'</connection>')

    def print_warning(self, warning_message):
        if not self._mode == TelegramLogTypes.Telegram_Lite:
            self._messages_queue.append(f'<warning>{warning_message}</warning>')

    def print_error(self, error_message):
        self._messages_queue.append(f'<error> {error_message} </error>')

    def confirm_connection(self, connection_id, connection_name):
        self._messages_queue.append(
            f'<confirmation> connection [{connection_id}:{connection_name}] confirmed! </confirmation>')

    def print_internal_message(self, message):
        if not self._mode == TelegramLogTypes.Telegram_Lite:
            self._messages_queue.append(f'<message> {message}</message>')

    def define_get(self, tag):
        if tag == 'start':
            self._messages_queue.append(f'<get>')
        elif tag == 'end':
            self._messages_queue.append(f'</get>')

    def confirm_data_cache(self, connection_id, connection_name):
        self._messages_queue.append(
            f'<data_cache> '
            f'data from connection [{connection_id}:{connection_name}] cached! '
            f'</data_cache>'
        )

    def define_frame(self, tag):
        if tag == 'start':
            self._messages_queue.append(f'<frame>')
        elif tag == 'end':
            self._messages_queue.append(f'</frame>')

    def confirm_framing(self):
        self._messages_queue.append(
            f'<frame_confirmation> '
            f'framed successfully! '
            f'</frame_confirmation>'
        )

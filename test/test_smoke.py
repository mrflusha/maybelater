import unittest
from telethon import TelegramClient
from telethon import sync, events
from time import sleep


'''


Заходим на сайт телеграма: https://my.telegram.org
Вводим телефон и ждем код подтверждения на родном клиенте телеграма. Он довольно длинный (12 символов) и неудобный для ввода.

Заходим в пункт "API". Ищем "Telegram API" и заходим в "Creating an application" (https://my.telegram.org/apps).

Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash. 


'''


api_id = ""
api_hash = ""
def get_str(msgs):
	for mes in msgs:
			mess = str(mes.message)
			return mess


class TelegramTestCase(unittest.TestCase):

	def test_answer(self):	
		with TelegramClient('name', api_id, api_hash) as self.client:	


			
			self.client.send_message('@teoll_bot', '/start')
			sleep(10)
			self.msgs = self.client.get_messages("@teoll_bot")
			self.mess = get_str(self.msgs)
			print(self.mess)
			assert self.mess == "Какую пиццу вы хотите заказать большую или маленькую?"
			sleep(10)



	def test_second_answer(self):
		with TelegramClient('name', api_id, api_hash) as self.client:


			

			self.client.send_message('@teoll_bot', '/start')
			sleep(4)
			self.client.send_message('@teoll_bot', 'Большую')
			sleep(4)
			self.msgs = self.client.get_messages("@teoll_bot")
			sleep(4)
			self.mess = get_str(self.msgs)
			


			assert self.mess == "Оплата будет производиться наличкой или картой?"

	def test_third_answer(self):
		with TelegramClient('name', api_id, api_hash) as self.client:

			self.client.send_message('@teoll_bot', '/start')
			sleep(4)
			self.client.send_message('@teoll_bot', 'Большую')
			sleep(4)
			self.client.send_message('@teoll_bot', 'наличкой')
			sleep(4)
			self.msgs = self.client.get_messages("@teoll_bot")
			sleep(4)
			self.mess = get_str(self.msgs)
			


			assert ("большую" and "наличкой") in self.mess

	def test_fourth_answer(self):
		with TelegramClient('name', api_id, api_hash) as self.client:
					
			self.client.send_message('@teoll_bot', '/start')
			sleep(4)
			self.client.send_message('@teoll_bot', 'Большую')
			sleep(4)
			self.client.send_message('@teoll_bot', 'наличкой')
			sleep(4)
			self.client.send_message('@teoll_bot', 'да')
			sleep(4)
			self.msgs = self.client.get_messages("@teoll_bot")
			sleep(4)
			self.mess = get_str(self.msgs)
			


			assert ("большую" and "наличкой" and "Спасибо") in self.mess


	def test_cancel_answer(self):
		with TelegramClient('name', api_id, api_hash) as self.client:
					
			self.client.send_message('@teoll_bot', '/start')
			sleep(4)
			self.client.send_message('@teoll_bot', 'Большую')
			sleep(4)
			self.client.send_message('@teoll_bot', 'наличкой')
			sleep(4)
			self.client.send_message('@teoll_bot', 'нет')
			sleep(4)
			self.msgs = self.client.get_messages("@teoll_bot")
			sleep(4)
			self.mess = get_str(self.msgs)
			


			assert "/start" in self.mess





if __name__ == '__main__':
    unittest.main(verbosity=2)
import telebot, config, logging
from telebot import types

class pizza(object):
	"""docstring for pizza"""
	def __init__(self, user_id, nick, size, pay_type):
		super(pizza, self).__init__()
		self.user_id = user_id
		self.nick = nick
		self.size = size
		self.pay_type = pay_type

bot = telebot.TeleBot(config.token)
logging.basicConfig(level=logging.INFO)



rage = False
global order


@bot.message_handler(commands=['start'])
def pizza_message(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	button_big = types.KeyboardButton(text = "Большую")
	button_small = types.KeyboardButton(text = "Маленькую")
	markup.add(button_big,button_small)

	bot.send_message(message.chat.id , "Какую пиццу вы хотите заказать большую или маленькую?", reply_markup = markup)


@bot.message_handler(content_types = ['text'])

def confirm(message):
	arr = list()# user_id, nick, pizza-size, paytype
	text_message = message.text.lower()
	global rage
	global pay_type 
	global pizza_size 
	if text_message == "большую" or text_message == "маленькую":
		pizza_size = text_message.lower()
		paytype_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		paytype_buttons = [types.KeyboardButton('Наличкой'),types.KeyboardButton('Картой')]
		paytype_markup.add(paytype_buttons[0],paytype_buttons[1])
		bot.send_message(message.chat.id, "Оплата будет производиться наличкой или картой?",reply_markup = paytype_markup)
	elif text_message == "наличкой" or text_message == "картой":
		pay_type = text_message.lower()

	try:
		if pizza_size and pay_type and not rage:
			confirm_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			confirm_buttons = [types.KeyboardButton('Да'), types.KeyboardButton('Нет')]
			confirm_markup.add(confirm_buttons[0],confirm_buttons[1])
			bot.send_message(message.chat.id,f"Ваш заказ:\nРазмер пиццы: {pizza_size}\nОплата: {pay_type}\nВсё верно?", reply_markup = confirm_markup)
			rage = True
	except NameError as e:
		pass
	try:
		if pizza_size and pay_type and text_message == "да":
			a = telebot.types.ReplyKeyboardRemove()
			order = pizza(message.chat.id, message.from_user.username, pizza_size,pay_type)

			bot.send_message(message.chat.id, f"Спасибо за заказ \nВаш заказ {order.nick} на {pizza_size} пиццу, Оплата: {pay_type} в скором времени будет обработан", reply_markup = a)
			print(order.nick)
			pizza_size = "костыль"
			pay_type = ""
			rage = False
		elif pizza_size and pay_type and text_message == "нет":
			a = telebot.types.ReplyKeyboardRemove()
			bot.send_message(message.chat.id, f"Введите команду /start и повторите сначала {message.from_user.username}", reply_markup = a)
			
	except NameError as e:
			pass



	
'''		
def pay_type(message):
	paytype = message.text.lower()
	bot.send_message(message.chat.id, pizza_size, paytype)


	bot.send_message(message.chat.id, pizza_size)
'''
'''

@bot.callback_query_handler(func= lambda call:True)



def confirm_pizza_size(call):
	if call.data == "большую":
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		yes_button = types.KeyboardButton("Да")
		no_button = types.KeyboardButton("Нет")
		markup_reply.add(yes_button,no_button)
		bot.send_message(call.message.chat.id , "Вы действительно хотите заказать большую пиццу?", reply_markup=markup_reply)		
	elif call.data == "маленькую":
		print("small")
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		yes_button = types.KeyboardButton("Да")
		no_button = types.KeyboardButton("Нет")
		markup_reply.add(yes_button,no_button)
		bot.send_message(call.message.chat.id,"Вы действительно хотите заказать маленькую пиццу?", reply_markup=markup_reply)		
'''

bot.infinity_polling()
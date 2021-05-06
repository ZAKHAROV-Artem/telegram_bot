import telebot
import random
import pyowm

from telebot import types


# print('В городе ' + place + ' сейчас температура ' + str(temperature) + ' градуса по цельсию')

bot = telebot.TeleBot('1028036404:AAEPu7Kxn7galAbMi4mQNyzFoFfaZMe8ceQ')
place = ''
randomGame = ''
observation = ''
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🎲0-10")
	item2 = types.KeyboardButton("🎲0-1000")
	item3 = types.KeyboardButton("🎲0-100000")
	item4 = types.KeyboardButton("Погода")
	item5 = types.KeyboardButton("Игра")
	item6 = types.KeyboardButton('Instagram')
	markup.add(item1,item2,item3,item4,item5,item6)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный Артемом Захаровым я его первый бот )))).".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	
	if message.chat.type == 'private':
		if message.text == '🎲0-10':
			bot.send_message(message.chat.id, str(random.randint(0,10)))
		if message.text == '🎲0-1000':
			bot.send_message(message.chat.id, str(random.randint(0,1000)))
		if message.text == '🎲0-100000':
			bot.send_message(message.chat.id, str(random.randint(0,100000)))
		if message.text == 'Погода':
			bot.send_message(message.from_user.id, 'В каком городе ты хочешь узнать погоду макарошка?')
			bot.register_next_step_handler(message, get_weather)
		if message.text == 'Игра':
			bot.send_message(message.chat.id, 'Правила игры: я загадываю число от 0 - 5 \n а ты его должен отгадать , все просто P.S я уже загадал)')
			bot.register_next_step_handler(message, get_randomGame)
		if message.text == 'Instagram':
			bot.send_message(message.chat.id, 'Подпишись пожалуйста )')
			bot.send_message(message.chat.id, 'https://www.instagram.com/invites/contact/?i=1alkmmd1xv87c&utm_content=333qb43')
def get_weather(message):
	try:
		global place
		place = message.text

		owm = pyowm.OWM('78ea318e8890258175c1551059981a9d')
		observation = owm.weather_at_place(place)
		w = observation.get_weather()

		sunrise_date = weather.sunrise_time(timeformat='date')
		sunrset_date = weather.sunset_time(timeformat='date')

		wind_speed = w.wind()

		status = w.detailed_status 
		pressure_dict = mgr.weather_at_place(place).observation.pressure
		temperature = w.get_temperature('celsius')['temp']
		bot.send_message(message.chat.id, 'В городе ' + str(place) +' '+str(status) + '\n Температура ' + str(temperature) +' ˚C \n Влажность - '+str(w.humidity)+'\n Скорость ветра - '+str(wind_speed['speed'])+' м/с \n Время восхода - '+str(sunrise_date)+'\n Время заката - '+str(sunrset_date)+'')
	except :
		bot.send_message(message.chat.id, 'Похоже такого города нет :(')


# RUN

def get_randomGame(message):
	global randomGame
	randomGame = str(random.randint(0,5))
	if message.text == randomGame:
		bot.send_message(message.chat.id, 'Молодец макарошка ты угадал ответ ' + randomGame)
	else:
		bot.send_message(message.chat.id, 'Не повезет в рандоме повезет в ЛЮБВИ ответ: ' + randomGame)

#
while True:
            bot.polling(none_stop=True, interval=0)

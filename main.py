import os
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(commands=['quotes'])
def quotes(message):
	data=requests.get('https://officeapi.dev/api/quotes/random')
	ot=data.json()
	o=ot.get('data')
	char=o['character']

	quote=str(o['content'])+os.linesep+os.linesep+"— "+str(char.get('firstname'))+" "+str(char.get('lastname'))
	bot.send_message(message.chat.id, quote)


@bot.message_handler(commands=['characters'])
def quotes(message):
	data=requests.get('https://officeapi.dev/api/characters/random')
	ot=data.json()
	o=ot.get('data')
	if(str(o.get('lastname'))==null):
		CharacterData=str(o.get('firstname'))
	else:
		CharacterData=str(o.get('firstname'))+" "+str(o.get('lastname'))
	bot.send_message(message.chat.id, CharacterData)


@bot.message_handler(commands=['episodes'])
def quotes(message):
	data=requests.get('https://officeapi.dev/api/episodes/random')
	ot=data.json()
	o=ot.get('data')

	episodeData="Episode - "+ str(o.get('title'))+ os.linesep + os.linesep + "Description - "+ str(o.get('description')) + os.linesep + os.linesep +"Air Date - "+ str(o.get('airDate'))
	bot.send_message(message.chat.id, episodeData)

bot.infinity_polling()

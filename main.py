import os
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
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

bot.infinity_polling()

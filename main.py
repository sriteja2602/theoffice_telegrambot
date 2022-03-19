import os
import telebot
import requests
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
	help='''
	You can control me by sending these commands:

	/quotes - displays a random quote from any character
	/rquote - displays a random quote every 20 minutes
	/characters - displays a random character
	/episodes - shows a random episode details
	/crew - get a random crew member 
	/allcrew - get a list of all crew members
	/help - see all available commands
	'''
	bot.send_message(message.chat.id, "What's up my brotha?")
	bot.send_message(message.chat.id, help)
	

@bot.message_handler(commands=['quotes'])
def quotes(message):
	data=requests.get('https://officeapi.dev/api/quotes/random')
	ot=data.json()
	o=ot.get('data')
	char=o['character']
	quote=str(o['content'])+os.linesep+os.linesep+"— "+str(char.get('firstname'))+" "+str(char.get('lastname'))
	bot.send_message(message.chat.id, quote)



@bot.message_handler(commands=['characters'])
def characters(message):
	data=requests.get('https://officeapi.dev/api/characters/random')
	ot=data.json()
	o=ot.get('data')
	if(str(o.get('lastname'))=='null'):
		CharacterData=str(o.get('firstname'))
	else:
		CharacterData=str(o.get('firstname'))+" "+str(o.get('lastname'))
	bot.send_message(message.chat.id, CharacterData)


@bot.message_handler(commands=['episodes'])
def episodes(message):
	data=requests.get('https://officeapi.dev/api/episodes/random')
	ot=data.json()
	o=ot.get('data')
	episodeData="**Episode** - "+ str(o.get('title'))+ os.linesep + os.linesep + "**Description**"+ os.linesep+os.linesep+ str(o.get('description')) + os.linesep + os.linesep +"**Air Date** - "+ str(o.get('airDate'))
	bot.send_message(message.chat.id, episodeData)


@bot.message_handler(commands=['crew'])
def crew(message):
	data=requests.get('https://officeapi.dev/api/crew/random')
	ot=data.json()
	o=ot.get('data')
	crew=str(o.get('name'))+ " — " + str(o.get('role')) 
	bot.send_message(message.chat.id, crew)

@bot.message_handler(commands=['allcrew'])
def allcrew(message):
	data=requests.get('https://officeapi.dev/api/crew')
	ot=data.json()
	o=ot.get('data')
	allcrew=''''''
	for i in o:
		allcrew+=i.get('name')+" — "+i.get('role')+'\n'
	bot.send_message(message.chat.id, allcrew)


# @bot.message_handler(commands=['rquote'])
# def rquote(message):
# 	now_utc = datetime.now(timezone('UTC'))
# 	now_asia = now_utc.astimezone(timezone('Asia/Kolkata')).minute
# 	if(1):
# 		if(now_asia%20==0):
# 			data=requests.get('https://officeapi.dev/api/quotes/random')
# 			ot=data.json()
# 			o=ot.get('data')
# 			char=o['character']
# 			rquote=str(o['content'])+os.linesep+os.linesep+"— "+str(char.get('firstname'))+" "+str(char.get('lastname'))
# 			bot.send_message(message.chat.id, rquote)
	

@bot.message_handler(commands=['help'])
def help(message):
	help='''
	You can control me by sending these commands:

	/quotes - displays a random quote from any character
	/characters - displays a random character
	/episodes - shows a random episode details
	/help - see all available commands
	'''
	bot.send_message(message.chat.id, help)
bot.infinity_polling()

import discord
import asyncio
from discord.ext import commands
import datetime
import requests
import requests
from bs4 import BeautifulSoup
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def bible_response():
	#https://www.verseoftheday.com/
	response = requests.get("https://www.verseoftheday.com/")
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		div_element = soup.find("div", {"class": "bilingual-left"})
		if div_element:
			return "Verse of Today: " + div_element.text
		else:
			return "Contact Administrator for Message"
	else:
		return "No Message today. Enjoy Studying!"

# timed messages
# async def send_daily_message():
# 	then = datetime.datetime.now()
# 	while True:
# 		now = datetime.datetime.now()
		
# 		# then = now.replace(hour=17, minute=35)
# 		wait_time = (then-now).total_seconds()
# 		print(wait_time) 
# 		await asyncio.sleep(wait_time)
        
# 		channel = bot.get_channel()
# 		bible_daily_verse = bible_response()
# 		await channel.send(bible_daily_verse)
# 		then = datetime.datetime.now() + datetime.timedelta(days=1)

# @bot.command(name="pic")
# async def Dog(ctx):
# 	response = requests.get("https://dog.ceo/api/breeds/image/random")
# 	image_link = response.json()["message"]
# 	await ctx.send(image_link)

@bot.command(name="verse")
async def verse(ctx):
	allowed_channel_id = 1
	if ctx.channel.id == allowed_channel_id:
		bible_daily_verse = bible_response()
		await ctx.send(bible_daily_verse)
	

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


token = os.environ.get('TOKEN')
bot.run(token)

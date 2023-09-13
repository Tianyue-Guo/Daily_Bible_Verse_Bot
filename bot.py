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
async def send_daily_message():
	now = datetime.datetime.now()
	then = datetime.datetime(2023, 9, 13, 8, 0, 0)
	wait_time = (then-now).total_seconds()
	print("wait time: ", wait_time) 
	await asyncio.sleep(wait_time)
	channel = bot.get_channel(1) # PLACEHOLDER
	bible_daily_verse = bible_response()
	await channel.send(bible_daily_verse)

	while True:
		now = then
		then = then + datetime.timedelta(seconds=10)
		# then = now.replace(hour=17, minute=35)
		wait_time = (then-now).total_seconds()
		print("wait time: ", wait_time) 
		await asyncio.sleep(wait_time)
        
		channel = bot.get_channel(1) # PLACEHOLDER
		bible_daily_verse = bible_response()
		await channel.send(bible_daily_verse)
		

# @bot.command(name="pic")
# async def Dog(ctx):
# 	response = requests.get("https://dog.ceo/api/breeds/image/random")
# 	image_link = response.json()["message"]
# 	await ctx.send(image_link)

@bot.command(name="verse")
async def verse(ctx):
	allowed_channel_id = 1 # PLACEHOLDER
	if ctx.channel.id == allowed_channel_id:
		bible_daily_verse = bible_response()
		await ctx.send(bible_daily_verse)
	

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await send_daily_message()


token = os.environ.get('TOKEN')
bot.run(token)

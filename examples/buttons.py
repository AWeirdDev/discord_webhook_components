"""This is just an example, nothing more"""


from discord_webhook_components import  checkWebhook, button, send, URLbutton, embed
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print("ready")

@client.command()
async def webhook(ctx):
  get = await checkWebhook(ctx, 'WEBHOOK_NAME') #Checks webhooks in the channel, and creates one if it doesn't exist
  send(url=get, content='Python is great! Use python!\n||Why did you click this??||', username="Captain Hook UwU", components=[button("hi", "good")]) #For URL buttons, use URLbutton('button label', 'https://example.com/your_link')

@client.command()
async def url(ctx):
  get = await checkWebhook(ctx, 'WEBHOOK_NAME')
  send(url=get, content='Python is great! Use python!\n||Why did you click this??||', username="Captain Hook UwU", components=[URLbutton("my website :D", "https://example.com")])
  
  
client.run('UNIQUE TOKEN')

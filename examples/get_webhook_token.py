from discord_webhook_components import checkWebhookToken as cwt
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print('I am ready!')

@client.command()
async def token(ctx):
  token = await cwt(ctx, 'WEBHOOK_NAME') #check, create webhook, and get its token
  print(token)
  
  
client.run('SUPER SECRET TOKEN')

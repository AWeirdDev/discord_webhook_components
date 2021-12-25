from discord_webhook_components import checkWebhook, embed, send
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print('ready!')
  
@client.command()
async def embeds(ctx):
  url = await checkWebhook(ctx, 'WEBHOOK_NAME')
  my_embed = embed(title="My New Embed!!11!", description='Embeds are really nice :D', image="Image URL", thumbnail="Thumbnail URL", color=0x0995ec, footer="Footer text :D")
  sec_embed = embed(title="Multiple Embeds! Nice!", description="multiple embeds are cool B)", color=0x0995ec) #The color's default value is 0x0995ec
  send(url=url, content="My first webhoook!", embeds=[my_embed, sec_embed]) #list
 

client.run('AMAZING TOKEN')

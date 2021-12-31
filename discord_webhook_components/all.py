import time
import requests
from .exceptions import IncorrectLinkError, WebhookNotFound, NoTokenError, RateLimitError

def button(label, style:int, custom_id:str=None):
  """Returns a button dict"""
  if not custom_id:
    custom_id = str(time.time())
  return {
                    "type": 2,
                    "label": label,
                    "style": style, 
                    "custom_id": custom_id
  }

def URLbutton(label, url:str):
  """With URL buttons, you can add an url in a button"""
  return {
          "type": 2,
          "style": 5,
          "label": label,
          "url": url
        }
  
#Nice tools

async def checkWebhook(ctx, name:str='MyWebhook'):
      """Checks, and creates webhook"""
      try:
        ctx.channel
      except:
        raise(AttributeError("Hmm… This is not the ctx (context) from discord.py"))
      b = False
      webhooks = await ctx.channel.webhooks()
      for webhook in webhooks:
        if webhook.name == name:
            get = webhook.url
            b = True
            return get
      if not b:
          b = await ctx.channel.create_webhook(name=name, reason=f'{time.time()}')
          get = b.url
          return get


async def checkWebhookToken(ctx, name:str='MyWebhook'):
      """Checks, and creates webhook"""
      try:
        ctx.channel
      except:
        raise(AttributeError("Hmm… This is not the ctx (context) from discord.py"))
      b = False
      webhooks = await ctx.channel.webhooks()
      for webhook in webhooks:
        if webhook.name == name:
            try:
              get = webhook.token
            except:
              raise(NoTokenError(f'The current webhook has no token. Webhook name "{name}" was not created by a bot!'))
            b = True
            return get
      if not b:
          b = await ctx.channel.create_webhook(name=name, reason=f'{time.time()}')
          get = b.token
          return get

def send(url, content, username='My Webhook', avatar_url='', embeds=None, components=None):
  """Sends a webhook message"""
  if not url.startswith('https://discord.com/api/webhooks/'):
    raise(IncorrectLinkError('This link is not a discord webhook link!'))
  if components:
    requests.get(url)

  if components:
    data = {
      "content": content,
      "avatar_url": avatar_url,
      "username": username,
      "content": content,
      "embeds": embeds,
      "components": [
        {
          "type":1,
          "components": components
        }
      ]
    }
  else:
      data = {
      "content": content,
      "avatar_url": avatar_url,
      "username": username,
      "content": content,
      "embeds": embeds
      
    }
  try:
    res = requests.post(url, json=data)
    if res.status_code == 429:
      raise(RateLimitError('Hmm... You are being blocked from the site due to error 429, too many requests.\nhttps://discord.com/developers/docs/topics/rate-limits'))
  except:
    if res.status_code == 429:
      raise(RateLimitError('Hmm... You are being blocked from the site due to error 429, too many requests.\nhttps://discord.com/developers/docs/topics/rate-limits'))
    else:
      raise(WebhookNotFound('Webhook was not found or other errors'))



def embed(title, description, thumbnail=None, image=None, color:int=0x0995ec, footer=None):
  """Presents an embed dict"""
  return {
    "title":title,
    "description": description,
      "color": color,
      "image": {
        "url": image
      },
      "thumbnail": {
        "url": thumbnail
      },
      "footer": {
        "text": footer
      }
    }

class style:
  """Colors for the buttons"""
  blurple = 1
  gray = 2
  grey = 2
  green = 3
  success = 3
  red = 4
  warning = 4

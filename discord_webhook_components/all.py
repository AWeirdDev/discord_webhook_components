import time
import requests

class now():
  pass
now.version = '0.0.1'
now.time = time.time()

#important :flushed:
def button(label, custom_id:str=None):
  """Returns a button dict"""
  if not custom_id:
    custom_id = str(time.time())
  return {
                    "type": 2,
                    "label": label,
                    "style": 1, 
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
            get = webhook.token
            b = True
            return get
      if not b:
          b = await ctx.channel.create_webhook(name=name, reason=f'{time.time()}')
          get = b.token
          return get

#Sends webhook
def send(url, content, username='My Webhook', avatar_url='', embeds=None, components=None):
  """Sends a webhook message"""
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
  asdf = requests.post(url, json=data)
  class webhook():
    pass
  webhook.status_code = asdf.status_code
  webhook.json = requests.get(url).text


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

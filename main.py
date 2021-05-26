import os
import discord
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask
from threading import Thread

client =  discord.Client()

@client.event
async def on_ready():
  print('Vape bot is ready, logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  status_url = "http://vapebot.pythonanywhere.com/"

  if message.content.startswith('$litestatus'):
    

    status_html = urlopen(status_url).read()
    soup = BeautifulSoup(status_html, features="html.parser")

# kill all script and style elements
    for script in soup(["script", "style"]):
      script.extract()    # rip it out

# get text
    text = soup.get_text()

# break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
    detection_text = '\n'.join(chunk for chunk in chunks if chunk)

    await message.channel.send(detection_text)

    embedVar = discord.Embed(title="Vape Lite Detection Status", description="This shows the detectibility of vape lite in a screenshare as of now!", color=0x191f29)

    embedVar.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsprEWSbwIcQ00LG_qCR6U4C-pRxguupa-x3jSkKfaPwuwBkov3hfm31Iu8Wm3BOPZjIQ&usqp=CAU')

    embedVar.add_field(name="Echo", value=":green_circle:  Undetected ", inline=False)


    embedVar.add_field(name="Paladin", value=":green_circle:   Undetected",inline=False)

    embedVar.add_field(name="Avenge", value=":green_circle:  Unknown", inline=False)

    embedVar.add_field(name="Actova", value=":yellow_circle:  Unknown", inline=False)

    embedVar.add_field(name="Vape Lite Smasher (Kangoroo)", value=":red_circle: Dogshit", inline=False)



    await message.channel.send(embed=embedVar)
  
  if message.content.startswith('$help'):
    help_embed = discord.Embed(title='Commands for Vape Bot', color=0x18baaf)
    help_embed.add_field(name='$litestatus', value='Checks the screenshare detection of vape lite using various SS Tools.')
    help_embed.add_field(name='$config <Lite/V4> <Blatant, Semi-Closet, Closet>', value='Gives configs for vape lite/v4 depending on blatant/semi-closet/closet (New feature soon to be able to choose servers)')
    help_embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJ2WYBxHjZM3a30mtyk7dZvQQ1TMYSGErrmA&usqp=CAU')

    await message.channel.send(embed=help_embed)
  
  if message.content.startswith('$config'):
    await message.channel.send('Configs coming soon!')



app = Flask(__name__)
if __name__ == '__main__':
  app.run()
@app.route('/')
def keep_alive():
  server = Thread(target=run)
  server.start()

my_secret = os.environ['vape_bot_token']

client.run(os.getenv('vape_bot_token'))

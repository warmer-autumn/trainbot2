import hikari
import os
import dotenv
import requests
import json
import random
from dotenv import load_dotenv
load_dotenv('test.env')


my_secret = os.getenv('TRAIN')

bot = hikari.GatewayBot(token=my_secret)
#test = hikari.KnownCustomEmoji

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent):
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return
    if event.content.startswith("choo choo"):
          await event.message.respond(":steam_locomotive::railway_car::railway_car::railway_car::transgender_flag::transgender_flag::transgender_flag::railway_car::railway_car::railway_car:")
    if event.message.attachments:
        #print(test)
        await event.message.add_reaction("dept_of_trains", 920417740911702036)
        
#async def ping(event: hikari.GuildMessageCreateEvent):
    
#print(os.environ)
bot.run()
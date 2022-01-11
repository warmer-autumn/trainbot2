import hikari
import os
import dotenv
import requests
import json
import random

my_secret = os.environ['train']

bot = hikari.GatewayBot(token=my_secret)


@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    if event.content.startswith("choo choo"):
          await event.message.respond(":steam_locomotive::railway_car::railway_car::railway_car::transgender_flag::transgender_flag::transgender_flag::railway_car::railway_car::railway_car:")
  


bot.run()

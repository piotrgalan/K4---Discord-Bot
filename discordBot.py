import os
from typing import Optional

import aiohttp
import dotenv

import lightbulb
import hikari
from hikari import Intents

dotenv.load_dotenv()

INTENTS = Intents.GUILD_MEMBERS | Intents.GUILDS

discordBot = lightbulb.BotApp(
    os.environ["BOT_TOKEN"],
    intents=INTENTS,
    banner=None,
)

discordBot.load_extensions_from("./extensions/")

@discordBot.listen()
async def on_starting(_: hikari.StartedEvent) -> None:
    discordBot.d.client_session = aiohttp.ClientSession()
    activity = hikari.Activity(name="Counterside", type=hikari.ActivityType.PLAYING)
    await discordBot.update_presence(activity=activity)

@discordBot.listen()
async def on_stopping(_: hikari.StoppingEvent) -> None:
    await discordBot.d.client_session.close()

if __name__ == "__main__":
    discordBot.run()
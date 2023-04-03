# K4 - Discord Bot

K4 is a discord bot created in Python and uses the following modules:
- Hikari
- Hikari-Lightbulb (Lightbulb)
- Aiohttp
- Dotenv
- Typing
- PyMongo

Commands:
/unit           - Connects to the unit database using pymongo and displays information about a specific unit.
/operator       - Connects to the operator database using pymongo and displays information about a specific operator.
/ship           - Connects to the ship database using and displays information about a ship unit.

#In development
/userinfo       - Displays information about specific user.
/timer          - Creates a countdown when the Guild Buff is active. 
/weeklyban      - Connects to the ban list database using pymongo and displays information about the currently banned units, operators and ship in PVP mode.
/announcement   - Creates a general announcement. This includes Title, Message, Image, URL link and Role ping.
/patchnotes     - Creates a patch notes announcement. This include Title and patch notes in a list.
/code           - Creates an annoucnement for in-game codes which can be redeemed.

Note: All the messages are displayed using embeds. 

#How-To-Run
1. Create a .env file (Make sure the file is in the same location as DiscordBot.py)
2. Copy and Paste the following:
  BOT_TOKEN = TOKEN-GOES-HERE 
3. Run DiscordBot.py (Make sure the token is correct and all the intents are on in the developer portal)

- At this moment in time the database will be private. Commands which require information from the database will not work.

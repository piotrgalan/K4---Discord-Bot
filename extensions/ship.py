import hikari
import lightbulb
import pymongo
from typing import Optional
from hikari import Embed

Ship_plugin = lightbulb.Plugin("Ship")

client = pymongo.MongoClient('')
db = client['']
collection = db['']

@Ship_plugin.command
@lightbulb.option("name", "Enter Ship Name.", type=str, required=True)
@lightbulb.command("ship", "Get information about a specific Ship!", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def ship(
    ctx: lightbulb.SlashCommand,
    name: str,
) -> None:

    document = collection.find_one({'Search_Name': name.upper()})

    if document is not None:
        Character_ID = document['Character_ID']
        Search_Name = document['Search_Name']
        Full_Name = document['Full_Name']
        Rarity = document['Rarity']
        Type = document['Type']
        PVE_Rating = document['PVE_Rating']
        PVP_Rating = document['PVP_Rating']
        Skill_1_Name = document['Skill_1_Name']
        Skill_1 = document['Skill_1']
        Skill_2_Name = document['Skill_2_Name']
        Skill_2 = document['Skill_2']
        Skill_3_Name = document['Skill_3_Name']
        Skill_3 = document['Skill_3']
        Analysis = document['Analysis']
        Pros = document['Pros']
        Cons = document['Cons']
        Image = document['Image']

        embed = Embed(title=f"Ship: {Full_Name}")
        embed.add_field("PVE Rating", PVE_Rating, inline=True)
        embed.add_field("PVP Rating", PVP_Rating, inline=True)
        embed.add_field("Rarity", Rarity)
        embed.add_field("Type", Type)
        embed.add_field(f"Skill: {Skill_1_Name} ", Skill_1)
        embed.add_field(f"Skill: {Skill_2_Name} ", Skill_2)
        embed.add_field(f"Skill: {Skill_3_Name} ", Skill_3)
        embed.add_field("Analysis", Analysis)
        embed.add_field("Pros:", Pros)
        embed.add_field("Cons:", Cons)
        embed.set_image(Image)

        await ctx.respond(embed)

    else:
        embed = Embed(title=f"{name} doesn't exist in the database!")
        await ctx.respond(embed)

def load(discordBot: lightbulb.BotApp) -> None:
    discordBot.add_plugin(Ship_plugin)
import hikari
import lightbulb
import pymongo
from typing import Optional
from hikari import Embed

unit_plugin = lightbulb.Plugin("Unit")

client = pymongo.MongoClient('')
db = client['']
collection = db['']

@unit_plugin.command
@lightbulb.option("name", "Enter Unit Name", type=str, required=True)
@lightbulb.command("unit", "Search Unit", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def unit(
    ctx: lightbulb.SlashCommand,
    name: str,
) -> None:

    document = collection.find_one({'Search_Name': name})

    if document is not None:
        Character_ID = document['Character_ID']
        Search_Name = document['Search_Name']
        Full_Name = document['Full_Name']
        Alt_Name = document['Alt_Name']
        Rarity = document['Rarity']
        Role = document['Role']
        Type = document['Type']
        Movement_Type = document['Movement_Type']
        Attack_Type = document['Attack_Type']
        PVE_Rating = document['PVE_Rating']
        PVE_Set = document['PVE_Set']
        PVE_Set_Description = document['PVE_Set_Description']
        PVP_Rating = document['PVP_Rating']
        PVP_Set = document['PVP_Set']
        PVP_Set_Description = document['PVP_Set_Description']
        Image = document['Image']

        embed = Embed(title=f"{Full_Name} ({Alt_Name})")
        embed.add_field("PVE Rating", PVE_Rating)
        embed.add_field("PVP Rating", PVP_Rating)
        embed.add_field("Role", Role)
        embed.add_field("Type", Type)
        embed.add_field("Rarity", Rarity)
        embed.add_field("Movement_Type", Movement_Type)
        embed.add_field("Attack_Type", Attack_Type)
        embed.add_field("PVE_Set", PVE_Set,)
        embed.add_field("PVE_Set_Description", PVE_Set_Description)
        embed.add_field("PVP_Set", PVP_Set)
        embed.add_field("PVP_Set_Description", PVP_Set_Description)
        embed.set_image(Image)
        
        await ctx.respond(embed)

    else:
        embed = Embed(title=f"{name} doesn't exist in the database!")
        await ctx.respond(embed)

def load(discordBot: lightbulb.BotApp) -> None:
    discordBot.add_plugin(unit_plugin)
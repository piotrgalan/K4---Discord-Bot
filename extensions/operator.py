import hikari
import lightbulb
import pymongo
from typing import Optional
from hikari import Embed

Operator_plugin = lightbulb.Plugin("Operator")

client = pymongo.MongoClient('')
db = client['']
collection = db['']

@Operator_plugin.command
@lightbulb.option("name", "Enter Operator Name", type=str, required=True)
@lightbulb.command("operator", "Search Unit", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def operator(
    ctx: lightbulb.SlashCommand,
    name: str,
) -> None:

    document = collection.find_one({'Search_Name': name.upper()})

    if document is not None:
        Character_ID = document['Character_ID']
        Search_Name = document['Search_Name']
        Full_Name = document['Full_Name']
        Rarity = document['Rarity']
        PVE_Rating = document['PVE_Rating']
        PVP_Rating = document['PVP_Rating']
        Ship_HP = document['Ship_HP']
        Ship_ATK = document['Ship_ATK']
        Ship_DEF = document['Ship_DEF']
        Ship_CDR = document['Ship_CDR']
        Ability = document['Ability']
        Ability_Time = document['Ability_Time']
        Level_1 = document['Level_1']
        Level_8 = document['Level_8']
        Skill_Order = document['Skill_Order']
        Analysis = document['Analysis']
        Pros = document['Pros']
        Cons = document['Cons']
        Image = document['Image']
        
        _Stats = f"HP: {Ship_HP}ㅤㅤATK: {Ship_ATK}ㅤㅤDEF: {Ship_DEF}ㅤㅤCDR: {Ship_CDR}\nㅤ"
        _Ability = f"{Ability}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ(Time: {Ability_Time} seconds)"

        embed = Embed(title=f"Operator: {Full_Name}")
        embed.add_field("PVE Rating", PVE_Rating, inline=True)
        embed.add_field("PVP Rating", PVP_Rating, inline=True)
        embed.add_field("Rarity", Rarity)
        embed.add_field("Ship Stats:", _Stats)
        embed.add_field("Ability", _Ability)
        embed.add_field("Level 1", Level_1)
        embed.add_field("Level 8", Level_8)
        embed.add_field("Skill Trigger Order", Skill_Order)
        embed.add_field("Analysis", Analysis)
        embed.add_field("Pros:", Pros)
        embed.add_field("Cons:", Cons)
        embed.set_image(Image)
        
        await ctx.respond(embed)

    else:
        embed = Embed(title=f"{name} doesn't exist in the database!")
        await ctx.respond(embed)

def load(discordBot: lightbulb.BotApp) -> None:
    discordBot.add_plugin(Operator_plugin)
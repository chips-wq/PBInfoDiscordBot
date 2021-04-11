import discord , requests
from bot.scrape.get_sursa import genereaza_sursa
from discord.ext import commands
from bot.scrape.scrape_PBInfo import genereaza_problema
#from bot.bot.troll import server_connect
from bot.util import update_db
from bot.config import auth , BASE_DIR
import bot.db as db

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

import bot.bot.cavou_bot

from bot.bot.util import generate_embed
    
@bot.bot.cavou_bot.client.event
async def on_ready():
    print("we are ready boys")

@bot.bot.cavou_bot.client.command()
async def problema(ctx , name_of_exercise):
    pbinfo_response = requests.get(f"https://www.pbinfo.ro/probleme/{name_of_exercise}")
    if pbinfo_response.status_code == 200:
        problema = genereaza_problema(pbinfo_response)
        genereaza_sursa(problema)
        embed , source_should_be_separate = generate_embed(problema)
        await ctx.send(embed=embed)
        if source_should_be_separate:
            rezolvare = problema.sursa.discord_ready_embed()
            await ctx.send(rezolvare)
    else:
        await ctx.send(f"Ups!Am intampinat o eroare: {pbinfo_response.status_code}")

@bot.bot.cavou_bot.client.command()
async def refresh(ctx):
    update_db(BASE_DIR , auth , db.c)
    await ctx.send("Am dat refresh la probleme!")

@bot.bot.cavou_bot.client.command()
async def name(ctx):
    await ctx.send(f"Numele acestui server este:{ctx.guild.name}\nID-ul acestui server:{ctx.guild.id}.")

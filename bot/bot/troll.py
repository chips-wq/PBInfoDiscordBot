import discord , socket
from discord.ext import tasks , commands

from bot.bot.util import speak_real
import bot.bot.cavou_bot


@bot.bot.cavou_bot.client.command()
async def speak(ctx):
    curr_guild = ctx.guild
    await speak_real(curr_guild , "whatever.mp4")

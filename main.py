import os
from art import *
import discord
from discord.ext import commands, tasks
from discord.utils import get
import openai
import random

TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#fungsi open ai
openai.api_key = "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"
async def generate_response(prompt):
    model = "text-davinci-002"
    temperature = 0.7
    max_tokens = 150
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    reply = response.choices[0].text.strip()
    return reply


#end fungsi dari openai

@bot.command(name='ask')
@commands.has_role('😛 | Friends')
async def chat(ctx, *, message=None):
    if message is None:
        await ctx.send(f'{ctx.author.mention}, ingin bertanya apa?')
    else:
        prompt = f'{ctx.author.mention}: {message}\nBot:'
        reply = await generate_response(prompt)
        await ctx.send(reply)



@bot.command(name='clear')
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit+1)
    await ctx.send(f'{limit} pesan berhasil dihapus.')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"!ask"))
  os.system('cls')
  tprint("Bot Online \n use     !ask")


bot.run('MTA4MTA0MTU5MDk2Mjg4MDU4NA.GByRxP.JTUGBpY3-S6jo1qNAAWploRNkVD9e5-7clxGP8')

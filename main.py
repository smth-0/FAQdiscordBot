#if a new file is created just import it here
from settings import *
from lists import *
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("on")

@client.command(aliases=['quote'])
async def quotes_safezone(ctx):
  await ctx.send(quotes.get("safezone"))

@client.command(aliases=['quotes'])
async def open_book(ctx):
  #we have to define book
  await ctx.send("book")

@client.event
async def on_reaction_add(reaction, ctx):
  if reaction.emoji == '👍':
    await ctx.send("book")

client.run(key)
# if a new file is created just import it here
from settings import *
from lists import *
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("on")

#how the person brings up the message
@client.command(aliases=['quote'])
async def quotes_safezone(ctx):
    #needs to be turned into a book
    msg = await ctx.send("Book Example")

@client.event
async def test(message):
  if message.author.bot:
    print("something")
    await client.delete_message(message)

@client.event
async def on_reaction_add(reaction, channel):
  if reaction.emoji == '👍':
    await channel.send("Book Example") 

@client.command(aliases=['next'])
async def next_page(ctx):
  await ctx.message.edit(content="new page")


client.run(key)

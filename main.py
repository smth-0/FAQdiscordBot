# if a new file is created just import it here
from settings import *
import wrapper
import discord
from discord.ext import commands
from threading import Thread

client = commands.Bot(command_prefix='.', case_insensitive=True)

current_books = {}


class Book:
    def __init__(self, ctx):
        print('new book created', ctx.message.channel.name)
        self.page = 0

    async def start_book(self, context):
        self.msg = await context.send(gui1)

    def flip(self, flip=1):
        # 1 - next, -1 - previous
        self.page += flip
        self.msg.edit('this is page #%d.' % self.page)

@client.event
async def on_ready():
    print("on")


# how the person brings up the message
@client.command(aliases=['quote'])
async def book_spawn(ctx):
    # needs to be turned into a book
    book_obj = Book(ctx)
    await book_obj.start_book(ctx)
    current_books[book_obj.msg.id] = (book_obj)

@client.event
async def on_reaction_add(reaction, channel):
    if reaction.emoji == '👍':
      if 'Frozenbyte Developer' in [i.name for i in reaction.message.author.roles]:
        print('emoji added')
        print('"%s" quote by user "%s" with id @%s' % (
        reaction.message.content, reaction.message.author, reaction.message.author.id))
        wrapper.add_quote(reaction.message)
        await channel.send('logged!')
      else:
        return

    elif reaction.emoji == 'de73a9116babdbce65076a42ac2ac2ba':
        print('flip left')
        current_books[-1].flip(-1)

    elif reaction.emoji == '464b4ad3ec906581bdc288c42780b3c9':
        print('flip right')
        current_books[-1].flip(1)
    else:
        print(reaction.emoji)


@client.command(aliases=['next'])
async def next_page(ctx):
  print('flip right')
  current_books[-1].flip(1)

@client.command(aliases=['before'])
async def last_page(ctx):
  print('flip left')
  current_books[-1].flip(-1)

@client.command(aliases=['searchs'])
async def search(ctx, arg):
  arg = str(arg)
  args = arg.split()
  for arg in args:
    pass
  


try:
    client.run(key)
except Exception as e:
    print('failed to start the bot. reason:', e)

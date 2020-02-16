# if a new file is created just import it here
from settings import *
from lists import *
from wrapper import *
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

current_books = {}


class Book:
    def __init__(self, ctx):
        print('new book created', ctx.message.channel.name)
        self.page = 0

    async def start_book(self, context):
        self.msg = await context.send("Book Example")

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
async def test(message):
    if message.author.bot:
        print("something")
        await client.delete_message(message)


@client.event
async def on_reaction_add(reaction, channel):
    if reaction.emoji == '👍':
      if 'Frozenbyte Developer' in [i.name for i in reaction.message.author.roles]:
        print('emoji added')
        print('"%s" quote by user "%s" with id @%s' % (
        reaction.message.content, reaction.message.author, reaction.message.author.id))
        await channel.send('logged!')
      else:
        return

    elif reaction.emoji == 'afc96e77efee1190e1fbe3cc69f149f8':
        print('flip left')
    elif reaction.emoji == 'afc96e77efee1190e1fbe3cc69f149f8':
        print('flip right')
        await channel.send('right')
    else:
        print(reaction.emoji)


@client.command(aliases=['next'])
async def next_page(ctx):
    current_books[-1].flip(1)


try:
    client.run(key)
except Exception as e:
    print('failed to start the bot. reason:', e)

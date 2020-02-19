# if a new file is created just import it here
from settings import *
import wrapper
import discord
from discord.ext import commands
from threading import Thread

client = commands.Bot(command_prefix='.', case_insensitive=True)

current_books = {}
last_100_books = []
left_turn, right_turn = '⬅️', '➡️'

FBdev = 'Frozenbyte Developer'  # quotable person
quotemod = 'Frozenbyte Developer'  # role allowed to put quotes into DB
book_timeout = 500  # seconds after last flip before it deletes the book -- doesnt works, ignore --


class Book:
    def __init__(self, ctx, tags=None):
        if len(tags) == 0:
            tags = None
        print('new book created in #', ctx.message.channel.name, 'with tags:', tags)
        self.page = 1
        self.results = wrapper.fecth_quote(tags)
        self.search = tags

        self.text, self.pagelen = wrapper.book_renderer(self.search, self.results, self.page)

    async def start_book(self, context):
        self.msg = await context.send(self.text)
        if self.pagelen:
            await self.msg.add_reaction(left_turn)
            await self.msg.add_reaction(right_turn)

    async def flip(self, flip=1):
        # 1 - next, -1 - previous
        if self.pagelen:
            self.page += flip
            if self.page > self.pagelen:
                self.page = 0
            if self.page < 0:
                self.page = self.pagelen
            self.text, self.pagelen = wrapper.book_renderer(self.search, self.results, self.page)
            await self.msg.clear_reactions()
            await self.msg.add_reaction(left_turn)
            await self.msg.add_reaction(right_turn)

            await self.msg.edit(content=self.text, delete_after=book_timeout)

    async def close(self):
        await self.msg.delete()


@client.event
async def on_ready():
    print("on")


# how the person brings up the message
@client.command(aliases=['quote'])
async def book_spawn(ctx, *args):
    # needs to be turned into a book
    book_obj = Book(ctx, args)
    await book_obj.start_book(ctx)
    current_books[book_obj.msg.id] = book_obj
    last_100_books.append(book_obj.msg.id)
    if len(last_100_books) > 100:
        current_books[last_100_books[0]].close()
        current_books[last_100_books[0]] = None
        last_100_books.pop(0)


@client.event
async def on_reaction_add(reaction, channel):
    if reaction.emoji == '👍':
        if FBdev in [i.name for i in reaction.message.author.roles]:
            print('emoji added')
            print('"%s" quote by user "%s" with id @%s' % (
                reaction.message.content, reaction.message.author, reaction.message.author.id))
            wrapper.add_quote(reaction.message)
            await channel.send('logged!')
        else:
            return

    if reaction.message.id in current_books.keys():
        who_reacted = await reaction.users().flatten()
        roles_who_reacted = []
        for i in [i.roles for i in who_reacted]:
            roles_who_reacted.extend(i)
        if quotemod in [i.name for i in roles_who_reacted]:
            if reaction.emoji == left_turn:
                print('flip left')
                await current_books[reaction.message.id].flip(-1)
            elif reaction.emoji == right_turn:
                print('flip right')
                await current_books[reaction.message.id].flip(1)


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

import discord
from discord.ext import commands


key = '' #<-- Bot run key
CF = "." #<--- The thing used at the start of every command
client = commands.Bot(command_prefix=CF, case_insensitive=True)

left_turn, right_turn = '⬅️', '➡️' #<-- Just dont mess with
quote_emoji = '💾' #used to save quotes
#
FBdev = 'Admin'  # quotable person, can save quotes too
quotemod = 'Moderator'  # role allowed to put quotes into DB
quotes_per_page = 10

db_name = "quotes.db"

log_on_boot = 'successfully started'
activity = 'with the database' # playing...

faqhelp = """```diff
commands list
```
```asciidoc
= ".quote <tags>" - search for keywords in the quote database. 
(Shows all if tags is none)
= ".get id <msgID>" - gives you jump link to the message for requested message ID. 
Note: only quoted messages are supported. 
= Adding 💾 emoji works as command to save the quote. 
```

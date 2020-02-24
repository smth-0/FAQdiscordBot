import discord
from discord.ext import commands


key = 'Njc4MDI5MzM3OTk1Mzc4Njg4.Xk29uw.y-OzIKLsjlffAvgwzD0vFDzO_Z0' #<-- Bot run key
CF = "." #<--- The thing used at the start of every command
client = commands.Bot(command_prefix=CF, case_insensitive=True) #<-- Just dont mess with

left_turn, right_turn = '⬅️', '➡️' #<-- Just dont mess with
quote_emoji = '💾' #used to save quotes
#
FBdev = 'Frozenbyte Developer'  # quotable person
quotemod = 'Moderator'  # role allowed to put quotes into DB
quotes_per_page = 10

db_name = "quotes.db" #<-- Also dont mess with

log_on_boot = 'successfully started'
activity = 'with the database' # playing...

#Im just gonna make main a bit cleaner -sweer

faqhelp = """```diff
commands list
```
```asciidoc
= ".quote <tags>" - search for keywords in the quote database. 
(Shows all if tags is none)
= ".get id <msgID>" - gives you jump link to the message for requested message ID. 
Note: only quoted messages are supported. 
= Adding 💾 emoji works as command to save the quote. 

= Made by community members
Lunar#1535
sweer#6178
Blue#8044
= And a special thanks to
Oobfiche#5954
🐉Mr. Extinct#6090```""" #< --- ^^^ credits
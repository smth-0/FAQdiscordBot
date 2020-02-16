import sqlite3

entry = sqlite3.connect("quotes.db")
cur = entry.cursor()

test_list = cur.execute("""SELECT * FROM quotes WHERE id = 0""").fetchall()

print(test_list)

# lemme test this shit on my local rep to not restart the bot every time
import sqlite3

entry = sqlite3.connect("quotes.db")
cur = entry.cursor()

print('wrapper library imported.')


def add_quote(msg_obj):
    # reaction.message should be passed here
    text, usr, msgID, usr_id = msg_obj.content, msg_obj.author, msg_obj.id, msg_obj.author.id
    dateUTC, jumplink = msg_obj.created_at, msg_obj.jump_url

    cur.execute("""INSERT INTO quotes(content, author, msgID, authorID, date, jumplink) VALUES('%s', '%s', '%s', '%s', '%s', '%s')""" %
                (text, usr, msgID, usr_id, dateUTC, jumplink))

    entry.commit()
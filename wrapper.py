import sqlite3

entry = sqlite3.connect("quotes.db")
cur = entry.cursor()
quotes_per_page = 10

print('wrapper library imported.')


def add_quote(msg_obj):
    # reaction.message should be passed here
    text, usr, msgID, usr_id = msg_obj.content, msg_obj.author, msg_obj.id, msg_obj.author.id
    dateUTC, jumplink = msg_obj.created_at, msg_obj.jump_url

    cur.execute(
        """INSERT INTO quotes(content, author, msgID, authorID, date, jumplink) VALUES('%s', '%s', '%s', '%s', '%s', '%s')""" %
        (text.replace(r"'", r"`"), usr, msgID, usr_id, dateUTC, jumplink))

    entry.commit()


def fecth_quote(tags=None):
    # tags - list of strings1
    if tags is None:
        return cur.execute("""SELECT * FROM quotes""").fetchall()
    tmp = []
    for tag in tags:
        tmp.append(r"content like '%{}%' ".format(tag))
    request = ' OR '.join(tmp)
    return cur.execute("""SELECT * FROM quotes WHERE """ + request).fetchall()


def book_renderer(search=None, results=None, page=0):
    if search is None:
        search = ['all']
    if results is None or len(results) == 0:
        return "Sorry, no matches in my database. Maybe try again with different tags?", 0
    else:
        results = ["- '%s' by %s." % (i[0], i[1]) for i in results]

    pages, tmp, k = [], [], 0
    for i in results:
        k += 1
        if k == quotes_per_page:
            k = 0
            pages.append(tmp)
            tmp = []
        tmp.append(i)
    if len(pages) == 0 and len(tmp):
        pages = tmp
    s = """your search: "%s"
current page: %d / %d
quotes:
""" % ('; '.join(search), page, len(pages) + 1)
    print("page", page, len(pages))
    s += '\n'.join(pages[page - 1])

    return s, len(pages) + 1
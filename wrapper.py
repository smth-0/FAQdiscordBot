import sqlite3

entry = sqlite3.connect("quotes.db")
cur = entry.cursor()
quotes_per_page = 10

print('wrapper library imported.')


def fetch_ID(id):
    res = cur.execute("""SELECT * FROM quotes WHERE msgID IS %s""" % id).fetchall()
    res = [(i[0].replace(r';!;', r"'"), i[1].replace(r';!;', r"'"), i[2], i[3], i[4], i[5]) for i in res]
    # print(res[0])
    return res



def add_quote(msg_obj):
    # reaction.message should be passed here
    text, usr, msgID, usr_id = msg_obj.content, str(msg_obj.author), msg_obj.id, msg_obj.author.id
    dateUTC, jumplink = msg_obj.created_at, msg_obj.jump_url

    # print(fetch_ID(msgID))
    if not fetch_ID(msgID):
      cur.execute(
          """INSERT INTO quotes(content, author, msgID, authorID, date, jumplink) VALUES('%s', '%s', '%s', '%s', '%s', '%s')""" %
          (text.replace(r"'", r";!;"), usr.replace(r"'", r";!;"), msgID, usr_id, dateUTC, jumplink))
      entry.commit()
      return True
    else:
      return False


def fecth_quote(tags=None):
    # tags - list of strings1
    if tags is None:
        return cur.execute("""SELECT * FROM quotes""").fetchall()
    tmp = []
    for tag in tags:
        tmp.append(r"content like '%{}%' ".format(tag))
    request = ' OR '.join(tmp)
    res = cur.execute("""SELECT * FROM quotes WHERE """ + request).fetchall()
    res = [(i[0].replace(r';!;', r"'"), i[1].replace(r';!;', r"'"), i[2], i[3], i[4], i[5]) for i in res]
    # print(res[0])
    return res


def book_renderer(search='none', results=None, page=0):
    if search == 'none' or search is None:
        search = ['no tags in search', ]
    tags_hud = '; '.join(search)

    quotes_hud = ""

    l, r = quotes_per_page * page, min((quotes_per_page * (page + 1)), len(results))
    if l > len(results):
        l = 0
    pagelen = len(results) // quotes_per_page
    page_results = results[l:r]

    for cur_quote in page_results:
        author, text = cur_quote[1], cur_quote[0].replace('\n', '\t')
        date, id = cur_quote[4][:16], cur_quote[2]

        quote_hud = """> <o>=============<%s>=============<o> [msgID:%s]
> **%s** - %s\n""" % (date, id, author, text)
        quotes_hud += quote_hud

    if pagelen:
        page_hud = "page %d from %d" % (page + 1, pagelen)
    else:
        page_hud = ""

    debug = """debug:
    l, r: %d, %d
    pagelen: %d
    len(): %d
    """ % (l, r, pagelen, len(results))

    hull = """quote search for [%s]:
> [ %s ]
> quotes:
%s
%s""" % (tags_hud, page_hud, quotes_hud, debug)
    return hull, pagelen

#!/usr/bin/python3

import feedparser
import subprocess
import datetime
import random
import sqlite3
#from kiwipiepy import Kiwi
#from PIL import Image
#import imagehash

now = datetime.datetime.now()

num_deleted = 0

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    # 26. 3. 25 
    cs.execute('''
        create table if not exists demo1 (
            id integer primary key, 
            url text not null, 
            title text not null, 
            lang text not null
        )
    ''')
    cs.execute('''
        delete from demo1 
    ''')

    cs.execute('''
        create table if not exists feeds (
            url text primary key, 
            title text not null, 
            lang text not null, 
            date text not null, 
            used integer
        )
    ''')

    f = feedparser.parse("https://www.yna.co.kr/rss/news.xml")
    # this is NOT their published date. 
    date = now.strftime("%Y-%m-%d-%H%M")
    for entry in f.entries[:3]: 
        cs.execute('''
            insert or ignore into feeds 
            (url, title, lang, date, used) 
            values (?, ?, ?, ?, ?)
        ''', 
        (entry.link, entry.title, 'ko', date, 0))
    ###################################### 
    #   SECRET  CODE S 2026. 3. 25 
    ###################################### 
    cs.execute('''
        select * from feeds 
        where url = "LAST" 
    ''')
    lasts = cs.fetchall()
    if (len(lasts) != 0): 
        lll = lasts[0]
        last = lll[1]
    else: 
        last = ""
    ###################################### 
    #   SECRET  CODE E 2026. 3. 25 
    ###################################### 
    cs.execute('''
        select * from feeds 
        where used = 0 
        order by date DESC
    ''')
    feeds = cs.fetchall()

    # 26. 4. 7 NEWSIS 
    cs.execute('''
        select url, title, lang, outlet from mixed 
        where used = 0 and outlet in ('NEWSIS', 'HILL', 'PBS', 'MSNBC', 'IRAN', 'NYT', 'GDN1', 'GDN2', 'GDN3', 'GDNC', 'FP', 'ET', 'DB', 'FOX') 
        order by date DESC
        limit 1
    ''')
    feeds_alt = cs.fetchall()
    # 26. 4. 5 TRY FETCHING FROM KOREAN OUTLETS FIRST! 
    if (len(feeds_alt) == 0): 
        cs.execute('''
            select url, title, lang, outlet from mixed 
            where used = 0 and outlet in ('HBIZ', 'KPOP') 
            order by date DESC
            limit 1
        ''')
        feeds_alt = cs.fetchall()
    # 26. 4. 12 STICK TO THE LAST! 
    if (len(feeds_alt) == 0): 
        cs.execute('''
            select url, title, lang, outlet from mixed 
            where used = 0 
            order by date DESC
            limit 1
        ''')
        feeds_alt = cs.fetchall()
#    if (len(feeds_alt) == 0): 
#        cs.execute('''
#            select url, title, lang, outlet from mixed 
#            where used = 0 and outlet in ('HBIZ', 'KPOP', 'PBS', 'SDOT', 'MSNBC', 'FOX', 'NDTV', 'IRAN') 
#            order by substr(date, 1, 13)+random() DESC
#            limit 1
#        ''')
#        feeds_alt = cs.fetchall()

    if (len(feeds_alt) != 0 and random.randint(0, 1) == 0): 
        prefer_alt = True
    else: 
        prefer_alt = False
    #
    # Mr. Miyajima's special magic1 S 
    #
    #if (len(feeds) != 0): 
    #    if ("中" in feeds[0][1] or "중국" in feeds[0][1]): 
    #        prefer_alt = True
    #
    # Mr. Miyajima's special magic1 E 
    #
    ###################################### 
    #   SECRET  CODE S 2026. 3. 25 
    ######################################
    if (len(feeds) != 0): 
        fff = feeds[0]
        print(fff[1])
        print(last)
        if (fff[1].rstrip() == last.rstrip()):  
            prefer_alt = True

    if (len(feeds) == 0 or prefer_alt): 
        # if yonhap news is unavailable for us now or, 
        # we feel like using some other news outlets, 
        # then try using one of them. 
        if (len(feeds_alt) == 0): 
            feed = f.entries[0]
            f_url = feed.link
            f_title = feed.title
            f_lang = "ko"
            f_outlet = "YNA"
        else: 
            feed = feeds_alt[0]
            f_url = feed[0]
            #f_title = '이걸 대신 사용: ' + feed[1]
            f_title = feed[1]
            f_lang = feed[2]
            f_outlet = feed[3]
            cs.execute('''
                update mixed set used = 1 
                where url = ? 
            ''', 
            (f_url,))
    else: 
        feed = feeds[0]
        f_url = feed[0]
        f_title = feed[1]
        f_lang = feed[2]
        f_outlet = "YNA"
        cs.execute('''
            update feeds set used = 1 
            where url = ? 
        ''', 
        (f_url,))
        ###################################### 
        #   SECRET  CODE S 2026. 3. 25 
        ###################################### 
        cs.execute('''
            insert or ignore into feeds 
            (url, title, lang, date, used) 
            values (?, ?, ?, ?, ?)
        ''', 
        ("LAST", entry.title, 'ko', "9999-99-99-9999", 1))
        ###################################### 
        #   SECRET  CODE E 2026. 3. 25 
        ###################################### 

    f_kiwi = ""
    # word (noun only) count using Kiwipiepy. 
#    f_kiwi = ""
#    if f_lang == "ko": 
#        cs.execute('''
#            create table if not exists stat1 (
#                word text primary key, 
#                count integer
#            )
#        ''')
#        kiwi = Kiwi()
#        tks = kiwi.tokenize(f_title)
#        for tk in tks: 
#            f_kiwi = f_kiwi + tk.form + " ; "   # 26. 4. 14 
#            if tk.tag == "NNG" or \
#               tk.tag == "NNP" or \
#               tk.tag == "NNB": 
#                w = tk.form
#                cs.execute('''
#                    insert or ignore into stat1 
#                    (word, count) 
#                    values (?, ?)
#                ''', 
#                (w, 0))
#                cs.execute('''
#                    update stat1 
#                    set count = count + 1 
#                    where word = ? 
#                ''', 
#                (w,))
#        f_kiwi = f_kiwi + "(Kiwipiepy로 분석된 일)"
#    else: 
#        pass

    # 26. 3. 25 
    cs.execute('''
        insert or ignore into demo1 
        (id, url, title, lang) 
        values (?, ?, ?, ?)
    ''', 
    (1, f_url, f_title, f_lang))

    # 26. 4. 7 
    if (f_outlet == "NEWSIS" or f_outlet == "YNA" 
        or f_outlet == "HILL" or f_outlet == "PBS" or f_outlet == "MSNBC" 
        or f_outlet == "IRAN" or f_outlet == "NYT" or f_outlet == "GDN1" 
        or f_outlet == "GDN2" or f_outlet == "GDN3" or f_outlet == "GDNC" 
        or f_outlet == "FP" or f_outlet == "ET" or f_outlet == "NDTV" 
        or f_outlet == "DB" or f_outlet == "SDOT" or f_outlet == "FOX"): 
        subprocess.run(["./newsis.sh", f_url])
    elif (f_lang == "en"): 
        subprocess.run(["./fox.sh", f_title])
    elif (f_outlet == "HBIZ" or f_outlet == "KPOP"): 
        subprocess.run(["wkhtmltoimage", "--width", "800", "--crop-y", "160", "--crop-h", "480", f_url, "bot_temp.png"])
    else: 
        # lang: ko (mostly) or others. 
        subprocess.run(["./mk.sh", f_title])

    subprocess.run(["right/getfed.sh", f_url, f_title, f_lang, f_title])
    # 26. 3. 27 
    #ihash = imagehash.phash(Image.open("bot_temp.png"))
    # 26. 3. 27 
    #cs.execute('''
    #    create table if not exists ihash (
    #        hash text primary key, 
    #        url text not null, 
    #        date text not null
    #    )
    #''')
    #cs.execute('''
    #    insert or ignore into ihash 
    #    (hash, url, date) 
    #    values (?, ?, ?)
    #''', 
    #(str(ihash), f_url, now.strftime("%Y-%m-%d-%H%M")))

    cn.commit();
    print("**************************************** STAGE1: OK")
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();



# top  
outlets = [
    {"lng": "ko", "nm": "KPOP","url": "https://www.heraldmuse.com/rss/google/newsAll"},
    {"lng": "ko", "nm": "CHOSUN1","url": "https://www.chosun.com/arc/outboundfeeds/rss/category/international/?outputType=xml"},
    {"lng": "ko", "nm": "CHOSUN2","url": "https://www.chosun.com/arc/outboundfeeds/rss/category/culture-life/?outputType=xml"},
    {"lng": "ko", "nm": "MK",     "url": "https://www.mk.co.kr/rss/40300001/"},
    {"lng": "ko", "nm": "HK",     "url": "https://www.hankyung.com/feed/all-news"},
    {"lng": "ko", "nm": "HBIZ",   "url": "https://biz.heraldcorp.com/rss/google/newsAll"},
#    {"lng": "ko", "nm": "NYT",    "url": "https://news-ex.jtbc.co.kr/v1/get/rss/newsflesh"},
#    {"lng": "ko", "nm": "GDN1",   "url": "https://news.sbs.co.kr/news/newsflashRssFeed.do?plink=RSSREADER"},
    {"lng": "ko", "nm": "GDN2",   "url": "https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=14&plink=RSSREADER"},
    {"lng": "ko", "nm": "GDN3",   "url": "https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=08&plink=RSSREADER"},
    {"lng": "ko", "nm": "GDNC",   "url": "https://news.sbs.co.kr/news/ReplayRssFeed.do?prog_cd=RJ&plink=RSSREADER"},
    {"lng": "ko", "nm": "HILL",   "url": "https://www.segye.com/Articles/RSSList/segye_recent.xml"},
    {"lng": "ko", "nm": "FOX",    "url": "https://www.imaeil.com/rss"},
    {"lng": "ko", "nm": "FP",     "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/society"},
    {"lng": "ko", "nm": "IRAN",   "url": "https://www.yonhapnewstv.co.kr/category/news/weather/feed/"},
    {"lng": "ko", "nm": "ET",     "url": "https://www.sedaily.com/rss/newsall"},
    {"lng": "ko", "nm": "NDTV",   "url": "https://rss.etoday.co.kr/eto/finance_news.xml"},
    {"lng": "ko", "nm": "DB",     "url": "https://news-ex.jtbc.co.kr/v1/get/rss/section/international"},
    {"lng": "ko", "nm": "PBS",    "url": "https://www.asiae.co.kr/rss/all.htm"},
    {"lng": "ko", "nm": "SDOT",   "url": "https://zdnet.co.kr/feed/"},
    {"lng": "ko", "nm": "MSNBC",  "url": "https://www.jjan.kr/news/rssAll"}
]
# 26. 3. 30 THIS MUST BE A FIXED 6-SIZED ARRAY. 
# 26. 3. 30 THIS MUST BE A FIXED 6-SIZED ARRAY. 
# 26. 3. 30 THIS MUST BE A FIXED 6-SIZED ARRAY. 
prime = [{"lng": "ko", "nm": "GDN1",   "url": "https://news.sbs.co.kr/news/newsflashRssFeed.do?plink=RSSREADER"},
         {"lng": "ko", "nm": "NYT",    "url": "https://news-ex.jtbc.co.kr/v1/get/rss/newsflesh"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/square.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/entertain.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/photo.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/sokbo.xml"}]
# 26. 3. 30 THIS MUST BE A FIXED 6-SIZED ARRAY. 
# 26. 3. 30 THIS MUST BE A FIXED 6-SIZED ARRAY. 
# 26. 3. 30 THIS MUST BE A FIXED 6-SIZED ARRAY. 

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    f_oletcd = "NONE"

    cs.execute('''
        create table if not exists mixed (
            url text primary key, 
            title text not null, 
            outlet text not null, 
            lang text not null, 
            date text not null, 
            used integer
        )
    ''')

    # 26. 4. 12 
    random.shuffle(outlets)
    # this is NOT their published date. 
    date = now.strftime("%Y-%m-%d-%H%M")
    #
    # BEWARE! NOW IT USES FIRST 6 OF SHUFFLED OUTLETS. SO BE CAREFUL OF NUMBERS 
    #
    for j in range(11): 
        if (j < 6): 
            #o = prime[random.randint(0, len(prime)-1)]
            # O, dirty code!!! 
            o = prime[j]
        else: 
            o = outlets[j-6]
        outlet_url  = o["url"]
        outlet_name = o["nm"]
        outlet_lang = o["lng"]
        f = feedparser.parse(outlet_url)
        for entry in f.entries[:8]: 
            if ("english" in entry.link): 
                pass
            else: 
                cs.execute('''
                    insert or ignore into mixed 
                    (url, title, outlet, lang, date, used) 
                    values (?, ?, ?, ?, ?, ?)
                ''', 
                (entry.link, entry.title, outlet_name, outlet_lang, date, 0))
 
    cs.execute('''
        select url, title, ifnull(outlets.name, mixed.outlet), 
               lang, date, used, mixed.outlet from mixed 
        left outer join outlets on mixed.outlet = outlets.code 
        where used = 0 and outlet <> 'NEWSIS' 
        order by date DESC
    ''')
    feeds = cs.fetchall()
    if (len(feeds) == 0): 
        feed = f.entries[0]
        f_url = feed.link
        f_title = feed.title
        f_outlet = outlet_name
        f_lang = outlet_lang
        f_oletcd = outlet_name
    else: 
        feed = feeds[0]
        f_url = feed[0]
        f_title = feed[1]
        f_outlet = feed[2]
        f_lang = feed[3]
        f_oletcd = feed[6]
        cs.execute('''
            update mixed set used = 1 
            where url = ? 
        ''', 
        (f_url,))

    # 26. 3. 25 
    cs.execute('''
        insert or ignore into demo1 
        (id, url, title, lang) 
        values (?, ?, ?, ?)
    ''', 
    (2, f_url, f_title, f_lang))
    # 26. 3. 27 
    # dirty code... 
    cs.execute('''
        insert or ignore into demo1 
        (id, url, title, lang) 
        values (?, ?, ?, ?)
    ''', 
    (3, f_oletcd, "", f_lang))

    subprocess.run(["top/getfed.sh", f_outlet, f_url, f_title, f_lang, f_oletcd])

    ###################################### 
    #   SECRET  CODE S 2026. 3. 25 
    ###################################### 
    hago = now + datetime.timedelta(minutes=-44)
    cs.execute('''
        delete from feeds 
        where date < ? 
   ''', (hago.strftime("%Y-%m-%d-%H%M"),))
    num_deleted = num_deleted + cs.rowcount
    tdago = now + datetime.timedelta(days=-3)
    cs.execute('''
        delete from mixed 
        where date < ? 
   ''', (tdago.strftime("%Y-%m-%d-%H%M"),))
    num_deleted = num_deleted + cs.rowcount
    ###################################### 
    #   SECRET  CODE E 2026. 3. 25 
    ###################################### 

    cn.commit();
    print("**************************************** STAGE2: OK")
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    # reset the left core. 
    subprocess.run(["left/getfed.sh"])

    thago = now + datetime.timedelta(minutes=-650)
    cs.execute('''
        select * from mixed 
        where used = 0 and date < ? 
        order by date ASC 
        limit 2 
    ''', (thago.strftime("%Y-%m-%d-%H%M"),))
    feeds = cs.fetchall()
    i = 4
    for feed in feeds: 
        url = feed[0]
        tit = feed[1]
        lang = feed[3]
        cs.execute('''
            update mixed set used = 1 
            where url = ? 
        ''', 
        (url,))
        cs.execute('''
            insert or ignore into demo1 
            (id, url, title, lang) 
            values (?, ?, ?, ?)
        ''', 
        (i, url, tit, lang))
        i = i + 1
        subprocess.run(["left/getfed.sh", url, tit, str(num_deleted)])

    cn.commit();
    print("**************************************** STAGE3: OK")
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();

try: 
    date = now.strftime("%Y-%m-%d-%H%M")
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    # 1. fetch 'em. 
    cs.execute('''
        select count(*) from feeds 
        group by date 
        having url <> "LAST" and date = ? 
        limit 1
    ''', 
    (date,))
    ynas = cs.fetchall()

    cs.execute('''
        select count(*) from mixed 
        group by outlet, date 
        having outlet = "NEWSIS" and date = ? 
        limit 1
    ''', 
    (date,))
    nwss = cs.fetchall()

    cs.execute('''
        select count(*) from mixed 
        where outlet <> "NEWSIS" 
        group by date 
        having date = ? 
        limit 1
    ''', 
    (date,))
    hbzs = cs.fetchall()

    # 2. count 'em. 
    if (len(ynas) == 0): 
        num_ynas = 0
    else: 
        num_ynas = ynas[0][0]
    if (len(nwss) == 0): 
        num_nwss = 0
    else: 
        num_nwss = nwss[0][0]
    if (len(hbzs) == 0): 
        num_hbzs = 0
    else: 
        num_hbzs = hbzs[0][0]

    # 3. record 'em. 
    cs.execute('''
        create table if not exists stat2 (
            date text primary key, 
            yna integer, 
            newsis integer, 
            hbiz integer
        )
    ''')
    cs.execute('''
        insert or ignore into stat2 
        (date, yna, newsis, hbiz) 
        values (?, ?, ?, ?)
    ''', 
    (date, num_ynas, num_nwss, num_hbzs))

    cn.commit();
    print("**************************************** STAGE4: OK")
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();


#!/usr/bin/python3

import feedparser
import datetime
import sqlite3

now = datetime.datetime.now()

yay = [ 
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/international.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/bank.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/society.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/met.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/sports.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/culture.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/politics.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/economy.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/industry.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/health.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/country.xml"},
         {"lng": "ko", "nm": "NEWSIS", "url": "https://www.newsis.com/RSS/newsiseyes.xml"},

         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/30000001/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/40300001/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/30100041/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/30200030/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/50400012/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/30300018/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/50100032/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/50200011/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/50300009/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/30000023/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/71000001/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/50700001/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/40200124/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/40200003/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/50000001/"},
         {"lng": "ko", "nm": "MK", "url": "https://www.mk.co.kr/rss/60000007/"},

         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/all-news"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/finance"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/economy"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/realestate"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/it"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/politics"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/international"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/society"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/life"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/opinion"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/sports"},
         {"lng": "ko", "nm": "HK", "url": "https://www.hankyung.com/feed/entertainment"},

         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/newsAll"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/economy"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/finance"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/realestate"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/industry"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/politics"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/society"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/world"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/bio"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/it"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/consumer"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/culture"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/opinion"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/entertainment"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/sports"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/honam"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/daegu"},
         {"lng": "ko", "nm": "HBIZ", "url": "https://biz.heraldcorp.com/rss/google/buk"},

         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/all.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/stock.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/economy.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/realestate.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/industry-IT.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/politics.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/society.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/world.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/life.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/opinion.htm"},
         {"lng": "ko", "nm": "PBS", "url": "https://www.asiae.co.kr/rss/nationwide.htm"},

         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/newsall"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/finance"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/realestate"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/economy"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/politics"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/society"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/international"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/it"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/opinion"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/life"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/sports"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/entertainment"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/sedin"},
         {"lng": "ko", "nm": "ET", "url": "https://www.sedaily.com/rss/artseeing"}
    ]

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    # this is NOT their published date. 
    date = now.strftime("%Y-%m-%d-%H%M")

    for y in yay: 
        print("Processing: " + y["url"])
        outlet_url  = y["url"]
        outlet_name = y["nm"]
        outlet_lang = y["lng"]
        f = feedparser.parse(outlet_url)
        for entry in f.entries[:5]: 
            if ("english" in entry.link): 
                pass
            else: 
                cs.execute('''
                    insert or ignore into mixed 
                    (url, title, outlet, lang, date, used) 
                    values (?, ?, ?, ?, ?, ?)
                ''', 
                (entry.link, entry.title, outlet_name, outlet_lang, date, 0))

    cn.commit();
    print("OK")
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();


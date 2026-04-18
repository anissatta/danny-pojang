#!/usr/bin/python3

import sqlite3

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select url, used, substr(date, 3, 8) from feeds
        where url <> 'LAST' 
        order by date DESC
        limit 4
    ''')
    feeds = cs.fetchall()
    print("( https://www.yna.co.kr/rss/news.xml )")
    for feed in feeds: 
        if (feed[1] == 0): 
            flag = " [USED:N] "
        else: 
            flag = " [USED:Y] "
        date = feed[2]
        print(date + flag + feed[0])

except Exception as e: 
    print(e)
finally: 
    cn.close();


#!/usr/bin/python3

import sqlite3
import datetime

now = datetime.datetime.now()
old = now + datetime.timedelta(minutes=-90)

num_fresh_yna = 0
num_fresh_newsis = 0
num_old_newsis = 0
num_fresh_hbiz = 0
num_old_hbiz = 0
num_fresh_fox = 0
num_old_fox = 0

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select date from feeds 
        where used = 0 
    ''')
    rs = cs.fetchall()
    num_fresh_yna = len(rs)

    print("\"연합뉴스\" " + str(num_fresh_yna))
    others = [
        "NEWSIS",
        "HBIZ",
        "FOX",
        "KPOP",
        "CHOSUN1",
        "CHOSUN2",
        "MK",
        "HK",
        "NYT",
        "GDN1",
        "GDN2",
        "GDN3",
        "GDNC",
        "HILL",
        "FP",
        "IRAN",
        "ET",
        "NDTV",
        "DB",
        "PBS",
        "SDOT",
        "MSNBC",
        "MISC"
    ]
    # 26. 4. 12 
    for o in others: 
        cs.execute('''
            select name from outlets 
            where code = ? 
        ''', (o,))
        rs = cs.fetchall()
        if (len(rs) == 0): 
            onm = o
        else: 
            onm = rs[0][0]

        cs.execute('''
            select date from mixed 
            where used = 0 and outlet = ? and date >= ? 
        ''', (o, old.strftime("%Y-%m-%d-%H%M"),))
        rs = cs.fetchall()
        num_fresh_o = len(rs)
        cs.execute('''
            select date from mixed 
            where used = 0 and outlet = ? and date < ? 
        ''', (o, old.strftime("%Y-%m-%d-%H%M"),))
        rs = cs.fetchall()
        num_old_o = len(rs)
        print("\"" + onm + "\" " + str(num_fresh_o))
        print("\"" + onm + ".O\" " + str(num_old_o))

except Exception as e: 
    print(e)
finally: 
    cn.close();


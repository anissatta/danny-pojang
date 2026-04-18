#!/usr/bin/python3

import subprocess
import sqlite3
import datetime

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select substring(date, 12, 4), yna, newsis, hbiz from stat2 
        order by date ASC 
    ''')
    rs = cs.fetchall()

    for r in rs: 
        print("\"" + r[0] + "\" " + str(r[1]) + " " + str(r[2]) + " " + str(r[3]))

    # clean up. S 
    now = datetime.datetime.now()
    evil = now + datetime.timedelta(minutes=-124)
    cs.execute('''
        delete from stat2 
        where date < ? 
    ''', (evil.strftime("%Y-%m-%d-%H%M"),))
    cn.commit()
    # clean up. E 

except Exception as e: 
    print(e)
finally: 
    cn.close();


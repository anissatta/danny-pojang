#!/usr/bin/python3

import sqlite3
import html

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select * from demo1 
        where id <> 3 
        order by id ASC 
        limit 5 
    ''')
    rs = cs.fetchall()

    i = 1
    for r in rs: 
        quoted1 = '"' + html.escape(r[1], quote=True) + '"'
        quoted2 = '"' + html.escape(r[2], quote=True) + '"'
        quoted3 = '"' + html.escape(r[3], quote=True) + '"'
        row = "["
        row += quoted1 + ", " + quoted2 + ", " + quoted3
        row += "]"
        if i < len(rs): 
            row += ","
        i = i + 1
        print(row)

except Exception as e: 
    print(e)
finally: 
    cn.close();


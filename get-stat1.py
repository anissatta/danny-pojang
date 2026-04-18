#!/usr/bin/python3

import sqlite3

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        select * from stat1 
        order by count DESC 
        limit 20
    ''')
    nouns = cs.fetchall()

    for i in range(len(nouns)): 
        noun = nouns[i]
        quoted = '"' + noun[0] + '"'
        row = "["
        row += quoted + ", " + str(noun[1])
        row += "]"
        if i < len(nouns)-1: 
            row += ","
        print(row)

except Exception as e: 
    print(e)
finally: 
    cn.close();


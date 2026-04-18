#!/usr/bin/python3

#import sys
import sqlite3

#if len(sys.argv) > 1: 
#    myurl = sys.argv[1]
try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    # use this one. 
    cs.execute('''
        select * from demo1 
        where id = ? 
    ''', (1,))
    rs = cs.fetchall()
    if (len(rs) != 1): 
        # It should not happen... 
        print("https://yna.co.kr")
    else: 
        myurl = rs[0][1]
        cs.execute('''
            select * from ihash 
            where url = ? 
            order by date DESC 
            limit 1
        ''', (myurl,))
        mines = cs.fetchall()
        if (len(mines) != 1): 
            # It should not happen... 
            print("https://yna.co.kr")
        else: 
            mine = mines[0]
            cs.execute('''
                select * from ihash 
                where url <> ? 
                order by date DESC 
                limit 333
            ''', (myurl,))
            yourses = cs.fetchall()
            shortest = 64
            shortest_one = "https://yna.co.kr"
            for yours in yourses: 
                myhash = int(mine[0], 16)
                urhash = int(yours[0], 16)
                # calculate the hamming distance. 
                hdist = bin(myhash ^ urhash).count("1")
                if (hdist < shortest): 
                    shortest = hdist
                    shortest_one = yours[1]
            print(shortest_one)
except Exception as e: 
    print(e)
finally: 
    cn.close();
#else: 
#    print("no arguments given")


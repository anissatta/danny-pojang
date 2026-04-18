#!/usr/bin/python3

import sqlite3

outlets = [
    {"cd": "NEWSIS", "nm": "뉴시스"},
    {"cd": "KPOP",   "nm": "헤럴드뮤즈"},
    {"cd": "CHOSUN1","nm": "조선일보.국제"},
    {"cd": "CHOSUN2","nm": "조선일보.문화"},
    {"cd": "MK",     "nm": "매일경제"},
    {"cd": "HK",     "nm": "한국경제"},
    {"cd": "HBIZ",   "nm": "헤럴드경제"},
    {"cd": "HILL",   "nm": "세계일보"},
    {"cd": "PBS",    "nm": "아시아경제"},
    {"cd": "FOX",    "nm": "매일신문"},
    {"cd": "SDOT",   "nm": "지디넷코리아"},
    {"cd": "DB",     "nm": "JTBC.국제"},
    {"cd": "NYT",    "nm": "JTBC.속보"},
    {"cd": "MSNBC",  "nm": "전북일보.전체"},
    {"cd": "IRAN",   "nm": "연뉴TV.날씨"},
    {"cd": "NDTV",   "nm": "이투데이.금융"},
    {"cd": "FP",     "nm": "JTBC.사회"},
    {"cd": "ET",     "nm": "서울경제"},
    {"cd": "GDN1",   "nm": "SBS뉴스.속보"},
    {"cd": "GDN2",   "nm": "SBS뉴스.연예"},
    {"cd": "GDN3",   "nm": "SBS뉴스.문화"},
    {"cd": "GDNC",   "nm": "SBS뉴스.TV"},
    {"cd": "MISC",   "nm": "기타"}
]

try: 
    cn = sqlite3.connect("turk.db")
    cs = cn.cursor()

    cs.execute('''
        create table if not exists outlets (
            code text primary key, 
            name text not null
        )
    ''')
    cs.execute('''
        delete from outlets 
    ''')
    for olet in outlets: 
        cs.execute('''
            insert into outlets 
            (code, name) 
            values (?, ?)
        ''', 
        (olet["cd"], olet["nm"]))

    cn.commit();
except Exception as e: 
    print(e)
    cn.rollback();
finally: 
    cn.close();


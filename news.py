#!/usr/bin/python3

import feedparser

try: 
    feed_url = "https://mycatiskorean.blogspot.com//feeds/posts/default"
    fp = feedparser.parse(feed_url)
    if (len(fp.entries) != 0): 
        latest = fp.entries[0]
        print(latest.title)
        print(latest.link)
    else: 
        print("ERROR: cannot fetch data")
except Exception as e: 
    print(e)


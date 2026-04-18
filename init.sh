#!/bin/sh

rm -f turk.db
python3 ./bot.py 2> /dev/null
python3 ./mk_outlets_mst.py
sh ./inst.sh
sh ./start.sh

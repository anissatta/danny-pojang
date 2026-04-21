#!/bin/bash

# as user, execute this script after step1.sh 
cd /home/user
wget git.io/trans
chmod +x ./trans
cd /home/user/danny-pojang
rm -f turk.db
python3 ./bot.py 2> /dev/null
python3 ./mk_outlets_mst.py
sh ./start.sh


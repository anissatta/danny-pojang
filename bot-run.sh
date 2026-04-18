#!/bin/sh

i=10764

while true
do
    ./bot.py
    ./bot-optional.sh $i
    ./kamsys-ng.sh $i

    i=$(($i+1))

    if [ -e ./last.sec ];then 
        last=$(cat ./last.sec)
    else 
        last=$(($(date "+%s")-90))
    fi

    now=$(date "+%s")
    delta=$((${now}-${last}))
    if [ $delta -gt 177 ]; then
        pillow=0
    else
        pillow=$((180-${delta}))
    fi
    echo "Last:  ${last}"
    echo "Now:   ${now}"
    echo "Delta: ${delta}"
    echo "Will sleep for ${pillow} seconds."

    sleep "${pillow}"
    date "+%s" > last.sec
done


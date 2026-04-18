#!/bin/sh 

dest=/home/user/danny-pojang/left/core

# if no arguments is specified, reset the core. 
if [ "$#" -eq 0 ]; then
    echo > $dest
else
    url=$1
    tit=$2
    del=$3
    echo '<div class="is-hidden">' >> $dest
    echo "${url}" >> $dest
    echo '</div>' >> $dest
    echo '<div class="is-hidden">' >> $dest
    echo "${tit}" >> $dest
    echo '</div>' >> $dest

    echo '<div class="is-delrows">' >> $dest
    echo "${del}" >> $dest
    echo '</div>' >> $dest
fi

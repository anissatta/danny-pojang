#!/bin/sh

page=$(shuf -i 1-1000 -n 1)
iurl=$(curl -s "https://www.10000recipe.com/recipe/list.html?order=date&page=${page}" | pup "a[class=common_sp_link] > img attr{src}" | shuf -n 1 -)

wget $iurl -O food_temp.jpg


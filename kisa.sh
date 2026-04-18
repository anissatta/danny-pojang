#!/bin/sh

./kisa.py > kisa.dat
gnuplot kisa.plot
convert kisa.png -negate kisa.png
convert kisa.png -alpha set -channel A -evaluate set 60% kisa.png


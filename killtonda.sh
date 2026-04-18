#!/bin/sh

./killtonda.py > killtonda.dat
gnuplot killtonda.plot
convert killtonda.png -alpha set -channel A -evaluate set 50% killtonda.png


#!/bin/sh

sudo apt-get update
sudo apt-get install git ffmpeg gnuplot
sudo apt-get install imagemagick
sudo apt-get install wget w3m
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-3.bookworm_amd64.deb


#!/bin/sh

sudo apt-get update
sudo apt-get install ffmpeg gnuplot
sudo apt-get install imagemagick figlet
sudo apt-get install wget w3m pup
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-3.bookworm_amd64.deb


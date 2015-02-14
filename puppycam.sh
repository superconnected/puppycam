#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
BASE=/home/pi/puppycam/website

raspistill -w 640 -h 480 -o $BASE/img/full/$DATE.jpg
convert $BASE/img/full/$DATE.jpg -resize 250x250 $BASE/img/thumbs/$DATE.jpg

python $BASE/generate_site.py

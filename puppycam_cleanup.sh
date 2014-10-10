#!/bin/bash

find /home/pi/puppycam/website/static/img/thumbnails/*.jpg -mtime +5 -exec rm -f {} \;
find /home/pi/puppycam/website/static/img/full/*.jpg -mtime +5 -exec rm -f {} \;

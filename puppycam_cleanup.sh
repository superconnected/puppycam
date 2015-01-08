#!/bin/bash

find /home/pi/puppycam/website/img/thumbs/*.jpg -mtime +5 -exec rm -f {} \;
find /home/pi/puppycam/website/img/full/*.jpg -mtime +5 -exec rm -f {} \;

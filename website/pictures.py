import os
import re
from itertools import groupby
import time

def pictures(img_path=None):
	"""Get all the .jpg images in the given path (or static/img if no path is provided)"""
	if img_path is None:
		img_path = os.path.join(os.path.dirname(__file__), 'static/img')
	pics = [pic for pic in os.listdir(img_path) if pic.endswith('.jpg')]
	return pics
	
def day_for_picture(pic):
	"""Get the day the picture was taken in YYYY-MM-DD format"""
	if pic is None:
		return None
	filename = os.path.basename(pic)
	day = re.search('\d{4}-\d{2}-\d{2}', filename)
	if day:
		return day.group(0)
	else:
		return None
		
def pretty_day(day):
	"""Get the day in a nice format"""
	if day is None:
		return None
	t = time.strptime(day, "%Y-%m-%d")
	return time.strftime("%A, %b %d, %Y", t)
	
def pictures_by_day(pics=None):
	"""Get a dictionary of days and the pictures for that day"""
	days = {}
	if pics is None:
		pics = pictures()
	if pics is None or len(pics) == 0:
		return days
	
	pics = sorted(pics, key=day_for_picture)
	for k, g in groupby(pics, day_for_picture):
		days[k] = list(g)
	return days
	
def time_for_picture(pic):
	"""Get the time for the picture in a nice format"""
	if pic is None:
		return None
	filename = os.path.basename(pic)
	pic_time = re.search('(\d{6}).jpg', filename)
	if pic_time:
		t = time.strptime(pic_time.group(1), "%H%M%S")
		return time.strftime("%I:%M %p", t).lstrip('0')
	else:
		return None
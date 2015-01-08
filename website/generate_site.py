import os
import re
from itertools import groupby
import time
from string import Template

class SiteGenerator(object):
	"""Reads image directories and generates web pages for listing"""
	def __init__(self):
		self.current_dir = os.path.dirname(__file__)
		self.layout_template = self.template('layout')
		self.list_template = self.template('list')
		self.day_template = self.template('day')
		self.pic_template = self.template('pic')
		self.pics_by_day = self.pictures_by_day()
		
	def template(self, name):
		"""Creates a string template from the given file contents"""
		template_path = os.path.join(self.current_dir, '_templates/' + name + '.html')
		temp = None
		with open(template_path, 'r') as template_file:
			temp = Template(template_file.read())
		return temp

	def pictures(self):
		"""Get all the .jpg images in the thumbnails path"""
		img_path = os.path.join(os.path.dirname(__file__), 'img/thumbs')
		if not os.path.isdir(img_path):
			return None
		pics = [pic for pic in os.listdir(img_path) if pic.endswith('.jpg')]
		return pics
	
	def day_for_picture(self, pic):
		"""Get the day the picture was taken in YYYY-MM-DD format"""
		if pic is None:
			return None
		filename = os.path.basename(pic)
		day = re.search('\d{4}-\d{2}-\d{2}', filename)
		if day:
			return day.group(0)
		else:
			return None
		
	def pretty_day(self, day):
		"""Get the day in a nice format"""
		if day is None:
			return None
		t = time.strptime(day, "%Y-%m-%d")
		return time.strftime("%A, %b %d, %Y", t)
	
	def pictures_by_day(self, pics=None):
		"""Get a dictionary of days and the pictures for that day"""
		days = {}
		if pics is None:
			pics = self.pictures()
		if pics is None or len(pics) == 0:
			return days
	
		pics = sorted(pics, key=self.day_for_picture)
		for k, g in groupby(pics, self.day_for_picture):
			days[k] = list(g)
		return days
	
	def time_for_picture(self, pic):
		"""Get the time for the picture in a nice format"""
		if pic is None:
			return None
		filename = os.path.basename(pic)
		pic_time = re.search('_(\d{6}).jpg', filename)
		if pic_time:
			t = time.strptime(pic_time.group(1), "%H%M%S")
			return time.strftime("%I:%M %p", t).lstrip('0')
		else:
			return None

	def build_list_page(self):
		"""Builds the HTML for the list of days"""
		days_html = []
		for key in reversed(sorted(self.pics_by_day)):
			latest = sorted(self.pics_by_day[key])[-1]
			days_html.append(self.pic_template.substitute({'link': key + '.html', 'pic': latest, 'time': self.pretty_day(key)}))
		list_html = self.list_template.substitute({'days': ''.join(days_html)})
		page_html = self.layout_template.substitute({'body': list_html})
		filename = os.path.join(self.current_dir, 'list.html')
		with open(filename, 'w') as list_file:
			list_file.write(page_html)

	def build_day_pages(self):
		"""Builds the HTML for each single day"""
		for key in self.pics_by_day:
			pics_html = []
			pics = reversed(sorted(self.pics_by_day[key]))
			for pic in pics:
				pics_html.append(self.pic_template.substitute({'link': 'img/full/' + pic, 'pic': pic, 'time': self.time_for_picture(pic)}))
			day_name = self.pretty_day(key)
			day_html = self.day_template.substitute({'dayName': day_name, 'pics': ''.join(pics_html)})
			day_page_html = self.layout_template.substitute({'body': day_html})
			filename = os.path.join(self.current_dir, key + '.html')
			with open(filename, 'w') as day_file:
				day_file.write(day_page_html)
				
	def prune_day_pages(self):
		"""Removes day pages so that old pages won't stick around after that day's pics are deleted"""
		day_pages = [path for path in os.listdir(self.current_dir) if re.search('\d{4}-\d{2}-\d{2}\.html', path)]
		for page in day_pages:
			os.remove(page)
	
	def generate_site(self):
		"""Generates the main listing page and pages for each day"""
		self.prune_day_pages()
		self.build_list_page()
		self.build_day_pages()



if __name__ == '__main__':
	generator = SiteGenerator()
	generator.generate_site()
	






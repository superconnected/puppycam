import unittest
from ..generate_site import SiteGenerator

class SiteGeneratorTests(unittest.TestCase):
	def setUp(self):
		self.sut = SiteGenerator()
	
	def test_day_for_picture_returns_day(self):
		day = self.sut.day_for_picture('path/to/pics/2015-01-01_120000.jpg')
		self.assertEqual('2015-01-01', day)
		
	def test_pretty_day_returns_date(self):
		day = self.sut.pretty_day('2015-01-01')
		self.assertEqual('Thursday, Jan 01, 2015', day)
		
	def test_time_for_picture_returns_time(self):
		time = self.sut.time_for_picture('path/to/pics/2015-01-01_120000.jpg')
		self.assertEqual('12:00 PM', time)
	
	def test_pictures_by_day_returns_valid_dict(self):
		pics = ['/pics/2014-09-10_2240001.jpg', '/pics/2014-09-10_2250001.jpg', '/pics/2014-09-11_080001.jpg']
		days = self.sut.pictures_by_day(pics)
		self.assertEqual(len(days), 2)
		self.assertEqual(len(days['2014-09-10']), 2)
		self.assertEqual(len(days['2014-09-11']), 1)

if __name__ == '__main__':
	unittest.main()

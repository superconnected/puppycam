from nose.tools import assert_true, assert_equal
from .. import pictures

# def test_pictures_returns_data():
# 	pics = pictures.pictures()
# 	assert_true(len(pics) > 0)

def test_day_for_picture_returns_day():
	pic = '/path/to/pics/2014-09-10_225001.jpg'
	day = pictures.day_for_picture(pic)
	assert_equal(day, '2014-09-10')
	
def test_pretty_day_returns_day():
	day = pictures.pretty_day('2014-09-10')
	assert_equal(day, 'Wednesday, Sep 10, 2014')
	
def test_pictures_by_day_returns_valid_dict():
	pics = ['/pics/2014-09-10_2240001.jpg', '/pics/2014-09-10_2250001.jpg', '/pics/2014-09-11_080001.jpg']
	days = pictures.pictures_by_day(pics)
	assert_equal(len(days), 2)
	assert_equal(len(days['2014-09-10']), 2)
	assert_equal(len(days['2014-09-11']), 1)
	
def test_time_for_picture_returns_time():
	pic = '/path/to/pics/2014-09-10_225001.jpg'
	time = pictures.time_for_picture(pic)
	assert_equal(time, '10:50 PM')
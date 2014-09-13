from flask import render_template
from website import app
import pictures

@app.route("/")
@app.route("/list")
def list():
	pics_by_day = pictures.pictures_by_day()
	days = {}
	latest_pics = {}
	for key in pics_by_day:
		days[key] = pictures.pretty_day(key)
		latest_pics[key] = sorted(pics_by_day[key])[-1]
	templateData = {
		'days': days,
		'latest_pics': latest_pics
	}
	return render_template('list.html', **templateData)
	
@app.route("/<day>")
def day(day):
	pics = sorted(pictures.pictures_by_day()[day])
	pics.reverse()
	times = {}
	for pic in pics:
		times[pic] = pictures.time_for_picture(pic)
	templateData = {
		'day': pictures.pretty_day(day),
		'pictures': pics,
		'times': times
	}
	return render_template('day.html', **templateData)


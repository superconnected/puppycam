from flask import render_template
from website import app
import pictures

@app.route("/")
@app.route("/list")
def list():
	pics_by_day = pictures.pictures_by_day()
	days = []
	for key in pics_by_day:
		pretty_day = pictures.pretty_day(key)
		latest = sorted(pics_by_day[key])[-1]
		days.append((key, pretty_day, latest))
	days = sorted(days, key=lambda day: day[0], reverse=True)
	return render_template('list.html', days=days)
	
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


import pywapi
import time

def getWeather(location):
	"""
	Gets the weather from Google.
	"""
	googleWeather = pywapi.get_weather_from_google(location)
	condition = googleWeather['current_conditions']['condition']
	temp = googleWeather['current_conditions']['temp_c']
	return "Weather: " + condition + ", " + temp + "c" + "\n"

def takeSnapshot():
	"""
	Makes a new file named after the timestamp it was created at and records the weather.
	"""
	# get current time.
	currentTime = int(time.time())
	# make and open new file for that time.
	newFile = open("hu-notes/hu-" + str(currentTime), "w")
	# put weather in file.
	weather = getWeather("brisbane,australia")
	newFile.write(weather)
	# close the file.
	newFile.close()
	
takeSnapshot()
	
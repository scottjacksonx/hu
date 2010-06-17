location = "brisbane,australia"

import pywapi

def getData():
	"""
	gets the weather at the specified location.
	"""
	
	try:
		googleWeather = pywapi.get_weather_from_google(location)
		condition = googleWeather['current_conditions']['condition']
		temp = googleWeather['current_conditions']['temp_c']
		return "<weather location=\"" + location + "\" condition=\"" + condition + "\" temp=\"" + temp + "c" + "\"/>"
	except:
		return ""
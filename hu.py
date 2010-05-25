import pywapi
import time
import pylast as lastfm

def getWeather(location):
	"""
	Gets the weather from Google.
	"""
	googleWeather = pywapi.get_weather_from_google(location)
	condition = googleWeather['current_conditions']['condition']
	temp = googleWeather['current_conditions']['temp_c']
	return "Weather: " + condition + ", " + temp + "c" + "\n"
	
def getRecentTracks(username):
	"""
	Gets recently-listened-to tracks from Last.fm
	"""
	apiKey = "fd4197bb1bfc8521ced2ba81d70fd812"
	network = lastfm.get_lastfm_network(api_key = apiKey, username = username)
	user = lastfm.User(username, network)
	recentTracks = user.get_recent_tracks(20)
	# get rid of any tracks with a play-time earlier than fifteen minutes ago.
	return recentTracks
	

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
	
	tracks = getRecentTracks("scottjacksonx")
	for track in tracks:
		newFile.write("Track: " + str(track[0]) + " | " + str(track[2]) + "\n")
	
	newFile.close()
	
takeSnapshot()
	
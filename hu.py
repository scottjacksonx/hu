import pywapi
import time
import datetime
import pylast as lastfm
import os
import commands

myLocation = "brisbane,australia"
myLastFmUsername = "scottjacksonx"
myBrowser = "safari"

def getWeather(location):
	"""
	Gets the weather from Google.
	"""
	googleWeather = pywapi.get_weather_from_google(location)
	condition = googleWeather['current_conditions']['condition']
	temp = googleWeather['current_conditions']['temp_c']
	return "Weather: " + condition + ", " + temp + "c"
	
def getCurrentlyPlaying():
	"""
	Gets the currently-playing track from iTunes.
	"""
	return commands.getoutput("osascript scripts/currentlyPlaying.applescript")
	
def getRecentTracks(username):
	"""
	Gets recently-listened-to tracks from Last.fm
	"""
	apiKey = "fd4197bb1bfc8521ced2ba81d70fd812"
	network = lastfm.get_lastfm_network(api_key = apiKey, username = username)
	user = lastfm.User(username, network)
	recentTracks = user.get_recent_tracks(20)
	tracksFromLastTenMinutes = []
	# get rid of any tracks with a play-time earlier than fifteen minutes ago.
	
	for track in recentTracks:
		now = time.time()
		if int(track[2]) + 600 > now:	# track was played < 10 minutes (600 seconds) ago.
			tracksFromLastTenMinutes.append(track)
	
	return tracksFromLastTenMinutes
	
def getOpenBrowserTabs(browser):
	"""
	Gets the title and URL of every tab open in the specified web browser.
	"""
	return commands.getoutput("osascript scripts/urls.applescript")
	
	

def takeSnapshot():
	"""
	Makes a new file named after the timestamp it was created at and records the weather and recently-listened-to tracks.
	"""
	# get current time.
	currentTime = int(time.time())
	# make and open new file for that time.
	newFile = open("hu-notes/hu-" + str(currentTime), "w")
	
	# put time in file
	snapshotTime = str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
	newFile.write(snapshotTime + "\n")
	
	# put weather in file.
	newFile.write(getWeather(myLocation) + "\n")
	
	# put current track in file.
	newFile.write("Now Playing: " + str(getCurrentlyPlaying()) + "\n\n")
	
	tracks = getRecentTracks(myLastFmUsername)
	for track in tracks:
		newFile.write("Recently Played: " + str(track[0]) + " | listened at " + str(track[2]) + "\n")
		
	newFile.write("\n")
	
	# put current tabs in file.
	newFile.write(str(getOpenBrowserTabs(myBrowser)))
	
	newFile.close()
	
takeSnapshot()
	
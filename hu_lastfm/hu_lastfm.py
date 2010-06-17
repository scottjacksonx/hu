lastfm_username="scottjacksonx"

import pylast as lastfm
import time
from unicodedata import decomposition

def getData():
	"""
	gets any lastfm listening statistics for the last ten minutes.
	
	and then judges you. wait, no -- that's in a future version of hu.
	"""
	try:
		apiKey = "fd4197bb1bfc8521ced2ba81d70fd812"
		network = lastfm.get_lastfm_network(api_key = apiKey, username = lastfm_username)
		user = lastfm.User(lastfm_username, network)
		recentTracks = user.get_recent_tracks(20)
		tracksFromLastTenMinutes = []
		# get rid of any tracks with a play-time earlier than fifteen minutes ago.
	
		for track in recentTracks:
			now = time.time()
			if int(track[2]) + 600 > now:	# track was played < 10 minutes (600 seconds) ago.
				tracksFromLastTenMinutes.append(track)
		return xmlify(tracksFromLastTenMinutes)
	else:
		return ""
	

	
def xmlify(tracks):
	"""
	takes a list of Tracks, turns them into a nice XML-ish format.
	"""
	if len(tracks) != 0:
		xmlifiedTracks = "<lastfm>\n"
		for track in tracks:
			trackDetails = u''
			trackDetails = asciify(unicode(str(track[0])))
			artistNameEnd = trackDetails.find(" - ")
			artistName = trackDetails[:artistNameEnd]
			startTitleName = artistNameEnd + 3
			titleName = trackDetails[startTitleName:]
		
			artist = "artist=\"" + artistName + "\" "
			title = "title=\"" + titleName + "\" "
			timestamp = "time=\"" + track[2] + "\" "
		
			convertedTrack = "<track " +  artist + title + timestamp + "/>\n"
			xmlifiedTracks += convertedTrack
		xmlifiedTracks += "</lastfm>"
		return xmlifiedTracks
	else:
		return ""
	
def asciify(string):
	"""
	gets rid of pesky things like umlauts and tildes and other accents. ascii all the way, baby.
	"""
	temp = u'' 
	for char in string:
		decomp = decomposition(char)
		if decomp: # Not an empty string 
			temp += unichr(int(decomp.split()[0], 16))
		else:
			temp += char
	return temp
import commands

def getData():
	"""
	gets the currently-playing track from iTunes.
	"""
	track = commands.getoutput("osascript hu_currentlyplaying/currentlyPlaying.applescript")
	if track[0:12] == "hu_currently":
		return ""
	return track
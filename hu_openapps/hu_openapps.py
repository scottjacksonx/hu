import commands

def getData():
	"""
	Gets the name of every open (and visible (i.e. not hidden)) application.
	"""
	openApps = commands.getoutput("osascript hu_openapps/openapps.applescript")
	if openApps[0:11] != "hu_openapps":
		return "<applications>\n" + openApps + "</applications>"
	return ""
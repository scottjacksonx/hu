import commands

def getData():
	"""
	Returns the name of the SSID of the network the computer is currently connected to.
	"""
	ssid = commands.getoutput("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I|grep \" SSID: \"|cut -c 18-")
	if ssid != "":
		return "<ssid name=\"" + ssid + "\" />"
	return ""
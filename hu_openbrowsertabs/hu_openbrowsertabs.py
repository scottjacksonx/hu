import commands

def getData():
	"""
	Gets the title and URL of every tab open in the specified web browser.
	"""
	urls = commands.getoutput("osascript hu_openbrowsertabs/urls.applescript")
	if urls[0:18] != "hu_openbrowsertabs":
		return "<browser>\n" + urls + "</browser>"
	return ""
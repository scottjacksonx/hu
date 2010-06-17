# Plugin declarations

plugin_modules = []
import hu_currentlyplaying.hu_currentlyplaying
plugin_modules.append(hu_currentlyplaying.hu_currentlyplaying)

import hu_lastfm.hu_lastfm
plugin_modules.append(hu_lastfm.hu_lastfm)

import hu_googleweather.hu_googleweather
plugin_modules.append(hu_googleweather.hu_googleweather)

import hu_ssidname.hu_ssidname
plugin_modules.append(hu_ssidname.hu_ssidname)

import hu_openbrowsertabs.hu_openbrowsertabs
plugin_modules.append(hu_openbrowsertabs.hu_openbrowsertabs)

import hu_openapps.hu_openapps
plugin_modules.append(hu_openapps.hu_openapps)

# End plugin declarations

import datetime
import time

class hu:
	"""
	i'm hu. i'm a big, important class. i watch you and i take notes.
	
	i hope you like me.
	"""
	
	def takeSnapshot(self):
		"""
		this is the part where i look at all of the things you want me to record.
		
		i look at the things, take a reading for each of them, and record them.
		
		hopefully.
		"""
		snapshot = "<entry time=\""
		snapshotTime = str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
		snapshot += snapshotTime + "\">\n"
		
		for plugin in plugin_modules:
			entryData = plugin.getData()
			if entryData != "":
				snapshot += str(entryData + "\n")
		snapshot += "</entry>"
		print snapshot
		return snapshot
	
	
	def writeSnapshotToLogFile(self, anEntry):
		"""
		this is the bit where i write the things down in my big book.
		
		if you want me to write down something secret, it's ok -- i won't tell.
		
		promise.
		"""
		try:
			logFile = open("hu-notes.txt", "r")
			currentLog = logFile.readlines()
			logFile.close()
		except:
			currentLog = []
		logFile = open("hu-notes.txt", "w")
		logFile.write("<hu>\n")
		for i in range(1, len(currentLog) - 1):
			logFile.write(currentLog[i])
		logFile.write(anEntry)
		logFile.write("\n</hu>")
		logFile.close()
			
			
		
			
hu = hu()
snapshot = hu.takeSnapshot()
hu.writeSnapshotToLogFile(snapshot)
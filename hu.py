import datetime
import time
import os

class hu:
	
	"""
	i'm hu. i'm a big, important class. i watch you and i take notes.
	
	i hope you like me.
	"""
	plugin_modules = []
	
	def __init__(self):
		"""
		hello, world.
		
		this is the part where i find out all of the things you want me to record.
		"""
		
		# get names of all folders in the current directory that start with "hu_"
		for file in os.listdir("."):
			if file[0:3] == "hu_":
				exec "import " + file + "." + file
				exec "self.plugin_modules.append(" + file + "." + file + ")"
	
	def takeSnapshot(self):
		"""
		this is the part where i look at all of the things you want me to record.
		
		i look at the things, take a reading for each of them, and record them.
		
		hopefully.
		"""
		snapshot = "<entry time=\""
		snapshotTime = str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
		snapshot += snapshotTime + "\">\n"
		
		for plugin in self.plugin_modules:
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
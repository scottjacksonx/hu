tell application "System Events"
	set theApps to (name of every process whose visible is true and name is not "Finder" and name is not (my name as text))
	set appList to ""
	repeat with appName in theApps
		set appList to appList & "<app name=\"" & appName & "\" />\n"
	end repeat
	get appList
end tell
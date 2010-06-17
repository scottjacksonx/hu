tell application "iTunes"
	get "<currentlyplaying artist=\"" & artist of current track & "\" title=\"" & name of current track & "\" />"
end tell
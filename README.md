# Hu #

>"Smells like fish," Scheme said.  
>Another splotch of ink.  
>"You're writing this down, right Hu?"  
>*What?*  
>"My observations. What I eat and drink. Smells. You're supposed to be taking notes."  
>*Oh. Right.* (Another splotch.) *Wait, why?*  
>"You never see the pattern as it's happening. Once, I kept track of everything I ate for six months and found out I had Thai food every nine days, like clockwork."  
>I started retroactively building a database. Although it only had one entry: an espresso at the Black Danube --  
>"And I want to correlate everything. When do I have the best ideas? When am I clever, and conversely, when can't I form a complete sentence? What have I been eating, drinking, absorbing? How much have I been sleeping?"  

-- *Annabel Scheme*, by Robin Sloan.

HUGIN-19.LG.GRAILGRID.NET (a.k.a. Hu) is the narrator of Robin Sloan's *Annabel Scheme*. In the section above, we see the kinds of things that Hu is capable of doing and recording.

I want to make Hu. A rudimentary version of Hu, sure, but Hu nonetheless. Every ten minutes or so, I want my computer to take a snapshot of what's going on -- what time it is, what software I have open, what websites I'm looking at, how many unread items are in my RSS reader, how many unread emails I have, what music I've been listening to, which files are open, how long/big those files are (to track my work's progress), what the weather's like, what I've eaten (via services like Daytum), etc. From there, I can look at trends, graph things, measure things, and spot patterns.

What's more, I want this thing to have a plugin architecture -- after all:

> *I can interface with anything! I'm infinitely extensible...*

Want Hu to record how many items are in your trash can? Write a little bit of code that checks how many items are in the trash can and tell Hu you want that data recorded. Ditto for recording your weight. Or your computer's remaining battery life. Or how many events are on your calendar for today ("do I work better when I've got long stretches of time to work in, or do I get work well in little chunks?").

This is all wishlist stuff, though. I'm hoping to get the basics done (what time it is, software open, websites I'm looking at, music I've been listening to, etc.) in a few weeks, then move on to making Hu extensible. If I get that done, the sky's the limit.

# The Plan #

This section is really only for me, but you can take a look at it to see what the roadmap for Hu looks like.

- Get Hu to record the time.
- Get Hu to record which apps I have open.
- Get Hu to record what music I've been listening to.
- Get Hu to record what websites I'm visiting.
- Get Hu to record which files are open and how long/big they are.
- Get Hu to record what the weather's like.
- Get Hu to be extensible.

# Administrivia #

I plan on making Hu on my Mac, and as such, there might be some Mac-specific stuff going on (using AppleScript to get the URLs of open tabs in a web browser, for example). We'll see what happens there. I also plan on making Hu a command-line thing for now. If I'm persuaded to, I might make it into a menubar app for Mac OS X, but someone else would have to write a system tray app for Windows users.
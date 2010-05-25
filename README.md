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

HUGIN-19.LG.GRAILGRID.NET (a.k.a. Hu) is the narrator of Robin Sloan's *Annabel Scheme*. In the section above, we see the kinds of things that Hu, an AI Watson to Scheme's Holmes, is capable of doing and recording.

**I want to make Hu.** A rudimentary version of Hu, sure, but Hu nonetheless. Every ten minutes, I want my computer to take a snapshot of what's going on -- what time it is, what software I have open, what websites I'm looking at, how many unread emails I have, what music I've been listening to, which files are open, how long/big those files are (to track my work's progress), what the weather's like, what I've eaten (via services like Daytum), etc. From there, I can look at trends, graph things, measure things, and try to spot patterns.

What's more, I want this thing to have a plugin architecture -- after all:

> *I can interface with anything! I'm infinitely extensible...*

Want Hu to record how many items are in your trash can? Write a little bit of code that checks how many items are in the trash can and tell Hu you want that data recorded. Ditto for recording your weight. Or your computer's remaining battery life. Or how many events are on your calendar for today ("do I work better when I've got long stretches of time to work in, or do I get work well in little chunks?").

This is all wishlist stuff, though. Don't get your hopes up too high just yet.

# Using Hu #

Hu is a little bit delicate at the moment. To use Hu, [download the source](http://github.com/scottjacksonx/hu/zipball/master), change your values at the top of `hu.py` and run `$ python hu.py`. Everything Hu captures will be stored in `hu-notes.txt`.

# The Potential #

Once Hu has a bunch of information about you, here are the kinds of things you can start to ask:

- What application do I spend the most time in? Find the most commonly occurring application on the "Current application" line.
- What websites do I visit the most often? Get the most frequently-appearing domain.
- How does the weather affect the kind of music I listen to? Compare the list of songs you listened to when the weather was "Cloudy" to the songs you listened to when the weather was "Fine."
- What time of day do I listen to music most at? See how many songs I listened to between 6pm and 12am and compare that number with how many songs I listened to between 9am and 3pm.

At the moment, you have to ask those questions at the command-line using your `sed`, `awk` and `grep` fu. I might make searching and querying Hu a bit easier later on, but until then, you'll have to speak bleep-blorp like a robot.

# Progress #

So far, Hu records the following things:

- the current time,
- what the weather's like, 
- the currently-playing track in iTunes,
- which application is currently active (i.e. front-most),
- recently played tracks on Last.fm,
- currently opened tabs in Safari.

I've only been working on Hu for a bit, so excuse the short feature list for now.




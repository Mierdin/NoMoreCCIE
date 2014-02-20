#Copyright (C) 2013 Matt Oswalt (http://keepingitclassless.net/) 
#Obviously humorous and meant to be taken as such.

import webbrowser

answer = raw_input("Can you use a GUI? (yes/no/huh/hello)")

if answer == 'no':
	webbrowser.open_new('http://www.opendaylight.org/')
elif answer == 'yes':
	print "Congratulations! You're a networking expert!"
elif answer == "hello":
	print "I see that you are in management. Go fire some CCIEs or something."
elif answer == "huh":
	print "What's a goooey ?"

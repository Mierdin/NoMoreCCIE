#Copyright (C) 2013 Matt Oswalt (http://keepingitclassless.net/) 
#Obviously humorous and meant to be taken as such.

#Test Comment

class CCIE:
    '''A class to describe a CCIE-certified engineer'''
    def __init__(self):
        self.name = ''
        self.salary = ''
        self.iq = ''
        self.homeless = True

    def setName(self, name=''):
        self.name = name


thisCCIE = CCIE()
thisCCIE.setName(raw_input('Please enter your name.'))

answer = raw_input("Can you use a GUI? (yes/no/huh)")

if answer == 'no':
    print "That's awkward."
    thisCCIE.homeless = True
elif answer == 'yes':
    print "Congratulations! You're a networking expert!"
    thisCCIE.salary = 1000000000
    thisCCIE.iq = 42
elif answer == "hello?":
    print "I see that you are in management. Go fire some CCIEs or something."
elif answer == "huh":
    print "What's a goooey ?"
    thisCCIE.homeless = True

#!/usr/bin/env python3

class MyTime():
    """ Define Time class to record the time everyday """
    
    def __init__(self, hrs = 0, mins = 0, secs = 0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs
   
    def __str__(self):
        return "({0}:{1}:{2})".format(self.hrs, self.mins, self.secs)

    def to_seconds(self):
        """ Return the number of seconds represented by this instance """
        return self.hours*3600 + self.minutes*60 + self.seconds



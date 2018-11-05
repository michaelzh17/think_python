#!/usr/bin/env python3

class SMS_store():
    """ Create a SMS message """
    def __init__(self, from_number, time_arrived, text_of_SMS):
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        self.has_been_reviewed = False

    def add_new_arrival(self):
        """ Making new message tuple, inserts it after other messages """
        pass
    
    def message_count(self):
        """ Return the number of sms messages in inbox """
        pass
    
    def get_unread_indexes(self):
        """ Return list of indexes of all not yet reviewed sms messages """
        pass

    def get_message(self, i):
        """ Return message (from_number, time_arrived, text_of_SMS)  of index[i] """
        pass

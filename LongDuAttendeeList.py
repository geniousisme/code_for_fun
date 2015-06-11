#!/usr/bin/env python
# coding:utf-8

# Chris: Implement the length limited list on python with LongDu event scenario.
# take some reference from this link: 
# http://stackoverflow.com/questions/17526659/how-to-set-a-max-length-for-a-python-list-set 

import uniout

class ToldYouRegisterEarlyBitchError(Exception):
      pass

class ToldYouDontRegisterTwiceBitchError(Exception):
      pass

class LongDuAttendeeList(list):
      def __init__(self):
          self.attendee_bound = 11
      
      def _check_attendee_bound(self):
          if len(self) > self.attendee_bound:
             raise ToldYouRegisterEarlyBitchError()

      def register(self, person):
          self._check_attendee_bound()
          if person in self:
             raise ToldYouDontRegisterTwiceBitchError()
          else:
             self.append(person)

      def show_attendee(self):
          print [person for person in self]

if __name__ == '__main__':
   l = LongDuAttendeeList()
   l.register('許家豪')
   l.show_attendee()

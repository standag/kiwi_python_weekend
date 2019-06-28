from __future__ import print_function
import sys, os, time
greetings =  'Hello'
name="Standa"
print("{greetings} {name}!".format( greetings=greetings,name = name ))
class Example:
    def __init__(self):
        self.variable='kiwi'
        self.something_really_long_name_for_variables = "something"
    def test(self):
        if self.something_really_long_name_for_variables.startswith("some") or self.variable == "apple":
            print ('test')
        elif self.something_really_long_name_for_variables in ["something", "someone", "anyone", "anything"]:
            print('test')
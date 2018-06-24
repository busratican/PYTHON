# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:00:08 2018

@author: Busra
"""
#REGULAR EXPRESSIONS = regex
#a tool for matching patterns in text. In Python, we have the re module.

#An example regex is r"^(From|To|Cc).*?python-list@python.org" 
#Now for an explanation: the caret ^ matches text at the beginning of a line. 
#The following group, the part with (From|To|Cc) means that the line has to start with one of the words that are separated by the pipe |. 
#That is called the OR operator, and the regex will match if the line starts with any of the words in the group. 
#The .*? means to un-greedily match any number of characters, except the newline \n character. 
#The un-greedy part means to match as few repetitions as possible. 
#The . character means any non-newline character, the * means to repeat 0 or more times, and 
#the ? character makes it un-greedy.

import re
pattern = re.compile(r"\[(on|of)\]") #slight optimization
print(re.search(pattern,"Mono: Playback 65 [%75] [-16.50dB] [on]"))
#returns match object
print(re.search(pattern,"Nada...:-("))
#does not return anything.
#end example

#EXAMPLE:A proper e-mail matching regex.
def test_email(given_pattern):
    pattern=re.compile(given_pattern)
    emails =  ["john@example.com", "python-list@gmail.com", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern,email):
            print("You failed to match {0}".format(email))
        elif not given_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Passed!")
pattern = r"^.*?@(gmail|hotmail|yahoo|outlook).com"
test_email(pattern)

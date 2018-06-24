# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:13:51 2018

@author: Busra
"""

#Exception Handling
#print(a)

#error
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#NameError: name 'a' is not defined
#</module></stdin>

#Handle all exceptins!
#Setup
actor={"name":"John Travolta","rank":"awesome"}
#function to modify,should return the last name of the actor-think back to previous lesson.
def get_last_name():
    return actor["name"].split()[1]
#TestCode
get_last_name()
print("All exceptions caught! Good Job")
lst_name = get_last_name()
print("The actor's last name is {0}".format(lst_name))
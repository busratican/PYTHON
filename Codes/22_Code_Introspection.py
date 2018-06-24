# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:31:19 2018

@author: Busra
"""

#CODE INTROSPECTION
#Code introspection is the ability to examine classes, functions and keywords to know what they are, what they do and what they know.
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__

# Use the help function to see what each function does.
# Delete this when you are done.
help(dir)
help(hasattr)
help(id)

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))
# Your code goes here
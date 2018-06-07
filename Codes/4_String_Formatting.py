# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:43:17 2018

@author: Busra
"""

#String Formatting
name = "John"
print("Hello, {0}!".format(name))
#print("Hello, %s!",% name) #old format,not accepted,invalid syntax error.
age = 23
print("{0} is {1} years old.".format(name,age))
#Any object which is not a string can be formatted using the %s operator as well
mylist = [1,2,3]
print("A list: {0}".format(mylist))

#Here are some basic argument specifiers you should know:
#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise:You will need to write a format string which prints out the data using the following syntax: 
#Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello"

print("{0} {1} {2}.Your current balance is ${3}.".format(format_string,data[0],data[1],data[2]))
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:48:47 2018

@author: Busra
"""

#conditions
x=2
print(x==2) #print out "true"
print(x == 3) #print false
print(x<3) #print true
#and,or operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John,and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick")
#in operator
#The "in" operator could be used to check if a specified object exists within an iterable object container, 
#such as a list:
if name in ["John","Rick"]:
    print("Your name is either John or Rick")
#Python uses indentation to define code blocks, instead of brackets. 
#The standard Python indentation is 4 spaces, 
#although tabs and any other space size will work, as long as it is consistent.
x==2
if x==2:
    print("x equals two!")
else:
    print("x does not equals to two")
#is operator:Unlike the double equals operator "==", 
#the "is" operator does not match the values of the variables, but the instances themselves
x=[1,2,3]
y=[1,2,3]
print(x==y)#prints true
print(x is y) #prints false
#not operator
print(not False) #prints True
print((not False) == (False)) #prints False

#Exercise:Change the variables in the first section, so that each if statement resolves as True.
# change this code
number = 10
second_number=0;
first_array = [1,1]
second_array = [1,2,3]

if number < 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 3:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array[1] and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 19:56:27 2018

@author: Busra
"""
#Multiple Function Arguments
#It is possible to declare functions which receive a variable number of arguments
def foo(first,second,third,*therest):
    print("First:{0}".format(first))
    print("Second:{0}".format(second))
    print("Third:{0}".format(third))
    print("And all the rest... {0}".format(list(therest)))
#call and print.
foo(1,2,3,4,5,6)
#It is also possible to send functions arguments by keyword, so that the order of the argument does not matter
def bar(first,second,third,**options):
    if options.get("action") == "sum":
        print("The sum is: {0}".format((first + second + third)))
    if options.get("number") == "first":
        return first
result = bar(1,2,3,action = "sum",number="first")
print("Result:{0}".format(result))
#EXERCISE:
#Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) 
#The foo function must return the amount of extra arguments received.
#The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.
# edit the functions prototype and implementation
def foo(a, b, c,*others):
    print("First:{0}".format(a))
    print("Second:{0}".format(b))
    print("Third:{0}".format(c))
    print("And all the rest... {0}".format(list(others)))
    return list(others).count
def bar(a, b, c,**others):
    if others.get("magicnumber") == 7:
        return True
    else:
        return False
# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
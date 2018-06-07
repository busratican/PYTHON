# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:47:21 2018

@author: Busra
"""

#print function
print("Hello world!")

#indentation
x=1
if x==1:
    #indented four spaces
    print("x is 1")



#Variables and Types
#defining integer number
myint = 7
print(myint)
#defining floating-point number
myfloat = 7.0
print(myfloat)
myfloat=float(7)
print(myfloat)
#strings
mystring = 'hello'
print(mystring)
mystring="hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

#simple operations
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " "+ world
print(helloworld)
#assignment operation
a,b=3,4
print(a,b)
#mixing operators between numbers and strings is not supported:
one = 1
two = 2
hello = "hello"
print(one+two+hello)
#ERROR:TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Exercise:The target of this exercise is to create a string, an integer, and a floating point number. 
#The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0,
#and the integer should be named myint and should contain the number 20.

mystring = "hello"
myfloat = 10.0
myint = 20
# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)




















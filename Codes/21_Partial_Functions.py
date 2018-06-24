# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:24:35 2018

@author: Busra
"""

#Partial Functions
from functools import partial

def multiply(x,y):
    return x*y
#create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

#EXERCISE
#Edit the function provided by calling partial() and replacing the first three variables in func(). 
#Then print with the new partial function using only one input variable so that the output equals 60

def func(u,v,w,x):
    return u*4+v*3+w*2+x
p = partial(func,5,6,7)
print(p(8))
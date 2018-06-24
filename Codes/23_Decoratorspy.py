# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:51:20 2018

@author: Busra
"""

#DECORATORS
#Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. 
@decorator
def functions(arg):
    return "value"
#function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions
@repeater
def multiply(num1,num2):
    print(num1*num2)
multiply(2,3)
#This would make a function repeat twice.

#You can also make it change the output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function
#Let's say you want to multiply the output by a variable amount. You could define the decorator
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15
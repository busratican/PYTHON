# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 19:25:25 2018

@author: Busra
"""

#GENERATORS
#Generators are used to create iterators, but with a different approach. 
#Generators are simple functions which return an iterable set of items, one at a time, in a special way.
#When an iteration over a set of item starts using the for statement, the generator is run. 
#Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, 
#returning a new value from the set. 
#example of a generator function which returns 7 random integers:
import random
def lottery():
    #returns 6 numbers between 1 and 40.
    for i in range(6):
        yield random.randint(1,40)
    #returns a 7th number between 1 and 15
    yield random.randint(1,15)
for random_number in lottery():
    print("And the next number is.....{}!".format(random_number))

#EXERCISE:Write a generator function which returns the Fibonacci series. 
# fill in this function
def fib():
    pass #this is a null statement which does nothing when executed, useful as a placeholder.
    number1,number2 = 1,1
    
    while 1:
        yield number1
        number1,number2 = number2,number1+number2
   
#TODO: Learn yield exactly what it is.
# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
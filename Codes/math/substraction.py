# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:07:10 2018

@author: Busra
"""
import addition #import module addition

def func_substraction(num1,num2):
    if num1 < num2:
        return (num2-num1)
    else:
        return (num1-num2)
def func_sort():
    numbers = []
    for x in range(1,101):
        numbers.append(x)
    return numbers.sort
def main():
    result = addition.func_add(5,4) #use func_add inside addition.py module
    print(result)
main()

class Initialization():
    print("Initializing....")
    variable = "Hello, you are in Initialization..."

    
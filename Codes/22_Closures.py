# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:35:09 2018

@author: Busra
"""

#CLOSURES
def transmit_to_space(message):
    "This is enclosing function"
    def data_transmission():
        "The nested function"
        print(message)
    data_transmission()
print(transmit_to_space("Test message"))

def print_msg(number):
    def printer():
        "here we are usşng the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)
print_msg(9)

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter
fun2=transmit_to_space("Burn the Sun!")
fun2()
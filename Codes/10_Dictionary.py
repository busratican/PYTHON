# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 20:27:47 2018

@author: Busra
"""

#DICTIONARY
#works with keys and values instead of indexes.
#a database of phone numbers:first way defining dictionary
phonebook = {'jack':4098, 'sape':4139, 'guido':4127, 'jill':23433543}
print(phonebook)
#second way
tel = {}
tel['Leonardo Da Vinci'] = 1
tel['Albert Einstein'] = 2
tel['Picasso'] = 3
print(tel)
#iterating over dictionaries
for name,number in phonebook.items():
    print("Phone number of {0} is {1} ".format(name,number))
#removing a value:first way
del phonebook['jack']
print(phonebook)
#second way
tel.pop('Picasso')
print(tel)

#EXERCISE:Add 'Jake' to the phonebook with the phone number 9876554 and remove Jill from the phonebook.
phonebook['jake'] = 9876554
del phonebook['jill']
print(phonebook)
#test code
if "jake" in phonebook:
    print("jake is listed in phonebook.")
if "jill" not in phonebook:
    print("jill is not kisted in the phonebook.")
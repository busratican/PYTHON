# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:18:38 2018

@author: Busra
"""

#Serialization
import json
#To load JSON back to a data structure, use the "loads" method. This method takes a string and turns it back into the json object datastructure:
#print(json.loads(json_string))
#To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String:
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
#Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
#Exercise:The aim of this exercise is to print out the JSON string with key-value pair "Me" : 800 added to it.
#import json
# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 18:46:57 2018

@author: Busra
"""

#NUMPY ARRAYS:
#they are fast, 
#easy to work with, 
#give users the opportunity to perform calculations across entire arrays
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
#import numpy package as  np
import numpy as np
#create two numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
#print the type pf np_height
print(type(np_height))
#Element-wise calculations.
#calculate bmi
bmi = np_weight / np_height ** 2
print(bmi)
#subsetting
#For a boolean response.
bmi > 3
#print only those observations above 23
bmi[bmi>23]
#EXERCISE:
#First, convert the list of weights from a list to a Numpy array
#Then, convert all of the weights from kilograms to pounds
#Use the scalar conversion of 2.2 lbs per kilogram to make your conversion
#Lastly, print the resulting array of weights in pounds.
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np
np_weight = np.array(weight_kg)

np_weight_pounds = np_weight * 2.22
print(np_weight_pounds)


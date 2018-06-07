# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 19:00:53 2018

@author: Busra
"""

#PANDAS BASIC
#Pandas Data Frames
#high-level data manipulation tool 
#It is built on the Numpy package and its key data structure is called the DataFrame.
#DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
dict = {"country" : ["Brazil","Russia","India","China","South Africa"],
        "capital" : ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area" : [8.516, 17.10, 3.286, 9.597, 1.221],
        "population" : [200.4, 143.5, 1252, 1357, 52.98]        
        }
import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
#with different index values
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
#Second way creating DataFrame
# the csv cars.csv is stored and can be imported using pd.read_csv:
cars = pd.read_csv("documents\cars.csv")
print(cars)
#Indexing DataFrames
#One of the easiest ways to do this is by using square bracket notation.
cars = pd.read_csv("documents\cars.csv",index_col = 0)
#print carb column as Pandas Series.
print(cars['carb'])
#print out carb column as Pandas DataFrame
print(cars[['carb']])
#print DataFrame with disp and hp columns.
print(cars[['disp','hp']])
#Square brackets can also be used to access observations (rows) from a DataFrame
#print first 4 rows.
print(cars[0:4])
# Print out fifth, sixth, and seventh row
print(cars[4:7])
#loc and iloc to perform just about any data selection operation. 
## Print out row for 2
print(cars.iloc[2])
#Print out observations for Australia and Egypt
#print(cars.loc[['AUS','EG']])

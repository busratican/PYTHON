# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:06:31 2018

@author: Busra
"""
#import substraction  #import module addition
#def func_add(num1,num2):
#    return num1+num2
#def main():
#    result = substraction.func_substraction(1,2) #use func_substraction inside substraction.py module
#    print(result)
#main()
#-----------------------------------------------------------------------------------------------------#
#importing module objects to the current namespace
#from substraction import func_substraction
#result = func_substraction(3,4)
#print(result)
#-----------------------------------------------------------------------------------------------------#
#importing all objects from a module
#from substraction import *
#def main():
#    result = func_substraction(6,1)
#    print(result)
#main()
#-----------------------------------------------------------------------------------------------------#
#custom import name
#import substraction as sub
#def main():
#    result = sub.func_substraction(9,0)
#    print(result)
#main()
#-----------------------------------------------------------------------------------------------------#
#module initialization
#initialize substraction function as a singleton
#sub = Initialization()
#sub.variable
#Extending module load path
#tell the Python interpreter where to look for modules.
#Method1:You could use environment varianle PYTHONPATH.
#PYTHONPATH=/math python addition.py
#Method2:sys.path.append
#sys.path.append("/math")
#Exploring built-in modules
#two important func: dir and help
#urllib:create read data from URLs
import urllib
urllib.urlopen("http://ocw.polytechnic.edu.na/courses/electrical-engineering-and-computer-science/6-837-computer-graphics-fall-2003/assignments/")
#look functions implemented in each module use dir.
import urllib
dir(urllib)
#read about more with help.
help(urllib.parse)
#writing packages
#Each package in Python is a directory which MUST contain a special file called '__init__.py'.
#If we create a directory called foo,which marks the package name,we can theb create a module inside that package called bar.
#We also must not forget to add the __init__.py file inside the foo directory.
#import foo.bar
#or
#from foo import bar
#The __init__.py file can also decide which modules the package exports as the API,while keeping other modules internal,
#by overriding the __all__ variable,like so:
#__init__.py
#__all__ = ["bar"]
#-----------------------------------------------------------------------------------------------------#
#Exercise:print an sorted list of numbers 1 to 100.
import substraction as module
my_list = []
my_list=module.func_sort()
























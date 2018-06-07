# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:15:33 2018

@author: Busra
"""

#FUNCTIONS
#function definitions:use de keyword
def my_func():
    print("Hello from my function!")
    
#parameters
def my_func_with_args(username,greeting):
    print("Hello {0}, from my function!, I wish you {1}".format(username,greeting))
#return keyword
def sum_two_numbers(a,b):
    return a + b
#call functions
my_func()
my_func_with_args("John Doe","a great year")
x=sum_two_numbers(1,2)
print(x)

#Exercise
#1--add function list_benefits():returns the following list of strings:"More organized code","More readable code","Easier code"
#"Code reuse","Allowing programmers to share and connect code together"
#2--add function build_sentence(info):recieves a single argument(string) and return sentence "...is a benefit of functions!".
#3--Run and see all the function together!

def list_benefits():
    sentences = ["More organized code","More readable code","Easier code","Code reuse","Allowing programmers to share and connect code together"]
    return sentences;
def build_sentence(info):
    return info + " is a benefit of functions!"

my_list = list_benefits()
for sentence in my_list:
    print(build_sentence(sentence))































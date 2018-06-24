# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:19:35 2018

@author: Busra
"""

#SETS
#Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
print(set("my name is Eric and Eric is my name".split()))

#Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other sets
a=set(["Jake","John","Eric"])
print(a)
b=set(["John","Jill"])
print(b)
#intersection
print(a.intersection(b))
print(b.intersection(a))
#union
print(a.union(b))
#difference
print(a.difference(b))
#symmetric_difference
print(a.symmetric_difference(b))
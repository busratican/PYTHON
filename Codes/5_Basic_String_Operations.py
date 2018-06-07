# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:57:11 2018

@author: Busra
"""

#Basic String Operations
astring = "Hello world!"
astring2 = 'Hello world!'
print("single quotes are ' '") #if you print regex like '',you should use "" for defining string.
print(len(astring))
print(astring2.index("o")) #give the index of character(first).
print(astring.count("l")) #counts num of 'l' in string.
print(astring2[3:7]) #starting from index 3 until index 6.
print(astring2[-6:-3]) #starts printing end.
print(astring[3:7:2])#[start:stop:step].This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax.
print(astring[::-1])#reverse string
print(astring.upper())#upper
print(astring2.lower())#lower
print(astring.startswith("Hello"))
print(astring.endswith("asdfsfsdfs"))#determine whether the string starts with something or ends with something
afewwords = astring.split(" ") #This splits the string into a bunch of strings grouped together in a list.
print(afewwords)

#Exercise:Try to fix the code to print out the correct information by changing the string.
s = "Strings are awesome!"
# Length should be 20
print("Length of s = {0}".format(len(s)))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = {0}".format(s.index("a")))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
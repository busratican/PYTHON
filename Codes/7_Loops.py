# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:50:10 2018

@author: Busra
"""

#LOOPS
#for loops
primes = [2,3,5,7]
for prime in primes:
    print(prime)
#xrange and range operators
    #range:returns new list with numbers of that specified range
    #xrange:returns an iterator(more efficient)
for x in range(5):
    print(x)
#prints (3,4,5)
for x in range(3,6):
    print(x)
#prints (3,5,7)
for x in range(3,8,2):
    print(x)
#while loops
count = 0
while count<5:
    print(count)
    count += 1
#break and continue
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
#else clause:when the code fails,then code part in "else" is executed.
count = 0
while(count<5):
    print(count)
    count+=1
else:
    print("Count value reached {0}".format(count))    
for i in range(1,10):
    if(i%5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition.")
#Exercise:Loop through and print all even numbers from the numbers list in the same order they are recieved.
#Do not print any numbers that come after 237 in the sequence.
numbers = []
for x in range(475,951):
    numbers.append(x) 
for number in numbers:
    if number % 2 == 0:
        print(number)
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
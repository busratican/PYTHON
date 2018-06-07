# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:34:57 2018

@author: Busra
"""

#CLASSES AND OBJECTS
class MyClass:
    variable = "blah"
    def function(self):
        print("This is a message inside the class")
myobjectx = MyClass()#create object of class(myobjectx)
print(myobjectx.variable)#access variable in Class
myobjecty = MyClass()
myobjecty.variable = "yackity" #change the string of variable.
print(myobjectx.variable)
print(myobjecty.variable)
#Accessing Object Functions
myobjectx.function() #access function.

#EXERCISE:We have a class defined for vehicles.Create 2 new vehicles called 'car1' and 'car2'.
#Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

class Vehicle:
    name = " "
    worth = float()
    
    def func_getCar(self,Cname,Cworth): #keyword self is important!
       print("Your car : {0} with cost {1}".format(Cname,Cworth))

car1 = Vehicle()
name_car1=car1.name = "Fer"
worth_car1=car1.worth = 60.000
car1.func_getCar(name_car1,worth_car1)

car2 = Vehicle()
name_car2=car2.name = "Jump"
worth_car2=car2.worth = 10.000
car2.func_getCar(name_car2,worth_car2)































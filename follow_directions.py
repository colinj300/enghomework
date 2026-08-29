# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 1.3 (Follow Directions)
# Date:         8/26/26
#

from math import * # math import

print("This shows the evaluation of (1-cos(x)) / x^2 evaluated cloose to x=0")
print("My guess is 1")

x = 1.0
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.1
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.01
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.001
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.0001
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.00001
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.000001
funct = ((1-cos(x)) / x**2)
print(funct)

x = 0.0000001
funct = ((1-cos(x)) / x**2)
print(funct)

print("")
print("My guess was a little off")





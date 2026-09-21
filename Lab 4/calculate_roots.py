# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 4.3 Individual (Calculate Roots)
# Date:         9/10/26
#

from math import *

aco = float(input("Please enter the coefficient A: "))
bco = float(input("Please enter the coefficient B: "))
cco = float(input("Please enter the coefficient C: "))

if(aco != 0):
    # quadratic equation
    disc = bco**2 - 4*aco*cco
    if(disc < 0):
        imaginary = sqrt(-disc)
        real = -bco / (2*aco)
        imaginary = imaginary / (2*aco)
        print(f"The roots are x = {real} + {imaginary}i and x = {real} - {imaginary}i")
    elif(disc == 0):
        print(f"The root is x = {-bco / (2*aco)}")
    else:
        x1 = (-bco + sqrt(disc)) / (2*aco)
        x2 = (-bco - sqrt(disc)) / (2*aco)
        print(f"The roots are x = {x1} and x = {x2}")
elif(bco != 0):
    print(f"The root is x = {-cco/bco}")
elif(cco != 0):
    print(f"You entered an invalid combination of coefficients!")

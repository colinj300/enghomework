# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 6.1 Individual (Howdy Whoop)
# Date:         9/25/26
#

from math import *

num1 = int(input(f"Enter an integer: "))
num2 = int(input(f"Enter another integer: "))

# checks
for i in range(1, 101, 1): # goes from 1 - 101 inclusive, steps by 1
    if i % num1 == 0 and i % num2 == 0:
        print("Howdy Whoop")
    elif(i % num1 == 0): # checks if evenly divisible by num1
        print("Howdy")
    elif(i % num2 == 0): # checks if evenly divisible by num2
        print("Whoop")
    else:
        print(i)

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 3.3 Individual (Challenge Problem (tau))
# Date:         9/2/26
#

from math import *

digits = int(input(f"Please enter the number of digits of precision for tau: ")) # inputs the user desired digits of precision
print(f"The value of tau to {digits} digits is: {tau:.{digits}f}") # prints out value of tau correctly rounded to user desired digits of presc. by dynamically formatting fstring. 

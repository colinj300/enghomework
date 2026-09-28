# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 6.2 Individual (Computing Sums)
# Date:         9/25/26
#

from math import *

num1 = int(input(f"Enter an integer: "))
num2 = int(input(f"Enter another integer: "))

sum = 0
# checks
for i in range(num1, (num2+1)): # goes from num1 to num2+1 so that the end value is also included in the sum
    sum += i # iterates and adds the current i value to the sum
print(f"The sum of all integers from {num1} to {num2} is {sum}")


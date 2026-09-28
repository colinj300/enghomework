# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 6.4 Individual (Co-balancing numbers)
# Date:         9/25/26
#

from math import *

usernum = int(input("Enter a value for n: "))

sum1 = 0
for i in range(usernum + 1):
    sum1 += i

sum2 = 0
counter = 0
nextnum = usernum + 1 # increments usernum in a seperate variable
while sum2 < sum1:
    sum2 += nextnum
    nextnum += 1
    counter += 1

# checks
if sum2 == sum1: # checks to see if they cobalanced
    print(f"{usernum} is a co-balancing number with r={counter}")
else:
    print(f"{usernum} is not a co-balancing number")


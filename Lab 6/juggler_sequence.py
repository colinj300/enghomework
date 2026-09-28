# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 6.3 Individual (Juggler Sequence)
# Date:         9/25/26
#

from math import *

usernum = int(input(f"Enter a positive integer: "))
usernumstr = str(usernum) # initializes the string for the sequence
counter = 0 # counter for num of iterations
print(f"The Juggler sequence starting at {usernum} is:")
# loop section
while usernum > 1:
    if(usernum % 2 == 0):
        usernum = int(sqrt(usernum))
    else:
        usernum = int(usernum ** (3/2))
    usernumstr += ", " + str(usernum) # concats the current number to the sequence string
    counter += 1 # increases counter (duh)
print(usernumstr)
print(f"It took {counter} iterations to reach 1")

    
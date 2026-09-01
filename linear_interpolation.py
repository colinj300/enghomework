# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 2.3 (Linear Interpolation)
# Date:         9/1/26
#

# x is going to represent t whenever mentioned so makes sense graphically
# y is going to represent the distance past houston in Km  so makes sense graphically

from math import *

x1 = 10 # time when first measurement taken
y1 = 2030 # distance past houston when first measurement was taken
x2 = 55 # time when second measurement was taken
y2 = 23030 # distance past houston when second measurement was taken
x0 = 25 # time we are using for output in part 1
rad = 6745 # radius of orbit circle
circ = 2*(pi)*rad # circumference of the circle that is orbiting, houston is at pos 0

y0 = (((y2-y1)/(x2-x1))*(x0-x1) + y1)
print("Part One")
print(f"For t = {x0} minutes, the position p = {y0} kilometers.")

print("Part Two")
x0 = 300 # reassigns x0 to 300 so the interpolation can be reran
y0 = (((y2-y1)/(x2-x1))*(x0-x1) + y1) # rerunning interpolation with updated x0
y0p2 = (y0 % circ) # assigns y0p2 the modulus of the interpolation divided by the circumference using x=300. 
print(f"For t = {x0} minutes, the position p = {y0p2} kilometers.")


# 300 minutes, just use the slope of the line to calculate the y pos (distance) in a larger number 
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 2.3 Individual (More Linear Interpolation)
# Date:         9/1/26
#

# x is going to represent t whenever mentioned so makes sense graphically
# y is going to represent the distance past houston in Km  so makes sense graphically

from math import *

x0 = 8 # x val for t = 12
y0 = 6 # y val for t = 12
z0 = 7 # z val for t = 12
t0 = 12.0 # t val

t1 = 30.0 # stated

x2 = -5 # x val for t = 85
y2 = 30 # y val for t = 85
z2 = 9 # z val for t = 85
t2 = 85.0 # stated

x1 = (((x2-x0)/(t2-t0))*(t1-t0) + x0)
y1 = (((y2-y0)/(t2-t0))*(t1-t0) + y0)
z1 = (((z2-z0)/(t2-t0))*(t1-t0) + z0)

print(f"At time {t1} seconds:")
print(f"x1 = {x1} m")
print(f"y1 = {y1} m")
print(f"z1 = {z1} m")
print("-----------------------")

t1 = 37.5
x1 = (((x2-x0)/(t2-t0))*(t1-t0) + x0)
y1 = (((y2-y0)/(t2-t0))*(t1-t0) + y0)
z1 = (((z2-z0)/(t2-t0))*(t1-t0) + z0)

print(f"At time {t1} seconds:")
print(f"x2 = {x1} m")
print(f"y2 = {y1} m")
print(f"z2 = {z1} m")
print("-----------------------")

t1 = 45.0
x1 = (((x2-x0)/(t2-t0))*(t1-t0) + x0)
y1 = (((y2-y0)/(t2-t0))*(t1-t0) + y0)
z1 = (((z2-z0)/(t2-t0))*(t1-t0) + z0)

print(f"At time {t1} seconds:")
print(f"x3 = {x1} m")
print(f"y3 = {y1} m")
print(f"z3 = {z1} m")
print("-----------------------")

t1 = 52.5
x1 = (((x2-x0)/(t2-t0))*(t1-t0) + x0)
y1 = (((y2-y0)/(t2-t0))*(t1-t0) + y0)
z1 = (((z2-z0)/(t2-t0))*(t1-t0) + z0)

print(f"At time {t1} seconds:")
print(f"x4 = {x1} m")
print(f"y4 = {y1} m")
print(f"z4 = {z1} m")
print("-----------------------")

t1 = 60.0
x1 = (((x2-x0)/(t2-t0))*(t1-t0) + x0)
y1 = (((y2-y0)/(t2-t0))*(t1-t0) + y0)
z1 = (((z2-z0)/(t2-t0))*(t1-t0) + z0)

print(f"At time {t1} seconds:")
print(f"x5 = {x1} m")
print(f"y5 = {y1} m")
print(f"z5 = {z1} m")
print("-----------------------")





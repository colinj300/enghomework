# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Angie Rodriguez
# Matvii Khoruzhenko
# Tasha Sawatphadungkij
# Section: ENG-102-535
# Assignment: Lab 3.2 Team (Still More Linear Interpolation)
# Date: 9/2/26
#

from math import *

t0 = float(input("Enter time 1: ")) # time 1 value val
x0 = float(input("Enter the x position of the object at time 1: ")) # prompts user for x pos @ t1
y0 = float(input("Enter the y position of the object at time 1: ")) # prompts user for y pos @ t1
z0 = float(input("Enter the z position of the object at time 1: ")) # prompts user for z pos @ t1

t2 = float(input("Enter time 2: ")) # time 2 value
x2 = float(input("Enter the x position of the object at time 2: ")) # prompts user for x pos @ t2
y2 = float(input("Enter the y position of the object at time 2: ")) # prompts user for y pos @ t2
z2 = float(input("Enter the z position of the object at time 2: ")) # prompts user for z pos @ t2

interval = float((t2-t0) / 4) # takes the difference of the final-initial time, divides by 4 so we have an equal interval
print("")

t1 = t0
x1 = float((((x2-x0)/(t2-t0))*(t1-t0) + x0))
y1 = float((((y2-y0)/(t2-t0))*(t1-t0) + y0))
z1 = float((((z2-z0)/(t2-t0))*(t1-t0) + z0))
print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

t1 += interval
x1 = float((((x2-x0)/(t2-t0))*(t1-t0) + x0))
y1 = float((((y2-y0)/(t2-t0))*(t1-t0) + y0))
z1 = float((((z2-z0)/(t2-t0))*(t1-t0) + z0))
print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

t1 += interval
x1 = float((((x2-x0)/(t2-t0))*(t1-t0) + x0))
y1 = float((((y2-y0)/(t2-t0))*(t1-t0) + y0))
z1 = float((((z2-z0)/(t2-t0))*(t1-t0) + z0))
print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

t1 += interval
x1 = float((((x2-x0)/(t2-t0))*(t1-t0) + x0))
y1 = float((((y2-y0)/(t2-t0))*(t1-t0) + y0))
z1 = float((((z2-z0)/(t2-t0))*(t1-t0) + z0))
print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

t1 += interval
x1 = float((((x2-x0)/(t2-t0))*(t1-t0) + x0))
y1 = float((((y2-y0)/(t2-t0))*(t1-t0) + y0))
z1 = float((((z2-z0)/(t2-t0))*(t1-t0) + z0))
print(f"At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")




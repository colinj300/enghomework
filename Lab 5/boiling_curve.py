# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 5 Individual (Boiling Curve)
# Date:         9/20/26
#

from math import *

# variable declarations
xA, yA = 1.3, 1000
xB, yB = 5, 7000
xC, yC = 30, 1.5e6
xD, yD = 120, 2.5e4
xE, yE = 1200, 1.5e6


delta_te = float(input("Enter the excess temperature: ")) # input statement

if delta_te < xA or delta_te > xE:
    print(f"Surface heat flux is not available")
elif delta_te <= xB:
    # segment a to b
    m = log(yB / yA) / log(xB / xA)
    q = yA * (delta_te / xA) ** m
    q_rounded = int(q + 0.5)
    print(f"The surface heat flux is approximately {q_rounded} W/m^2")
elif delta_te <= xC:
    # segment b to c
    m = log(yC / yB) / log(xC / xB)
    q = yB * (delta_te / xB) ** m
    q_rounded = int(q + 0.5)
    print(f"The surface heat flux is approximately {q_rounded} W/m^2")
elif delta_te <= xD:
    # segment c to d
    m = log(yD / yC) / log(xD / xC)
    q = yC * (delta_te / xC) ** m
    q_rounded = int(q + 0.5)
    print(f"The surface heat flux is approximately {q_rounded} W/m^2")
else:
    # segment d to e
    m = log(yE / yD) / log(xE / xD)
    q = yD * (delta_te / xD) ** m
    q_rounded = int(q + 0.5)
    print(f"The surface heat flux is approximately {q_rounded} W/m^2")




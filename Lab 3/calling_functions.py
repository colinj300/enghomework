# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 3.2 Individual (Calling Functions)
# Date:         9/2/26
#


from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

sidelen = float(input(f"Please enter the side length: ")) # takes user input for side length, floats and stores it

printresult("triangle", sidelen, float(((sqrt(3) / 4)*(sidelen**2)))) # calls printresult with triangle, sidelen, and area of equilateral triangle calculation 
printresult("square", sidelen, float(sidelen**2)) # calls printresult with square, sidelen, and area of square calculation 
printresult("pentagon", sidelen, float(0.25 * sqrt(5*(5+(2*sqrt(5))))*(sidelen**2))) # calls printresult with pentagon, sidelen, and area of regular pentagon calculation 
printresult("hexagon", sidelen, float(((3*sqrt(3))/2)*(sidelen**2))) # calls printresult with hexagon, sidelen, and area of regular hexagon calculation 
printresult("dodecagon", sidelen, float(3*(2 + sqrt(3))*(sidelen**2))) # calls printresult with dodecagon, sidelen, and area of regular dodecagon calculation 

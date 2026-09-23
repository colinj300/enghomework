# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Angie Rodriguez
# Matvii Khoruzhenko
# Tasha Sawatphadungkij
# Section: ENG-102-535
# Assignment: Lab 6.1 Team (Pyramid Area)
# Date: 9/21/26

from math import *

s_length = float(input(f"Enter the side length in meters: ")) # takes side length as float
layers = int(input(f"Enter the number of layers: ")) # takes layers as int

top_layer = (s_length * layers)**2 # gets the surface area of the bottom layer from top-down

side_area = 0 # declares the varaible

for i in range(layers, 0, -1):
    side_area += (s_length * s_length) * i

total = float(top_layer + (4*side_area)) 

print(f"You need {total:.2f} m^2 of gold foil to cover the pyramid")
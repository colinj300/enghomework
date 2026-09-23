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

s_length = float(input(f"Enter the side length in meters: ")) # side length input
layers = float(input(f"Enter the number of layers: ")) # layers input
top_layer = (s_length * layers)**2 # area of the bottom-most layer from top-down
onearea = s_length**2 # area of one square

squaresperface = (layers*(layers + 1))/2 # number of squares per side face
area_tot = float((squaresperface*onearea)*4 + top_layer) # number of squares per side face * area of one square * 4 * area of top-down
print(f"You need {area_tot:.2f} m^2 of gold foil to cover the pyramid")

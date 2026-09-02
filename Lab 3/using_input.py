# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 3.1 Individual (Using Input)
# Date:         9/2/26
#

from math import * # stated

print(f"This program calculates the Reynolds number given velocity, length, and viscosity")
reynolds_velo = float(input(f"Please enter the velocity (m/s): ")) # takes user input for velocity, floats and stores it
reynolds_len = float(input(f"Please enter the length (m): ")) # takes user input for length, floats and stores it
reynolds_visc = float(input(f"Please enter the viscosity (m^2/s): ")) # takes user input for viscosity, floats and stores it
print(f"Reynolds number is {((reynolds_velo * reynolds_len) / reynolds_visc):.0f}")
print("")

print(f"This program calculates the wavelength given distance and angle")
wavelength_dist = float(input(f"Please enter the distance (nm): ")) # takes user input for distance, floats and stores it
wavelength_angle = float(input(f"Please enter the angle (degrees): ")) # takes user input for angle in degrees, floats and stores it
print(f"Wavelength is {(2 * wavelength_dist * sin(((pi/180) * wavelength_angle))):.4f} nm")
print("")

print(f"This program calculates the production rate given time, initial rate, and decline rate")
arps_days = float(input(f"Please enter the time (days): ")) # takes user input for num of days, floats and stores it
arps_qi = float(input(f"Please enter the initial rate (barrels/day): ")) # takes user input for initial rate, floats and stores it
arps_di = float(input(f"Please enter the decline rate (1/day): ")) # takes user input for decline rate, floats and stores it
arps_hypconst = 0.8
print(f"Production rate is {(arps_qi / (1 + (arps_hypconst * arps_di * arps_days))**(1/arps_hypconst)):.2f} barrels/day")
print("")

print(f"This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
rocket_m0 = float(input(f"Please enter the initial mass (kg): ")) # takes user input for initial mass, floats and stores it
rocket_mf = float(input(f"Please enter the final mass (kg): ")) # takes user input for final mass, floats and stores it
rocket_ve = float(input(f"Please enter the exhaust velocity (m/s): ")) # takes user input for exhaust velocity, floats and stores it
print(f"Change of velocity is {(rocket_ve * log(rocket_m0 / rocket_mf)):.1f} m/s")









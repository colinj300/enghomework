# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 2.1 (Using Variables)
# Date:         9/1/26
#

from math import *

# Reynolds Number Vars
reynolds_mu = 9 # m/s
reynolds_visc = .0015 # m^2/s
reynolds_L = .875 # meters

# Wavelength Vars
wavelength_dist = .030 # nm
wavelength_angle = 35 # degrees

# Arps equation vars
arps_days = 10
arps_qi = 100 # barrels/day
arps_di = 2 # decline rate (2 barrels/day)
arps_hypconst = .8

#Tsiolkovsky rocket equation vars
rocket_m0 = 11000 # kg
rocket_mf = 8300 # kg
rocket_ve = 2030 # m/s

print("Reynolds number is", (reynolds_mu * reynolds_L) / reynolds_visc) # Reynolds number print statement
print("Wavelength is", 2 * wavelength_dist * sin(((pi/180) * wavelength_angle)), "nm") # Wavelength print statement
print("Production rate is", arps_qi / (1 + (arps_hypconst * arps_di * arps_days))**(1/arps_hypconst), "barrels/day") 
print("Change of velocity is", rocket_ve * log(rocket_m0 / rocket_mf), "m/s")

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Angie Rodriguez
# Matvii Khoruzhenko
# Tasha Sawatphadungkij
# Section: ENG-102-535
# Assignment: Lab 3.1 Team (Unit Conversions)
# Date: 9/2/26
#

from math import *

# unit conversion vars
lbtof = 4.44822 # pounds to feet conversion
meterstoft = 3.28084 # meters to feet conversion
atmtokpa = 101.325 # atmospheres to kilopascals conversion
wattstobtu = 3.41214163 # watts to BTU conversion
lpstogpm = 0.264172052 # lps to gpm conversions
ctof = 33.80 # celcius to farenheit conversion

usernum = float(input("Please enter the quantity to be converted: ")) # user input prompt, stores as float

## conversion print statements
print(f"{usernum:.2f} pounds force is equivalent to {(lbtof*usernum):.2f} newtons") # prints the conversion between lbs force and newtons
print(f"{usernum:.2f} meters is equivalent to {(meterstoft*usernum):.2f} feet") # prints the conversion between meters and feet
print(f"{usernum:.2f} atmospheres is equivalent to {(atmtokpa*usernum):.2f} kilopascals") # prints the conversions between atmospheres and kpa
print(f"{usernum:.2f} watts is equivalent to {(wattstobtu*usernum):.2f} BTU per hour") # prints the conversion between watts and BTU/h
print(f"{usernum:.2f} liters per second is equivalent to {(lpstogpm*60*usernum):.2f} US gallons per minute") # prints conversion between L/s and gpm
print(f"{usernum:.2f} degrees Celsius is equivalent to {((usernum*1.8)+32):.2f} degrees Fahrenheit")  # prints conversion between celcius and farenheit.


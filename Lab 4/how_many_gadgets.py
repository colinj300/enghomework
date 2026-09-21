# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 4.2 Individual (How Many Gadgets)
# Date:         9/10/26
#

dayval = int(input(f"Please enter a positive value for day: ")) # gets user input for day value

if dayval <= 0: # checks if dayval is positive
    print("You entered an invalid number!") #prints such
elif 0 < dayval <= 10: # checks if dayval is between 0 & 10 inclusive
    print(f"The sum total number of gadgets produced on day {dayval} is {dayval*10}") # prints
elif 11 <= dayval <= 50: # if not between 0 & 10 inclusive, check if dayval is between 11 & 50 inclusive
    print(f"The sum total number of gadgets produced on day {dayval} is {((((dayval-10)*(11+dayval)/2))+100):.0f}") # prints
elif 51 <= dayval <= 100: # if not between 11 & 50 inclusive, checks if between 51 and 100 inclusive
    print(f"The sum total number of gadgets produced on day {dayval} is {(1320 + 50*(dayval-50))}") # prints
elif dayval >= 101: # if not between 51 & 100 inclusive, checks if greater or = to 101
    print(f"The sum total number of gadgets produced on day {dayval} is 3820") # prints





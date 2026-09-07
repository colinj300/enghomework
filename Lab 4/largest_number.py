# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 4.1 Individual (Largest Number)
# Date:         9/10/26
#

num1 = float(input(f"Enter number 1: "))
num2 = float(input(f"Enter number 2: "))
num3 = float(input(f"Enter number 3: "))

if num1 >= num2 and num1 >= num3: # compares num1 to num2 and num3
    print(f"The largest number is {num1}") # prints num1 as largest
elif num2 >= num1 and num2 >= num3: # else-if num2 > num1 & num3
    print(f"The largest number is {num2}") # prints num2 as largest
else: # stated
    print(f"The largest number is {num3}") # prints num3 as largest


    

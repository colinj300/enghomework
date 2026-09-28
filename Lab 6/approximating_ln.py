# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Angie Rodriguez
# Colin Johns
# Tasha Sawatphadungkij
# Matvii Khoruzhenko
# Section: 535
# Assignment: Lab Topic 6 (Approximating ln)
# Date: 23 September 2026

from math import*
# Ask user to input a for value of x
x = float (input("Enter a value for x: "))
# Making sure x is between 0 and 2 if its not it is out of range, the user has to keep inputing until it is in range
while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))
# Ask user to input a value for tolerance
tol = float(input("Enter the tolerance: "))
# The values we are starting with:
n = 1
approx_ln = 0.0
approx = ((x-1)**n)/n
# Loop intil the value is getting larger than tolerance or smaller than - tolerance
while approx >= tol or approx <= -tol:
    # Add if n is odd and subtract if n is even
    if n % 2 != 0:
        approx_ln += approx
    else:
        approx_ln -= approx
    # Keep moving to the next number
    n+=1
    approx = ((x-1)**n)/n
# Find the exact value
exact = log(x)
# Subtract to find difference
# If the exact number is bigger, subtract the approximation and if the approximation is bigger subtract the exact number to give positive value.
if exact > approx_ln:
    difference = exact - approx_ln
else: 
    difference = approx_ln - exact

# Output the answers
print(f"ln({x}) is approximately {approx_ln}")
print(f"ln({x}) is exactly {exact}")
print(f"The difference is {difference}")
    

    
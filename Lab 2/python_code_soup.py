# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 2.2 Individual (Python Code Soup)
# Date:         9/1/26
#

x = 1
y = 10
z = 0

z += x # z now equals 1
print(z) # prints 1

x += 1 # x now equals 2
x += 1 # x now equals 3
z = 0 # z now equals 0
y *= x # y now equals 30
z += y # z now equals 30
print(z) # prints 30

y += x # y = 33
y += x # y = 36
z += y # z = 66
z += y # z = 102
print(z) # prints 102

z = 0
y = 10
x = y # x now equals 100
y *= x # y now equals 10000
x = y # x now equals 10000
y *= x # y now equals 1e8
x = y # x now equals 1e8
y *= x
x = y # y now equals 1e16
y *= x
z += y # z now equals 1e16
print(z) # prints 1e16

y = 10 # stated
z = 0 # stated
x = y # x now equals 10
y += x # y now equals 20
x += 1 # x now equals 11
z += x # z now equals 11
x += 1 # x now equals 12
y *= x # y now equals 240
y *= x # y now equals 2880
z += y # z now equals 2891 
y += x # y now equals 2892
z += y # z now equals 5783
z += y # z now equals 8675
print(z)


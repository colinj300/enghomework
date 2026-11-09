# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 9 Individual (Small Functions)
# Date:         10/20/26
#

from math import *

def parta(listA):
    s = sorted(listA)
    n = len(s)
    mid = n // 2

    if n % 2 == 1:
        median = s[mid]
    else:
        median = (s[mid - 1] + s[mid]) / 2

    return s[0], median, s[-1]

def partb(times, distances):
    velos = []
    for i in range(1, len(times)):
        velos.append((distances[i]-distances[i-1])/(times[i]-times[i-1]))
    return velos

def partc(nums):
    for i in range(len(nums)):
        if (2030-nums[i]) in nums and nums.index(2030-nums[i]) != i:
            return nums[i] * (2030 - nums[i])
    return False

def partd(n):
    for start in range(2, n, 2):
        total = 0
        nums = []
        current = start
        while total < n:
            total += current
            nums.append(current)
            current += 2
        if total == n:
            return nums
    return False

def parte(r, a):
    cheight = r - sqrt((r**2 - a**2))
    asphere = (4/3) * pi * (r**3)
    acap = ((pi * (cheight**2))/3)*((3*r)-cheight)
    acyl = ((pi * (a**2)) * 2 * (r-cheight))
    return asphere - 2*acap - acyl

def partf(border, name, comp, email):
    width = max(len(name), len(comp), len(email)) + 4
    top = border * (width + 2)
    bottom = top
    l1 = border + name.center(width) + border
    l2 = border + comp.center(width) + border
    l3 = border + email.center(width) + border
    card = "\n".join([top, l1, l2, l3, bottom])
    return card

def partg(xval, tolerance):
    total = 0
    n = 1
    term = (2/(2*n - 1)) * (xval**(2*n - 1))
    while abs(term) >= tolerance:
        total += term
        n += 1
        term = (2/(2*n - 1)) * (xval**(2*n - 1))
    return total
        

        






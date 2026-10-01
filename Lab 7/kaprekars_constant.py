# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 7.3 (Kaprekars Constant)
# Date:         10/1/26
#

usernum = input("Enter a four-digit integer: ")
current = int(usernum)
count = 0
goal = 6174

print(usernum, end="")

while current != goal and current != 0:
    s = str(current) 
    while len(s) < 4: # pads to 4 digits w lead 0
        s = "0" + s

    digits = list(s)
    digits.sort()

    usernumdesc = []
    for i in range(len(digits)-1, -1, -1):
        usernumdesc.append(digits[i])

    ascnum = int("".join(digits))
    descnum = int("".join(usernumdesc))
    current = descnum - ascnum
    count += 1
    print(f" > {current}", end="")
print()
if current == goal:
    print(f"{usernum} reaches 6174 via Kaprekar's routine in {count} iterations")
else:
    print(f"{usernum} reaches 0 via Kaprekar's routine in {count} iterations")

    





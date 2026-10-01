# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 7.3 Bonus (Kaprekars Challenge)
# Date:         10/1/26
#
counter = 0
for j in range(0, 10000):
    current = j
    count = 0
    goal = 6174
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
    counter += count
print(f"Kaprekar's routine takes {counter} total iterations for all four-digit numbers")
    





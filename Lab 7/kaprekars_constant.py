# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 7.3 (Kaprekars Constant)
# Date:         8/26/26
#

numbersstr = input("Enter numbers: ")
list(numbersstr)
print(numbersstr)

numbers = [int(x) for x in numbersstr] # converts all chars to ints
 # converts current index to integer

# check the sum of numbers from index 0-i, i+1 to end and compare the two
# nested loops is the only thing i could think of

for i in range(len(numbers)):
    leftsum = 0
    rightsum = 0
    leftlist = []
    rightlist = []
    for j in range(numbers[:i+1]): # get left sum
        leftsum += numbers[j]
        leftlist.append(numbers[j])
    for j in range(numbers[i+1:]):
        rightsum += numbers[j]
        rightlist.append(numbers[j])
    if leftsum == rightsum:
        print(f'Left: {leftlist}')
        print(f'Right: {rightlist}')
        print(f'Both sum to {leftsum}')
        break
    

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 7.1 (Name Game)
# Date:         8/26/26
#

name = input("What is your name? ")
storedname = name
list(name)
vowellist = ['a', 'e', 'i', 'o', 'u']
vowindex = 0 
for i in range(len(name)):
    if name[i] in vowellist: # finds and stores the index val of the first vowel
        vowindex = i 
        break
novowel = name[vowindex:] # slices the name at the first vowel to the end, stores in novowel string
if vowindex == 0: # if the first letter is a vowel
    print(f'{storedname}, {storedname}, Bo-B{storedname.lower()}')
    print(f'Banana-Fana Fo-F{storedname.lower()}')
    print(f'Me Mi Mo-M{storedname.lower()}')
    print(f'{storedname}!')
else: # if the first letter lays somewhere other than the first letter
    print(f'{storedname}, {storedname}, Bo-B{novowel}')
    print(f'Banana-Fana Fo-F{novowel}')
    print(f'Me Mi Mo-M{novowel}')
    print(f'{storedname}!')

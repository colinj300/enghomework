# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Arsenii Markov
# Matvii Khoruzhenko
# Adan Parra
# Section: ENG-102-535
# Assignment: Lab 11 Team (Passport Checker)
# Date: 11/4/26

individuals = []
current = []
raw = []

scanpp = input(f'Enter the name of the file: ')

with open(scanpp) as f:
    for line in f:
        if line.strip() == "": # if current line is empty
            if current: # if current has stuff in it 
                individuals.append(" ".join(current)) # joins each line in between the break lines with a space to put in one whole string
                raw.append("\n".join(current))
                current = []
        else:
            current.append(line.strip())

if current:
    individuals.append(" ".join(current))
    raw.append("\n".join(current))

people = []
for i in range(len(individuals)):
    person = {}
    fields = individuals[i].split(' ')
    for j in range(len(fields)):
        key, value = fields[j].split(":")
        person[key] = value
    people.append(person)

invalid = []
valid = []
counter = 0

for i in range(len(people)):
    # valid if all 8 fields are there, or 7 fields with pid being the only one missing
    if len(people[i]) == 8 or (len(people[i]) == 7 and "pid" not in people[i]):
        counter += 1
        valid.append(raw[i])
    else:
        invalid.append(people[i])

with open("valid_passports.txt", "w") as out:
    out.write("\n\n".join(valid)) # blank line only between passports, none at the end

print(f"There are {counter} valid passports")
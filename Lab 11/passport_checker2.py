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

valid = []
counter = 0
hex_chars = "0123456789abcdef"
eyeclg = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for i in range(len(people)):
    p = people[i]
    is_valid = True

    # first check: all 8 fields, or 7 with pid being the only one missing
    if not (len(p) == 8 or (len(p) == 7 and "pid" not in p)):
        is_valid = False
    else:
        # second check: every value follows the rules
        birth = p.get("byr")
        issue = p.get("iyr")
        exp = p.get("eyr")
        height1 = p.get("hgt")
        htype = height1[-2:]
        hnum = height1[:-2]
        haircl = p.get("hcl")
        eyecl = p.get('ecl')
        cntid = p.get('cid')

        if len(birth) != 4 or not birth.isdigit() or int(birth) < 1922 or int(birth) > 2010:
            is_valid = False
        if len(issue) != 4 or not issue.isdigit() or int(issue) < 2016 or int(issue) > 2026:
            is_valid = False
        if len(exp) != 4 or not exp.isdigit() or int(exp) < 2026 or int(exp) > 2036:
            is_valid = False
        if not hnum.isdigit():
            is_valid = False
        elif htype == "cm":
            if int(hnum) < 150 or int(hnum) > 193:
                is_valid = False
        elif htype == "in":
            if int(hnum) < 59 or int(hnum) > 76:
                is_valid = False
        else:
            is_valid = False
        if len(haircl) != 7 or haircl[0] != "#":
            is_valid = False
        else:
            for c in haircl[1:]:
                if c not in hex_chars:
                    is_valid = False
        if eyecl not in eyeclg:
            is_valid = False
        if len(cntid) != 3 or not cntid.isdigit() or cntid[0] == "0":
            is_valid = False

    if is_valid:
        counter += 1
        valid.append(raw[i])

with open("valid_passports2.txt", "w") as out:
    out.write("\n\n".join(valid)) # blank line only between passports, none at the end

print(f"There are {counter} valid passports")
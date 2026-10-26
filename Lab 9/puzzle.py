# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzstring):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newlist = []
    for char in puzstring:
        if char in alpha and char not in newlist:
            newlist.append(char)
    return "".join(newlist)

def is_valid_guess(validletters, userguess):
    if len(userguess) < 10:
        return False
    newlist = []
    for char in userguess:
        if char in validletters and char not in newlist:
            newlist.append(char)
    return "".join(newlist) == userguess

def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == (quotient * divisor) + remainder:
        return True
    return False

def make_number(word, userguess):
    userguesslist = []
    codestring = ""
    for char in userguess:
        userguesslist.append(char)
    for char in word:
        codestring += str(userguesslist.index(char))
    return int(codestring)

def make_numbers(puzstring, userguess):
    words = [w.strip() for w in puzstring.replace("|", ",").split(",")]
    words = [w for w in words if w]

    quotient = words[0]
    divisor = words[1]
    dividend = words[2]
    remainder = words[-1]

    return (make_number(dividend, userguess), make_number(quotient, userguess),
            make_number(divisor, userguess), make_number(remainder, userguess))


def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    print()
    print_puzzle(puzzle)
    get_valid_letters(puzzle)
    is_valid_guess(get_valid_letters(puzzle), "TAKEOURSIM")
    make_number("RUE", "TAKEOURSIM")
    make_numbers(puzzle, "TAKEOURSIM")
    print(make_numbers(puzzle, "TAKEOURSIM"))

    
    

if __name__ == "__main__":
    main()

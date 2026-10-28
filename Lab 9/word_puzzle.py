# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Arsenii Markov
# Matvii Khoruzhenko
# Adan Parra
# Section: ENG-102-535
# Assignment: Lab 9 Team (Word Puzzle)
# Date: 10/27/26

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
    """ Return a string of the unique letters in the puzzle, in order of first appearance. """
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newlist = []
    # Keep each letter the first time it shows up; skip spaces, commas, and '|'
    for char in puzstring:
        if char in alpha and char not in newlist:
            newlist.append(char)
    return "".join(newlist)

def is_valid_guess(validletters, userguess):
    """ Return True if the guess is exactly 10 unique letters from the valid letters. """
    # Too short can never be valid
    if len(userguess) < 10:
        return False
    newlist = []
    # Collect each valid letter once; repeats or invalid letters get dropped
    for char in userguess:
        if char in validletters and char not in newlist:
            newlist.append(char)
    # If nothing was dropped, the guess was all unique, valid letters
    return "".join(newlist) == userguess

def check_user_guess(dividend, quotient, divisor, remainder):
    """ Return True if dividend == quotient * divisor + remainder. """
    if dividend == (quotient * divisor) + remainder:
        return True
    return False

def make_number(word, userguess):
    """ Convert a word to an integer using each letter's position in the guess as its digit. """
    userguesslist = []
    codestring = ""
    # Turn the guess into a list so we can look up each letter's index
    for char in userguess:
        userguesslist.append(char)
    # Each letter's index in the guess is its digit
    for char in word:
        codestring += str(userguesslist.index(char))
    return int(codestring)

def make_numbers(puzstring, userguess):
    """ Return (dividend, quotient, divisor, remainder) as integers based on the guess. """
    # Split the puzzle on commas and '|', strip spaces, and drop empty pieces
    words = [w.strip() for w in puzstring.replace("|", ",").split(",")]
    words = [w for w in words if w]

    # Puzzle order is: quotient, divisor, dividend, ..., remainder (last)
    quotient = words[0]
    divisor = words[1]
    dividend = words[2]
    remainder = words[-1]

    return (make_number(dividend, userguess), make_number(quotient, userguess),
            make_number(divisor, userguess), make_number(remainder, userguess))
    

def main():
    """ Get a puzzle and a guess from the user, then report whether the guess is valid and correct. """
    # puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"

    # 1. Take the puzzle string input from the user
    print("Enter a word arithmetic puzzle: ")
    puzzle_str = input()
    
    # 2. Print the puzzle configuration 
    print_puzzle(puzzle_str)
    
    # 3. Get valid unique letters from the puzzle string
    valid_letters = get_valid_letters(puzzle_str)
    
    # 4. Prompt the user for their guess
    print()
    user_guess = input("Enter your guess, for example ABCDEFGHIJ: ").strip()
    
    # 5. Route the guess to the appropriate validation logic
    if not is_valid_guess(valid_letters, user_guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        # Case: Guess is valid; compute numbers and check the division math
        # make_numbers returns a tuple of (dividend, quotient, divisor, remainder)
        dividend, quotient, divisor, remainder = make_numbers(puzzle_str, user_guess)
        
        # check_user_guess checks if dividend == quotient * divisor + remainder
        is_correct = check_user_guess(dividend, quotient, divisor, remainder)
        
        if is_correct:
            print("Good job!")
        else:
            print("Try again!")


    
    

if __name__ == "__main__":
    main()

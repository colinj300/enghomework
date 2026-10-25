# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Arsenii Markov
# Matvii Khoruzhenko
# Adan Parra
# Section: ENG-102-535
# Assignment: Lab 8 Team (Ascii Clock)
# Date: 10/13/26

ascii_dict = {
    "0": [
        "000",
        "0 0",
        "0 0",
        "0 0",
        "000"
    ],
    "1": [
        " 1 ",
        "11 ",
        " 1 ",
        " 1 ",
        "111"
    ],
    "2": [
        "222",
        "  2",
        "222",
        "2  ",
        "222"
    ],
    "3": [
        "333",
        "  3",
        "333",
        "  3",
        "333"
    ],
    "4": [
        "4 4",
        "4 4",
        "444",
        "  4",
        "  4"
    ],
    "5": [
        "555",
        "5  ",
        "555",
        "  5",
        "555"
    ],
    "6": [
        "666",
        "6  ",
        "666",
        "6 6",
        "666"
    ],
    "7": [
        "777",
        "  7",
        "  7",
        "  7",
        "  7"
    ],
    "8": [
        "888",
        "8 8",
        "888",
        "8 8",
        "888"
    ],
    "9": [
        "999",
        "9 9",
        "999",
        "  9",
        "999"
    ],
    ":": [
        " ",
        ":",
        " ",
        ":",
        " "
    ],
    "A": [
        " A ",
        "A A",
        "AAA",
        "A A",
        "A A"
    ],
    "P": [
        "PPP",
        "P P",
        "PPP",
        "P  ",
        "P  "
    ],
    "M": [
        "M   M",
        "MM MM",
        "M M M",
        "M   M",
        "M   M"
    ],
    " ": [
        " ",
        " ",
        " ",
        " ",
        " "
    ]
}

# user input for time
user_input=input(f"Enter the time: ")
#user input for  clock type
clock_type=int(input(f"Choose your clock type (12 or 24): "))
# user input for what characters they would like in their digtial clock 
user_char=input(f"Enter your preferred character: ")
valid_chars = "abcdeghkmnopqrsuvwxyz@$&*="
while user_char not in valid_chars:
    user_char=input(f"Character not permitted! Try again: ")

##############################################################################

# Define the hour, split it away from the entire time
if user_input[1] == ":":
    user_hour = int(user_input[0])
    time_continued = user_input[1:]
else:
    user_hour = user_input[0] + user_input[1] # Concatenate the strings
    user_hour = int(user_hour)
    time_continued = user_input[2:]

##############################################################################

# Convert hour to 12 hour format
if clock_type == 12: 
    if user_hour <= 12:
        converted_time = (str(user_hour) + time_continued)
        print(f'{converted_time} am')
# If given hour is greather than 12 then subtract 12 from it
    else:
        user_hour -= 12
        converted_time = (str(user_hour) + time_continued)
        print(f'{converted_time} pm')
    
##############################################################################

# Convert to 24 hour fomat
else: 
    # Account for the hour with only one number (ex: 8:56)
    user_hour = str(user_hour)
    if len(user_hour) == 1:
        user_input = list(user_input)
        user_input.insert(0,'0')
        converted_time = ''.join(user_input)
        print(converted_time)
    # Account for the hour with two number (ex: 08:56)
    else:
        converted_time = user_input
        print(converted_time)

# Build the big digital clock one row at a time
printstr = ""
for row in range(5):
    for char in converted_time:
        glyph_row = ascii_dict[char][row]   
        # Swap the drawing character for the user's character
        # (spaces and colons stay the same)
        for c in glyph_row:
            if c == " " or c == ":":
                printstr += c
            else:
                printstr += user_char
        printstr += " "
    printstr += "\n"

print(printstr)
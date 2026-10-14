# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         COLIN JOHNS
# Section:      ENG-102-535
# Assignment:   LAB 8 Team (Ascii Clock)
# Date:         10/13/26
#


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
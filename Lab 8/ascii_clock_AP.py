# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Colin Johns
# Arsenii Markov
# Matvii Khoruzhenko
# Adan Parra
# Section: ENG-102-535
# Assignment: Lab 8 Team (Ascii Clock)
# Date: 10/7/26


# user input for time
user_input=input(f"Enter the time: ")
#user input for  clock type
clock_type=int(input(f"Choose your clock type (12 or 24): "))
# user input for what characters they would like in their digtial clock 
user_char=input(f"Enter your preferred character: ")
valid_chars = "abcdeghkmnopqrsuvwxyz@$&*="
while user_char not in valid_chars:
    user_char=input(f"Character not permitted! Try again: ")
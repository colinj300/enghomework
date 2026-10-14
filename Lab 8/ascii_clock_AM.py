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
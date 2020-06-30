# US Elevator floor converter
# ---
# This program convert a Europe elevator floor number to it respective
# number in US elevator floor system.


# Read user input
user_input = input('What is the Europe floor? ')

# Process 
us_floor = int(user_input) + 1

# Output the result
print('The respective US floor is:', us_floor)
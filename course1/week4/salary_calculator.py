# Salary Calculator
# ---
# This program calculates the salary based on a given worked hour
# and a dolar per hour rate

# Read user input
hour = input('How many hours did you work? ')
rate = input('What is the value of your hour? ')

# Process
salary = float(hour) * float(rate)
salary = '$' + str(salary)

# Output the result
print('Your salary is:', salary)
# Salary Calculator
# ---
# This program calculates the salary based on a given worked hour
# and a dolar per hour rate

# Read user input
try :
    hour = float(input('How many hours did you work? '))
    rate = float(input('What is the value of your hour? '))
except :
    print('Error, please enter numeric input')
    quit()

# Process
salary = hour * rate
salary = '$' + str(salary)

# Output the result
print('Your salary is:', salary)
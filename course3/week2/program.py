import re

file_handler = open('regex_sum_627074.txt')
numbers = list()

for line in file_handler:
    numbers_in_line = re.findall('[0-9]+', line)
    
    if len(numbers_in_line) < 1:
        continue

    for number in numbers_in_line:
        numbers.append(int(number))

print(sum(numbers))
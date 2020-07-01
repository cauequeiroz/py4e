file_name = input('Enter a file name: ')
file_handler = open(file_name)

for line in file_handler:
    line = line.rstrip()
    print(line)
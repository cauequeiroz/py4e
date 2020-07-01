# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line
# that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the
# line (i.e. the entire address of the person who sent the message). Then print out
# a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

def init():
    file_handler = open('mbox-short.txt')
    email_list = list()

    for line in file_handler:
        if not line.startswith('From '): continue
        
        line = line.rstrip()
        email = line.split()[1]
        
        print(email)
        email_list.append(email)
    
    count = len(email_list)
    print("There were", count, "lines in the file with From as the first word")

init()
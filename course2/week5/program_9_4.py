# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent the mail. The program creates
# a Python dictionary that maps the sender's mail address to a count of the number of
# times they appear in the file. After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.

def init():
    file_name = input('Enter file: ')
    file_handler = open(file_name)
    
    email_histogram = dict()
    for line in file_handler:
        if not line.startswith('From '): continue

        email = line.split()[1]
        email_histogram[email] = email_histogram.get(email, 0) + 1

    biggest_email = None
    biggest_count = None
    for key, value in email_histogram.items():
        if biggest_count is None or value > biggest_count:
            biggest_email = key
            biggest_count = value
    
    print(biggest_email, biggest_count)    

init()

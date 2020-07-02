# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

def init():
    file_handler = open('mbox-short.txt')
    hours = dict()

    for line in file_handler:
        if not line.startswith('From '): continue

        time = line.split()[5]
        hour = time.split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

    # craziest way, just for fun :p
    for (k, v) in sorted([(k, v) for (k, v) in hours.items()]):
        print(k, v)

init()
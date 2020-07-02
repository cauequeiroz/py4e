# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line
# into a list of words using the split() method. The program should build a list of
# words. For each word on each line check to see if the word is already in the list
# and if not append it to the list. When the program completes, sort and print the
# resulting words in alphabetical order.

def add_once(list, elements):
    for element in elements:
        if element in list: continue
        list.append(element)


def init():
    file_handler = open('romeo.txt')
    words = list()

    for line in file_handler:
        line = line.rstrip()
        add_once(words, line.split())

    words.sort()
    print(words)

init()
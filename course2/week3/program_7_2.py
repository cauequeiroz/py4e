def safe_open(file):
    try:
        return open(file)
    except:
        print('File not exists.')
        quit()

def init():
    file_name = input('Enter a file name: ')
    file_handler = safe_open(file_name)

    counter = 0
    total = 0

    for line in file_handler:
        if not line.startswith('X-DSPAM-Confidence:'): continue

        start_position = line.find(':') + 1
        number = float(line[start_position:].strip())

        counter = counter + 1
        total = total + number

    average = total / counter
    print('Average spam confidence:', average)

init()
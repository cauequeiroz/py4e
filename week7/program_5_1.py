def readInput():
    sum = 0
    counter = 0

    while True:
        command = input('Type a number: ')
        if command == 'done':
            print(sum, counter, sum/counter)
            break
        else:
            try:
                number = int(command)
                sum = sum + number
                counter = counter + 1
            except:
                print('Invalid input')

readInput()


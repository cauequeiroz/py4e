class Floor(object):
    def __init__(self, number):
        self.floor = int(number)
    
    def getFloor(self):
        return self.floor

class EuropeFloor(Floor):
    def __init__(self, number):
        Floor.__init__(self, number)

    def toUSFloor(self):
        return self.floor + 1

class USFloor(Floor):
    def __init__(self, number):
        Floor.__init__(self, number)
    
    def toEuropeFloor(self):
        return self.floor - 1

def init():
    floor = input('What is the floor? ')
    floor_type = input ('US or EU? ')

    print()

    if floor_type == 'US':
        us_floor = USFloor(floor)
        print('US Floor: ', floor)
        print('EU Floor: ', us_floor.toEuropeFloor())
    else:
        eu_floor = EuropeFloor(floor)
        print('EU Floor: ', floor)
        print('US Floor: ', eu_floor.toUSFloor())

init()
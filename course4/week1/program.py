class Person:
    name = None

    def __init__(self, name):
        self.name = name
        print('[' + self.name + '] Creating a person object...')
    
    def __del__(self):
        print('[' + self.name + '] Deleting a person object...')

    def walk(self):
        print('[' + self.name + '] Walking...')

class Programmer(Person):
    language = None

    def code(self, language):
        self.language = language
        print('[' + self.name + '] Coding in ' + self.language + '...')


p1 = Person('Caue Queiroz')
p2 = Person('Thaina Queiroz')
p3 = Programmer('Linus Torvalds')

p1.walk()
p2.walk()
p3.walk()

p3.code('python')

p1 = 12
p2 = 13
p3 = 14
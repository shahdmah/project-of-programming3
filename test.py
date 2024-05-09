


class Person:
 

    def __init__(self, name):
        print(f'Initializing the person object...')
        self.name = name

person = Person('John')

print(person.name)
print(id(person))
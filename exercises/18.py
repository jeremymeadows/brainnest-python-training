# Create a class `Dog` with methods `bark()` and `info()`.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'{self.name} barks')

    def info(self):
        print(f'{self.name} is a {self.breed}')


rex = Dog('Rex', 'dalmation')
fido = Dog('Fido', 'golden retriever')

rex.bark()
fido.bark()

rex.info()
fido.info()

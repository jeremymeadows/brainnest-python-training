# classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def printname(self):
        print(f'Hello my name is {self.name} and I am {self.age} years old')

p1 = Person('John', 30)
print(p1.name)
print(p1.age)
print(p1)

p1.name = 'Mike'
p1.printname()


class Student(Person):
    def __init__(self, name, age, year):
        Person.__init__(self, name, age)
        self.year = year

    def printstudent(self):
        print(self.name, self.age, self.year)

    def get_year(self):
        return f'{self.year}'


x = Student('Kevin', 18, 4)
x.printname()
x.get_year()

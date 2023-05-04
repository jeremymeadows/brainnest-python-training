# Create a Vehicle class with the following attributes: make, model, and year.
# The class should also have the following methods: start(), stop(), and info().

# Create a Car class that inherits from the Vehicle class. The Car class should
# have an additional attribute: num_doors. The class should also have the
# following method: lock_doors().

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('vroom vroom')

    def stop(self):
        print('screech')

    def info(self):
        print(self.make, self.model, self.year)

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        Vehicle.__init__(self, make, model, year)
        self.num_doors = num_doors

    def lock_doors(self):
        print('click ' * self.num_doors)


car = Car('Ford', 'Fiesta', 2016, 4)
car.info()
car.start()
car.stop()
car.lock_doors()

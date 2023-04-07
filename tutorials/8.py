# custom functions

def my_function():
    print("Hello")

my_function()


def name_function(fname):
    print(fname, 'Johnson')

name_function('Emil')
name_function('Tobias')
name_function('Linus')


def full_name_function(fname, lname):
    print(fname, lname)

full_name_function('Emil', 'Johnson')


def my_country(country):
    print('I am from', country)

my_country('Sweden')
my_country('India')
my_country('Brazil')


def times_five(x):
    return x * 5

print(times_five(3))
print(times_five(5))
print(times_five(9))

# decorators

def shout(text):
    return text.upper()

print(shout('hello'))

yell = shout
print(yell('hello'))


def whisper(text):
    return text.lower()

def greet(func):
    print(func('Hi, I am created by a function passed as an argument'))

greet(shout)
greet(whisper)

def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(15)
print(add_15(10))


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print('before function execution')
        val = func(*args, **kwargs)
        print('after function execution')
        return val

    return inner1

def function_to_be_used():
    print('inside function')

function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()


@hello_decorator
def sum_two_numbers(a, b):
    print('inside function')
    return a + b

a, b = 1, 2
print('Sum =', sum_two_numbers(a, b))


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor2
def num():
    return 2

@decor2
@decor1
def num2():
    return 2

print(num())
print(num2())

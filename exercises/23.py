# Write a decorator that repeats a function call a specified number of times

def repeat(func):
    def inner():
        for _ in range(3):
            func()
    return inner

@repeat
def hello():
    print('Hello, world!')

hello()

# Create a decorator my_logger that logs the name of the function being called
# and the arguments it was called with. The logger should output the function
# name and arguments to the console each time the function is called.

def my_logger(func):
    def inner(*args, **kwargs):
        print(f'{func.__name__}({", ".join(map(lambda e: str(e), args))}, {kwargs})')
        return func(*args, **kwargs)
    return inner

@my_logger
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2, b = 3))

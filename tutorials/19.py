# generators

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

x = simpleGeneratorFun()

print(next(x))
print(next(x))
print(next(x))
# print(next(x)) # runs out of items

for i in simpleGeneratorFun():
    print(i)

print(next(simpleGeneratorFun()))
print(next(simpleGeneratorFun()))
print(next(simpleGeneratorFun()))


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = fib(5)
print(next(x))

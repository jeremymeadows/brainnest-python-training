# function arguments

def func(*args):
    for arg in args:
        print(arg)

func('Hello', 'welcome', 'to', 'class')


def positional_func(arg1, *argv):
    print('First argument:', arg1)
    for arg in argv:
        print(arg)

positional_func('Hello')
positional_func('Hello', 'welcome', 'to', 'class')


def object_into_func(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

args = ('this', 'is', 'demo')
object_into_func(*args)

kwargs = { 'arg1': 'this', 'arg2': 'is', 'arg3': 'demo' }
object_into_func(**kwargs)


def args_and_kwargs(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

args_and_kwargs('this', 'is', 'demo', first='this', mid='is', last='demo')


def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

kwargs_func(first='John', age=30)


def more_args(*kids):
    print('The youngest child is', kids[-1])

more_args('Emil', 'Tobias', 'Linus')


def more_kwargs(**kid):
    print('His last name is', kid['last'])

more_kwargs(first='Emil', last='Johnson')


def defaults(country = 'Norway'):
    print('I am from', country)

defaults('Sweden')
defaults('India')
defaults('Brazil')
defaults()

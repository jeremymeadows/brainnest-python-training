# Rewrite the following code using functions and/or loops to make it less
# repetitive:
#
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
# print(f'I am happy to hear that you are feeling {feeling}.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print(f'I am happy to hear that you are feeling {feeling}.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print(f'I am happy to hear that you are feeling {feeling}.')

def check_feelings():
    print('How are you feeling?')
    feeling = input()
    print(f'I am happy to hear that you are feeling {feeling}.\n')


for time in ['morning', 'afternoon', 'evening']:
    print(f'Good {time}!')
    check_feelings()

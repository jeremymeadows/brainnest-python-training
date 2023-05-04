# Rewrite your pay computation with time-and-a-half for overtime (ex 4) and
# create a function called `compute_pay` which takes two parameters (hours and
# rate). Include error handling.

def compute_pay(hours, rate):
    if hours < 0 or rate < 0:
        raise ValueError('cannot be negative')

    pay = hours * rate
    if hours > 40:
        pay += (hours - 40) * (rate * 0.5)
    return pay


try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))

    print(f'Your gross pay is €{compute_pay(hours, rate)}')
except:
    print('sorry, please enter a valid number')

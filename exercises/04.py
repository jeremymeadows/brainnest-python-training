# Rewite your pay coputation (ex 2) to give the employee 1.5 times the hourly
# rate for hours worked above 40. Include some error handling for bad values.

try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))

    if hours < 0 or rate < 0:
        raise ValueError('cannot be negative')

    pay = hours * rate

    if hours > 40:
        pay += (hours - 40) * (rate * 0.5)

    print(f'Your gross pay is €{pay}')
except:
    print('sorry, please enter a valid number')

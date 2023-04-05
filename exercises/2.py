# Write a program to prompt the user for hours and rate per hours to compute
# gross pay.

hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
gross = hours * rate
print(f'Your gross pay is €{gross}')

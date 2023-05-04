# Write a program which repeatedly reads numbers until the user enters `done`.
# Once `done` is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using `try` and `except` and print an error message then skip to the next
# number. Optionally try to find the largest and smallest as well.

from statistics import mean

nums = []
while (num := input('Enter a number: ')) != 'done':
    try:
        nums.append(float(num))
    except ValueError:
        print('invalid input')

print()
print('total:   ', sum(nums))
print('count:   ', len(nums))
print('average: ', mean(nums))
print('largest: ', max(nums))
print('smallest:', min(nums))

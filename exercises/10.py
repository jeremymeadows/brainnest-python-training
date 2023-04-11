# Create a for loop that iterates through a list of numbers and prints the
# largest number in the list

numbers = [30, -47, -84, -75, 48, -51, -36, 98, -34, 66]
largest = None
for number in numbers:
    if not largest or number > largest:
        largest = number
print(largest)

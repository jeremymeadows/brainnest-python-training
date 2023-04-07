# Write a program to prompt for a score between 0.0 and 1.0. If the score is
# out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:
#
# Score   Grade
# >= 0.9  A
# >= 0.8  B
# >= 0.7  C
# >= 0.6  D
# < 0.6   F

def get_grade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'


try:
    score = float(input('Enter a score: '))

    if score < 0 or score > 1:
        raise ValueError('must be between 0 and 1')
except:
    print('sorry, please enter a valid number')
    exit(1)

print(get_grade(score))

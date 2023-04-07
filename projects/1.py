'''
The hangman game is a word guessing game where the player is given a word and
has to guess the letters that make up the word. The player is given a certain
number of tries (no more than 6 wrong guesses are allowed) to guess the correct
letters before the game is over.
'''

# Output
'''
You have 6 tries left.
Used letters:
Word: _ _ _ _
Guess a letter: a

You have 6 tries left.
Used letters: a
Word: _ a _ a
Guess a letter: j

You have 6 tries left.
Used letters: j a
Word: j a _ a
Guess a letter: v
You guessed the word java!
'''

word = 'sphynx'
tries = 6
guesses = []

while tries > 0:
    print(f'You have {tries} {"tries" if tries > 1 else "try"} left.')
    print(f'Used letters: {" ".join(reversed(guesses))}')
    print(f'Word: {" ".join(["_" if char not in guesses else char for char in word])}')

    while not (guess := input('Guess a letter: ')) or guess in guesses:
        if guess != '':
            print(f'You already guessed {guess}')
    guesses.append(guess)
    print()

    if guess not in word:
        tries -= 1
    elif all([char in guesses for char in word]):
        print(f'You guessed the word: {word}!')
        break
else:
    print(f'Out of tries, the word was: {word}.')

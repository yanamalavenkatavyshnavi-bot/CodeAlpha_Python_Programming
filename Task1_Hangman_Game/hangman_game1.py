import random

words = ["python", "apple", "computer", "school", "program"]
word = random.choice(words)

guessed = []
wrong = 0

print("WELCOME TO HANGMAN")

while wrong < 6:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print("Wrong guess! Remaining:", 6 - wrong)

if wrong == 6:
    print("Game Over!")
    print("The word was:", word)

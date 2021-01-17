# Write your code here
import random


def menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == "play":
            return True
        elif choice == "exit":
            return False


# najpierws lista słów
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hidden_word = list("-" * len(word))
letters = set(word)
wrong_letters = set()

lives = 8

print("H A N G M A N")

while menu():

    while lives > 0 and "-" in hidden_word:
        print()
        print("".join(hidden_word))
        guess = input("Input a letter: ")

        # sprawdzamy, czy 1 znak
        if len(guess) != 1:
            print("You should input a single letter")
            continue

        # sprawdzamy, czy mała litera łacińska
        if not (guess.islower() and guess.isalpha()):
            print("Please enter a lowercase English letter")
            continue

        if guess in letters:
            if guess not in hidden_word:
                for n in range(len(word)):
                    if word[n] == guess:
                        hidden_word[n] = guess
            else:
                print("You've already guessed this letter")
                continue
        elif guess in wrong_letters:
            print("You've already guessed this letter")
            continue
        else:
            print("That letter doesn't appear in the word")
            wrong_letters.add(guess)
            lives -= 1

    if lives > 0:
        print()
        print(word)
        print("You guessed the word!")
        print("You survived!")
        print()
    else:
        print("You lost!")
        print()

# print()
# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")

# Stage 4/8
# # Write your code here
# import random
#
# # najpierws lista słów
# words = ['python', 'java', 'kotlin', 'javascript']
# word = random.choice(words)
#
# print("H A N G M A N")
# print("Guess the word: " + word[0:3] + "-" * (len(word) - 3))
#
# guess = input()
#
# if guess == word:
#     print("You survived!")
# else:
#     print("You lost!")

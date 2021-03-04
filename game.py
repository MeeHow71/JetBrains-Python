# Write your code here
import random

# otwieramy plik z wynikami i tworzymy tablicę wyników
scores = {}
score_file = open('rating.txt', 'r', encoding='utf-8')
for line in score_file:
    name, score = line.split()
    scores[name] = int(score)

name = input("Enter your name: ")
print("Hello,", name)

if name not in scores:
    scores[name] = 0

user_choices = input("> ")

if user_choices == "":
    choices = ['rock', 'paper', 'scissors']
else:
    choices = user_choices.split(',')

print("Okay, let's start")

end = len(choices)

user_choice = input()

while user_choice != '!exit':
    if user_choice in choices:
        computer_choice = random.randrange(0, end)

        result = (choices.index(user_choice) - computer_choice) % end

        if result == 0:
            print("There is a draw (" + choices[computer_choice] + ")")
            scores[name] += 50
        elif result <= (end - 1) // 2:
            print("Well done. The computer chose", choices[computer_choice], "and failed")
            scores[name] += 100
        else:  # result > end // 2:
            print("Sorry, but the computer chose", choices[computer_choice])

    elif user_choice == '!rating':
        print("Your rating:", scores[name])
    else:
        print("Invalid input")

    user_choice = input()

out = open('rating.txt', 'w', encoding='utf-8')

for obj in scores.items():
    print(obj[0], obj[1], file=out)

out.close()

print("Bye!")

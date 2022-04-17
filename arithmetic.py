# write your code here
import random


def ok():
    print("Right!")


def nok():
    print("Wrong!")


def check_input():
    while True:
        try:
            entry = int(input())
            return entry
        except ValueError:
            print("Incorrect format.")


def ask_user():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    oper = random.randint(1, 3)  # 1+, 2-, 3*

    if oper == 1:
        print(str(a), '+', str(b))
        answer = check_input()
        if answer == a + b:
            ok()
            return True
        else:
            nok()
            return False
    elif oper == 2:
        print(str(a), '-', str(b))
        answer = check_input()
        if answer == a - b:
            ok()
            return True
        else:
            nok()
            return False
    elif oper == 3:
        print(str(a), '*', str(b))
        answer = check_input()
        if answer == a * b:
            ok()
            return True
        else:
            nok()
            return False


def ask_square():
    a = random.randint(11, 29)
    print(a)
    answer = check_input()
    if answer == a * a:
        ok()
        return True
    else:
        nok()
        return False


# tu się zaczyna program
level = 0  # brak określonego poziomu
levels = ["simple operations with numbers 2-9",
          "integral squares of 11-29"]

while True:
    print("Which level do you want? Enter a number:")
    print("1 - " + levels[0])
    print("2 - " + levels[1])
    level = int(input())
    if level in [1, 2]:
        break
    else:
        print("Incorrect format")

correct_answers = 0

for _ in range(5):
    if level == 1:
        if ask_user():
            correct_answers += 1
    elif level == 2:
        if ask_square():
            correct_answers += 1

print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")

ask_write = input()
if ask_write in ["yes", "YES", "y", "Yes"]:
    print("What is your name?")
    name = input()
    result_file = open("results.txt", "a", encoding="UTF-8")
    result_file.write(name + ": " + str(correct_answers) + "/5 in level " + str(level)
                      + " (" + levels[level - 1] + ")")
    result_file.close()
    print('The results are saved in "results.txt".')

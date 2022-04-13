# write your code here
import random


friends = {}

print("Enter the number of friends joining (including you):")
num_of_friends = int(input())

if num_of_friends < 1:
    print("No one is joining for the party")
    exit(0)

print("Enter the name of every friend (including you), each on a new line:")
for _ in range(num_of_friends):
    name = input()
    friends[name] = 0

print("Enter the total bill value:")
bill_value = float(input())

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
use_lucky = input()
if use_lucky == "Yes":
    friends_list = list(friends)
    lucky = random.randint(0, num_of_friends - 1)
    name = friends_list[lucky]
    print(f"{name} is the lucky one!")
    splitted_bill = round(bill_value / (num_of_friends - 1), 2)
    for fname in friends:
        if fname != name:
            friends[fname] = splitted_bill
        else:
            friends[fname]
    print(friends)
else:
    print("No one is going to be lucky")
    splitted_bill = round(bill_value / num_of_friends, 2)
    for fname in friends:
        friends[fname] = splitted_bill
    print(friends)

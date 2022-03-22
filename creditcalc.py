import argparse
import math
import sys


def wrong_args():
    print("Incorrect parameters")
    sys.exit()


def calc_diff(argi):
    # do obliczeń DIFF potrzebne są: principal, periods oraz interest
    if argi.interest is None or argi.principal is None or argi.periods is None:
        wrong_args()
    elif argi.principal < 0 or argi.periods < 0:
        wrong_args()
    elif argi.payment is not None:
        wrong_args()
    else:
        p = argi.principal
        n = argi.periods
        i = argi.interest / 12 / 100
        total = 0
        for m in range(n):
            d = math.ceil(p / n + i * (p - p * (m + 1 - 1) / n))
            total += d
            print("Month " + str(m+1) + ": payment is", d)
        print()
        print("Overpayment =", total - p)


def calc_annuity(argi):
    # obliczamy brakujący parametr

    # tu obliczamy Annuity Payment
    if argi.payment is None:
        if argi.principal < 0 or argi.periods < 0:
            wrong_args()
        credit_principal = argi.principal
        periods = argi.periods
        interest = argi.interest
        # nominal interest rate:
        i = interest / 12 / 100
        annuity = credit_principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1)
        annuity = math.ceil(annuity)
        print("Your annuity payment = " + str(annuity) + "!")
        print("Overpayment =", annuity * periods - credit_principal)

    # tu obliczamy Principal
    if argi.principal is None:
        payment = argi.payment
        periods = argi.periods
        # nominal interest rate:
        i = argi.interest / 12 / 100
        credit_principal = payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
        credit_principal = math.floor(credit_principal)
        print("Your credit principal = " + str(credit_principal) + "!")
        print("Overpayment =", payment * periods - credit_principal)

    # tu obliczamy Periods
    if argi.periods is None:
        credit_principal = argi.principal
        payment = argi.payment
        # nominal interest rate:
        i = argi.interest / 12 / 100
        # count of periods:
        n = math.log(payment/(payment - i * credit_principal), 1 + i)
        n = math.ceil(n)
        # print("n = ", n)
        years = n // 12
        months = n % 12
        # print(years, months)
        if years == 0:
            if months == 1:
                print("You need 1 month to repay this credit!")
            else:
                print("You need " + str(months) + " months to repay this credit!")
        elif years == 1:
            info = "You need 1 year"
            if months > 1:
                info += " and " + str(months) + " months"
            elif months == 1:
                info += " and " + str(months) + " month"
            info += " to repay this credit!"
            print(info)
        else:
            info = "You need " + str(years) + " years"
            if months > 1:
                info += " and " + str(months) + " months"
            elif months == 1:
                info += " and " + str(months) + " month"
            info += " to repay this credit!"
            print(info)
        print("Overpayment =", payment * n - credit_principal)


parser = argparse.ArgumentParser()
# Tu dodajemy argumenty do funkcji
# Potem trzeba usunąć niepotrzebne wpisy
parser.add_argument('--type', type=str, help='Typ czegośtam')
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int, help='Wartość dla x')
parser.add_argument('--periods', type=int, help='Wartość całkowita y')
parser.add_argument('--interest', type=float, help='Wartość całkowita y')

# Ta część jest tylko do celów sprawdzania parametrów
args = parser.parse_args()
# print(parser)
# print(args)
# print(args.type)
# print(args.principal)
# print(args.periods)
# print(args.interest)
# print("Number of arguments given:", len(sys.argv))

# Do poprawnego działania potrzebujemy 4 parametrów
if len(sys.argv) != 5:
    wrong_args()

# Musimy mieć oprocentowanie i to dodatnie
if args.interest is None or args.interest < 0:
    wrong_args()

# Możemy obliczać albo Annuity albo Differentiated
if args.type == 'annuity':
    calc_annuity(args)
elif args.type == 'diff':
    calc_diff(args)
else:
    wrong_args()

# import math
#
# print("What do you want to calculate?")
# print('type "n" - for the count of months,')
# print('type "a" - for the annuity monthly payment,')
# print('type "p" - for the credit principal:')
# choice = input()
# if choice == 'n':
#     print("Enter the credit principal:")
#     credit_principal = int(input())
#     print("Enter the monthly payment:")
#     payment = int(input())
#     print("Enter the credit interest:")
#     interest = float(input())
#     # nominal interest rate:
#     i = interest / 12 / 100
#     # count of periods:
#     n = math.log(payment/(payment - i * credit_principal), 1 + i)
#     n = math.ceil(n)
#     print("n = ", n)
#     years = n // 12
#     months = n % 12
#     print(years, months)
#     if years == 0:
#         if months == 1:
#             print("You need 1 month to repay this credit!")
#         else:
#             print("You need " + str(months) + " months to repay this credit!")
#     elif years == 1:
#         info = "You need 1 year"
#         if months > 1:
#             info += " and " + str(months) + " months"
#         elif months == 1:
#             info += " and " + str(months) + " month"
#         info += " to repay this credit!"
#         print(info)
#     else:
#         info = "You need " + str(years) + " years"
#         if months > 1:
#             info += " and " + str(months) + " months"
#         elif months == 1:
#             info += " and " + str(months) + " month"
#         info += " to repay this credit!"
#         print(info)
# if choice == 'a':
#     print("Enter the credit principal:")
#     credit_principal = int(input())
#     print("Enter the number of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     interest = float(input())
#     # nominal interest rate:
#     i = interest / 12 / 100
#     annuity = credit_principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1)
#     annuity = math.ceil(annuity)
#     print("Your annuity payment = " + str(annuity) + "!")
# if choice == 'p':
#     print("Enter the monthly payment:")
#     payment = float(input())
#     print("Enter the count of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     interest = float(input())
#     # nominal interest rate:
#     i = interest / 12 / 100
#     credit_principal = payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
#     credit_principal = math.floor(credit_principal)
#     print("Your credit principal = " + str(credit_principal) + "!")
#
#
#
#
#
# print("Enter the credit principal")
# credit_principal = int(input())
# print("What do you want to calculate?")
# print('type "m" - for the count of months,')
# print('type "p" - for the monthly payment:')
# choice = input()
# if choice == 'm':
#     print("Enter the monthly payment:")
#     payment = int(input())
#     # tu kontynuacja
#     count = credit_principal // payment
#     if credit_principal % payment != 0:
#         count += 1
#     if count == 1:
#         print("It takes " + str(count) + " month to repay the credit")
#     else:
#         print("It takes " + str(count) + " months to repay the credit")
# if choice == 'p':
#     print("Enter the count of months:")
#     months = int(input())
#     # tu kontynuacja
#     payment = credit_principal // months
#     if credit_principal % months == 0:
#         print("Your monthly payment = " + str(payment))
#     else:
#         payment += 1
#         lastpayment = credit_principal - (months - 1) * payment
#         print("Your monthly payment = " + str(payment) + " with last monthly payment = " + str(lastpayment))
#
# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'
#
# # write your code here
# print(credit_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

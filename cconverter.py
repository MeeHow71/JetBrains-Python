import requests
import json


currency_code = input()

url = "http://www.floatrates.com/daily/" + currency_code.lower() + ".json"

rates = {currency_code: 1}
# rates[currency_code] = 1

r = requests.get(url)
json_table = r.text
dict_table = json.loads(json_table)

if currency_code.lower() == "eur":
    rates['usd'] = dict_table['usd']['rate']
elif currency_code.lower() == "usd":
    rates['eur'] = dict_table['eur']['rate']
else:
    rates['usd'] = dict_table['usd']['rate']
    rates['eur'] = dict_table['eur']['rate']

# dest_currency = input()

while True:
    dest_currency = input()
    if dest_currency == "":
        break
    amount = float(input())
    if dest_currency in rates:
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        result = amount * rates[dest_currency]
        print("You received", round(result, 2), dest_currency)
    else:
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        rates[dest_currency] = dict_table[dest_currency.lower()]['rate']
        result = amount * rates[dest_currency]
        print("You received", round(result, 2), dest_currency)

    # dest_currency = input()


# print(table)
# print(table['usd'])


# rates = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
#
# amount = float(input(""))
#
#
# def convert(amount, currency):
#     result = amount * rates[currency]
#     print("I will get", round(result, 2), currency, "from the sale of", amount, "conicoins.")
#
#
# convert(amount, 'RUB')
# convert(amount, 'ARS')
# convert(amount, 'HNL')
# convert(amount, 'AUD')
# convert(amount, 'MAD')
#
# # # write your code here!
# # coni = float(input("Please, enter the number of conicoins you have: > "))
# # exch = float(input("Please, enter the exchange rate: > "))
# # total = coni * exch
# # print("The total amount of dollars:", total)
# #
# # # coni = int(input())
# # # print("I have", coni, "conicoins.")
# # # print(coni, "conicoins cost", coni * 100, "dollars")
# # # print("I am rich! Yippee!")

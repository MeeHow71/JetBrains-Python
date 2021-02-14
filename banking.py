# Write your code here
import random
import sqlite3

# dolny i górny zakres generowanych numerów
# self.account_number = random.randrange(10000000000, 20000000000)
lower_range = 1000000000
upper_range = 2000000000


# to jest funkcja do generowania numeru karty
def luhn(temp_number):
    # print("temp_number", temp_number)
    digits = []
    for digit in temp_number:
        digits.append(int(digit))
    # print("digits:", digits)

    for _i in range(0, len(digits), 2):
        digits[_i] *= 2
    # print("odd * 2", digits)

    for _i in range(len(digits)):
        if digits[_i] > 9:
            digits[_i] -= 9
    # print("subtract", digits)

    summa = 0
    for digit in digits:
        summa += digit
    # 1print("summa:", summa)

    last_digit = 0
    if summa % 10 != 0:
        last_digit = 10 - summa % 10

    return str(last_digit)


# def generate_card_number():
#     # jeśli lista kont jest pusta, to po prostu tworzymy nowe
#     # jeśli jest już tam cokolwiek, to musimy sprawdzić, czy coś się nie powtarza
#     if not accounts:
#         # temp_number = "400000844943340"
#         temp_number = "400000" + str(random.randrange(lower_range, upper_range))[1:]
#         last_digit = luhn(temp_number)
#         temp_number += last_digit
#         return temp_number
#
#     # tu sprawdzamy czy się nie powtarza:
#     # robimy to tak: 1. stwórz numer, 2. sprawdź, czy się powarza, 3. jeśli tak - powtórz.
#     while True:
#         temp_number = "400000" + str(random.randrange(lower_range, upper_range))[1:]
#         # temp_number = "400000844943340"
#         last_digit = luhn(temp_number)
#         temp_number += last_digit
#
#         num_of_repetitions = 0
#         for account in accounts:
#             if account.card_number == temp_number:
#                 num_of_repetitions += 1
#
#         if num_of_repetitions == 0:
#             return temp_number


# dane o kontach będziemy trzymać w klasie Account
# class Account:
#     def __init__(self):
#         # PIN może się powtarzać, ale numer karty / konta musi być unikalny
#         # dlatego generujemy przy pomocy funkcji
#         self.card_number = generate_card_number()
#
#         # tu generujemy PIN:
#         self.pin = str(random.randrange(10000, 20000))[1:]
#
#         # na końcu informacja o stanie konta.
#         self.balance = 0
#
#         print()
#         print("Your card has been created")
#         print("Your card number:")
#         print(self.card_number)
#         print("Your card PIN:")
#         print(self.pin)


def check_luhn(dest_card):
    digits = []
    for digit in dest_card:
        digits.append(int(digit))

    # usuwamy ostatni element
    last = digits.pop()

    for _i in range(0, len(digits), 2):
        digits[_i] *= 2

    for _i in range(len(digits)):
        if digits[_i] > 9:
            digits[_i] -= 9

    summa = 0
    for digit in digits:
        summa += digit

    if (summa + last) % 10 == 0:
        return True
    else:
        return False


def transfer(source_card_idx):
    print("Enter card number:")
    dest_card = input(">")
    if check_luhn(dest_card):
        sql_select_dest = '''SELECT * FROM card WHERE number = ?'''
        cur.execute(sql_select_dest, (dest_card,))
        dest_record = cur.fetchone()
        if dest_record:
            dest_card_idx = dest_record[0]
            print("Enter how much money you want to transfer:")
            how_much = int(input(">"))
            sql_select_source = '''SELECT * FROM card WHERE id = ?'''
            cur.execute(sql_select_source, (source_card_idx,))
            source_record = cur.fetchone()
            if source_record[3] > how_much:
                new_balance_source = source_record[3] - how_much
                new_balance_dest = dest_record[3] + how_much
                sql_update_balance = '''UPDATE card SET balance = ? WHERE id = ?'''
                cur.execute(sql_update_balance, (new_balance_source, source_card_idx))
                conn.commit()
                cur.execute(sql_update_balance, (new_balance_dest, dest_card_idx))
                conn.commit()
                print("Success!")
            else:
                print("Not enough money!")
        else:
            print("Such a card does not exist.")
    else:
        print("Probably you made a mistake in the card number. Please try again!")


def logged_in(idx):
    print()
    print("You have successfully logged in!")

    while True:
        print()
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        choice = input(">")
        if choice == "1":
            sql_select_idx = '''SELECT * FROM card WHERE id = ?'''
            cur.execute(sql_select_idx, (idx,))
            record = cur.fetchone()
            print("Balance:", record[3])
        elif choice == "2":
            sql_select_idx = '''SELECT * FROM card WHERE id = ?'''
            cur.execute(sql_select_idx, (idx,))
            record = cur.fetchone()
            print("Enter income:")
            income = int(input(">")) + record[3]
            sql_update_balance = '''UPDATE card SET balance = ? WHERE id = ?'''
            cur.execute(sql_update_balance, (income, idx))
            conn.commit()
            print("Income was added!")
        elif choice == "3":
            print()
            print("Transfer")
            transfer(idx)
        elif choice == "4":
            sql_close_account = '''DELETE FROM card WHERE id = ?'''
            cur.execute(sql_close_account, (idx,))
            conn.commit()
            print("The account has been closed!")
            break
        elif choice == "5":
            break
        elif choice == "0":
            print("Bye!")
            exit()


def login():
    print()
    print("Enter your card number:")
    card_number = input(">")
    print("Enter your PIN:")
    pin_number = input(">")

    sql_sel_find_card = '''SELECT * FROM card WHERE number = ?'''
    cur.execute(sql_sel_find_card, (card_number,))
    records = cur.fetchall()

    # DEBUG:
    # print(records[0])

    if len(records) > 0:
        if records[0][2] == pin_number:
            print("Idziemy dalej z indeksem: ", records[0][0])
            logged_in(records[0][0])
        else:
            print()
            print("Wrong card number or PIN!")
    else:
        print()
        print("Wrong card number or PIN!")

    # poniższe zmienne zapisuje, czy istnieje konto i czy PIN jest prawidłowy
    # account_ok = 0
    # pin_ok = 0
    # idx = None
    # for account in accounts:
    #     if account.card_number == card_number:
    #         account_ok = 1
    #         if account.pin == pin_number:
    #             pin_ok = 1
    #             idx = accounts.index(account)
    #             break
    
    # if account_ok and pin_ok:
    #     logged_in(idx)
    # else:
    #     print()
    #     print("Wrong card number or PIN!")


def create_an_account():
    # najpierw sprawdzimy, czy w bazie jest choć jedno konto
    sqlite_select_check = '''SELECT * FROM card'''
    cur.execute(sqlite_select_check)
    records = cur.fetchall()

    temp_number = []

    if not records:
        # temp_number = "400000844943340"
        temp_number = "400000" + str(random.randrange(lower_range, upper_range))[1:]
        last_digit = luhn(temp_number)
        temp_number += last_digit

    # tu sprawdzamy czy się nie powtarza:
    # robimy to tak: 1. stwórz numer, 2. sprawdź, czy się powarza, 3. jeśli tak - powtórz.
    num_of_repetitions = 1
    while num_of_repetitions != 0:
        temp_number = "400000" + str(random.randrange(lower_range, upper_range))[1:]
        # temp_number = "400000844943340"
        last_digit = luhn(temp_number)
        temp_number += last_digit

        num_of_repetitions = 0
        for row in records:
            if row[1] == temp_number:
                num_of_repetitions += 1

    # teraz pin:
    pin = str(random.randrange(10000, 20000))[1:]

    # na koniec balance:
    # balance = 0

    # polecenie wstawienia rekordu
    # sqlite_insert = '''INSERT INTO card (id, number, pin, balance)
    #                    VALUES (?, ?, ?, ?);'''

    # teraz zrobimy to inaczej:
    # wstawimy rekord, ale tylko z numerem karty i pinem
    # id jest AUTOINCREMENT, a balance DEFAULT 0
    sqlite_insert = '''INSERT INTO card (number, pin)
                       VALUES (?, ?);'''

    # krotka z danymi
    data_tuple = (temp_number, pin)
    # print("Dodajemy: ", data_tuple)

    # wykonaj dodanie
    cur.execute(sqlite_insert, data_tuple)

    # potwierdź
    conn.commit()

    print()
    print("Your card has been created")
    print("Your card number:")
    print(temp_number)
    print("Your card PIN:")
    print(pin)


def main_menu():
    while True:
        print()
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = input(">")
        if choice == "1":
            create_an_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break


#############
#   START   #
#############
# listę kart będziemy trzymać na liście kont:
# accounts = []

# łączymy się z bazą danych:
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

# TODO: tu kontynuujemy!
# Trzeba zmienić sposób tworzenia tabeli na Autoincrement
# również dodawanie kont (bez id)

# print("Database created and Successfully Connected to SQLite")
# sqlite_select_Query = "SELECT name FROM sqlite_master WHERE type='table' AND name='card';"
# cur.execute(sqlite_select_Query)
# record = cur.fetchone()
# print("Wynik zapytania o tabelkę to: ", record)
#
# if not record:
#     print("no nie ma tabelki")
#     sqlite_create_table_query = '''CREATE TABLE card (
#                                 id INTEGER PRIMARY KEY,
#                                 number TEXT NOT NULL,
#                                 pin TEXT UNIQUE,
#                                 balance INTEGER DEFAULT 0);'''
sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS card (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            number TEXT NOT NULL UNIQUE,
                            pin TEXT,
                            balance INTEGER DEFAULT 0);'''

cur.execute(sqlite_create_table_query)
record = cur.fetchall()
# print("oto co wyszło: ", record)
# print("Tabelka utworzona")
# else:
# print("Tabelka istnieje: ", record)

# i startujemy:
main_menu()
cur.close()

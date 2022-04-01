class CoffeeMachine:
    # czy będą potrzebne jakieś zmienne klasowe?

    def __init__(self):
        self.state = "waiting"
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def print_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")

    def make_coffee(self, rwater, rmilk, rcofee, rmoney):
        missing = ""
        if self.water >= rwater and self.milk >= rmilk and self.coffee >= rcofee and self.cups >= 1:
            self.water -= rwater
            self.milk -= rmilk
            self.coffee -= rcofee
            self.cups -= 1
            self.money += rmoney
            print("I have enough resources, making you a coffee!")
            self.state = "waiting"
        else:
            if self.water < rwater:
                missing += "water"
            if self.milk < rmilk:
                missing += " milk"
            if self.coffee < rcofee:
                missing += " coffee"
            if self.cups < 1:
                missing += " cups"
            print("Sorry, not enough", missing + '!')
            self.state = "waiting"

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def process_input(self, user_input):
        self.user_input = user_input
        if self.state == "waiting" and self.user_input == "remaining":
            self.print_status()
        elif self.state == "waiting" and self.user_input == "buy":
            self.state = "choosing coffee"
        elif self.state == "waiting" and self.user_input == "fill":
            self.state = "filling"
        elif self.state == "waiting" and self.user_input == "take":
            self.take()
        else:
            print(self.user_input)


cm = CoffeeMachine()

while True:
    if cm.state == "waiting":
        print()
        print("Write action (buy, fill, take, remaining, exit)")
        choice = input("> ")
        if choice != "exit":
            cm.process_input(choice)
        else:
            break
    elif cm.state == "choosing coffee":
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input("> ")
        if choice == "1":
            cm.make_coffee(250, 0, 16, 4)
        elif choice == "2":
            cm.make_coffee(350, 75, 20, 7)
        elif choice == "3":
            cm.make_coffee(200, 100, 12, 6)
        elif choice == "back":
            cm.state = "waiting"
    elif cm.state == "filling":
        print("Write how many ml of water do you want to add:")
        cm.water += int(input("> "))

        print("Write how many ml of milk do you want to add:")
        cm.milk += int(input("> "))

        print("Write how many grams of coffee beans do you want to add:")
        cm.coffee += int(input("> "))

        print("Write how many disposable cups of coffee do you want to add:")
        cm.cups += int(input("> "))

        cm.state = "waiting"


# # Write your code here
# # zasoby
# water = 400
# milk = 540
# coffee = 120
# cups = 9
# money = 550
#
#
# def print_status():
#     print("The coffee machine has:")
#     print(water, "of water")
#     print(milk, "of milk")
#     print(coffee, "of coffee beans")
#     print(cups, "of disposable cups")
#     print("$" + str(money), "of money")
#
#
# # tu trzeba zrobić funkcję zarządzającą zasobami ekspresu
# # przy wyborze co kupić sprawdzi, czy mamy wystarczająco zasobów
# # i odpowiednio ustawi ich poziom.
# def make_coffee(rwater, rmilk, rcofee, rmoney):
#     global water, milk, coffee, cups, money
#     missing = ""
#     if water >= rwater and milk >= rmilk and coffee >= rcofee and cups >= 1:
#         water -= rwater
#         milk -= rmilk
#         coffee -= rcofee
#         cups -= 1
#         money += rmoney
#         print("I have enough resources, making you a coffee!")
#     else:
#         if water < rwater:
#             missing += "water"
#         if milk < rmilk:
#             missing += " milk"
#         if coffee < rcofee:
#             missing += " coffee"
#         if cups < 1:
#             missing += " cups"
#         print("Sorry, not enough", missing + '!')
#
#
# def buy():
#     global water
#     global milk
#     global coffee
#     global cups
#     global money
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
#     choice = input("> ")
#     if choice == "1":
#         make_coffee(250, 0, 16, 4)
#     elif choice == "2":
#         make_coffee(350, 75, 20, 7)
#     elif choice == "3":
#         make_coffee(200, 100, 12, 6)
#     elif choice == "back":
#         return
#
#
# def fill():
#     print("Write how many ml of water do you want to add:")
#     global water
#     water += int(input("> "))
#
#     print("Write how many ml of milk do you want to add:")
#     global milk
#     milk += int(input("> "))
#
#     print("Write how many grams of coffee beans do you want to add:")
#     global coffee
#     coffee += int(input("> "))
#
#     print("Write how many disposable cups of coffee do you want to add:")
#     global cups
#     cups += int(input("> "))
#
#
# def take():
#     global money
#     print("I gave you $" + str(money))
#     money = 0
#
#
# while True:
#     print()
#     print("Write action (buy, fill, take, remaining, exit)")
#     choice = input("> ")
#     if choice == "buy":
#         buy()
#     elif choice == "fill":
#         fill()
#     elif choice == "take":
#         take()
#     elif choice == "remaining":
#         print_status()
#     elif choice == "exit":
#         break
#
# # print()
# # print_status()
# #
# # print("Write how many ml of water the coffee machine has:")
# # water = int(input("> "))
# # print("Write how many ml of milk the coffee machine has:")
# # milk = int(input("> "))
# # print("Write how many grams of coffee beans the coffee machine has:")
# # coffee = int(input("> "))
# # print("Write how many cups of coffee you will need:")
# # cups = int(input("> "))
# #
# # max_num = 0
# #
# # water_needed = 200 * cups
# # milk_needed = 50 * cups
# # coffee_needed = 50 * cups
# #
# # if water // 200 > 0:
# #     max_num = water // 200
# # if milk // 50 < max_num:
# #     max_num = milk // 50
# # if coffee // 15 < max_num:
# #     max_num = coffee // 15
# #
# # if max_num < cups:
# #     print("No, I can make only " + str(max_num) + " cups of coffee")
# # elif max_num == cups:
# #     print("Yes, I can make that amount of coffee")
# # else:
# #     print("Yes, I can make that amount of coffee (and even "
# #     + str(max_num - cups) + " more than that)")
# #
# # #
# # # print("For " + str(cups) + " cups of coffee you will need:")
# # # print(str(200 * cups) + " ml of water")
# # # print(str(50 * cups) + " ml of milk")
# # # print(str(15 * cups) + " g of coffee beans")

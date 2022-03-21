def print_board(symbols):
    print("---------")
    print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
    print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
    print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
    print("---------")


def get_state(inp):
    grid_full = '_' not in inp
    lines = [inp[:3], inp[3:6], inp[6:], inp[::3], inp[1::3], inp[2::3], inp[::4], inp[2:7:2]]
    o_victory_count = lines.count(['O', 'O', 'O'])
    x_victory_count = lines.count(['X', 'X', 'X'])
    # o_victory_count = lines.count('OOO')
    # x_victory_count = lines.count('XXX')
    # print(o_victory_count, x_victory_count, grid_full, inp.count('O'), inp.count('X'))
    if abs(inp.count('O') - inp.count('X')) > 1 or o_victory_count + x_victory_count > 1:
        return 'Impossible'
    if o_victory_count + x_victory_count == 0:
        if grid_full:
            print("Draw")
            exit(0)
            # return 'Draw'
        # return 'Game not finished'
    if x_victory_count:
        print("X wins")
        exit(0)
    elif o_victory_count:
        print("O wins")
        exit(0)
    # return 'X wins' if x_victory_count else 'O wins'


# def impos():
#     print("Impossible")
#     exit(0)


# def check_board(symbols):
#     # najpierw sprawdzamy, czy znaki są w określonym zakresie
#     for n in range(len(symbols)):
#         if symbols[n] not in "XO_":
#             print("Wrong symbols")
#
#     # posumujmy X i O, żeby określić, czy tak może być
#     x, y, empty = 0, 0, 0
#     for n in range(len(symbols)):
#         if symbols[n] == "X":
#             x += 1
#         if symbols[n] == "O":
#             y += 1
#         if symbols[n] == "_" or symbols[n] == " ":
#             empty += 1
#     # print("x =", x)
#     # print("y =", y)
#     # print("x - y =", abs(x - y))
#     if abs(x - y) > 1:
#         impos()
#
#     # potem sprawdźmy ile jest warunków wygrywających
#     x_wins, y_wins = 0, 0
#     # dla X:
#     for n in range(3):
#         if symbols[n] == "X" and symbols[n + 3] == "X" and symbols[n + 6] == "X":
#             x_wins += 1
#     for n in range(0, 7, 3):
#         if symbols[n] == "X" and symbols[n + 1] == "X" and symbols[n + 2] == "X":
#             x_wins += 1
#     if symbols[0] == "X" and symbols[4] == "X" and symbols[8] == "X":
#         x_wins += 1
#     if symbols[2] == "X" and symbols[4] == "X" and symbols[6] == "X":
#         x_wins += 1
#     # dla O:
#     for n in range(3):
#         if symbols[n] == "O" and symbols[n + 3] == "O" and symbols[n + 6] == "O":
#             y_wins += 1
#     for n in range(0, 7, 3):
#         if symbols[n] == "O" and symbols[n + 1] == "O" and symbols[n + 2] == "O":
#             y_wins += 1
#     if symbols[0] == "O" and symbols[4] == "O" and symbols[8] == "O":
#         y_wins += 1
#     if symbols[2] == "O" and symbols[4] == "O" and symbols[6] == "O":
#         y_wins += 1
#
#     if x_wins + y_wins > 1:
#         impos()
#     elif x_wins == 1:
#         print("X wins")
#         exit(0)
#     elif y_wins == 1:
#         print("O wins")
#         exit(0)
#
#     # jeśli nie ma warunków wygrywających, to sprawdźmy, czy jest remis, czy też gra
#     # nie jest jeszcze skończona
#     if empty == 0:
#         print("Draw")
#     else:
#         print("Game not finished")


def enter_move(symbols):
    correct_entry = False
    # x, y = 0, 0
    position = 9

    while not correct_entry:
        temp = input("Enter the coordinates: ").split()
        x_string, y_string = "a", "a"
        # x_string, y_string = input("Enter the coordinates: ").split()
        if len(temp) > 0:
            x_string = temp[0]
        if len(temp) > 1:
            y_string = temp[1]
        if x_string not in "0123456789" or y_string not in "0123456789":
            print("You should enter numbers!")
            continue
        x = int(x_string)
        y = int(y_string)
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        # TODO: tu poprawić obliczanie pozycji
        # position = -3 * y + 9 + x - 1
        position = 3 * (x - 1) + y - 1
        if symbols[position] == "X" or symbols[position] == "O":
            print("This cell is occupied! Choose another one!")
            continue
        correct_entry = True

    global entry_symbol

    symbols[position] = entry_symbol
    if entry_symbol == "X":
        entry_symbol = "O"
    else:
        entry_symbol = "X"

    print_board(symbols)

    return symbols


# tutaj program się zaczyna
entry_symbol = "X"
board = ["_" for _ in range(9)]
# board = 9*"_"
print_board(board)

for _ in range(9):
    board = enter_move(board)
    get_state(board)

#
#
#
#
#
#
#

# check_board(board)

# symbols = input("Enter cells: ")
#
# print("---------")
# print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
# print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
# print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
# print("---------")
#
# # # write your code here
# # print("XOX")
# # print("OXO")
# # print("XXO")

# inne piękne rozwiązanie
# def get_state(inp):
#     grid_full = '_' not in inp
#     lines = [inp[:3], inp[3:6], inp[6:], inp[::3], inp[1::3], inp[2::3], inp[::4], inp[2:7:2]]
#     o_victory_count = lines.count('OOO')
#     x_victory_count = lines.count('XXX')
#     # print(o_victory_count, x_victory_count, grid_full, inp.count('O'), inp.count('X'))
#     if abs(inp.count('O') - inp.count('X')) > 1 or o_victory_count + x_victory_count > 1:
#         return 'Impossible'
#     if o_victory_count + x_victory_count == 0:
#         if grid_full:
#             return 'Draw'
#         return 'Game not finished'
#     return 'X wins' if x_victory_count else 'O wins'
#
# inp = input()
# grid = [' '.join(list(inp[i:i+3])) for i in range(0, len(inp), 3)]
# grid_with_frame = ['-' * 9, *['| ' + elem + ' |' for elem in grid], '-' * 9]
# print(*grid_with_frame, sep="\n")
# print(get_state(inp))

# albo takie:
# i = input()
# winner = [i[0:3], i[3:6], i[6:9], i[0] + i[3] + i[6], i[1] + i[4] + i[7], i[2] + i[5] + i[8], i[0] + i[4] + i[8], i[2] + i[4] + i[6]]
# def board(x):
#     print(f'''---------
# | {i[0]} {i[1]} {i[2]} |
# | {i[3]} {i[4]} {i[5]} |
# | {i[6]} {i[7]} {i[8]} |
# ---------''')
# board(i)
# print(winner)
# if ('XXX' in winner and 'OOO' in winner) or abs(i.count('X') - i.count('O')) > 1:
#     print('Impossible')
# elif ('XXX' not in winner and 'OOO' not in winner) and '_' not in i:
#     print('Draw')
# elif ('XXX' not in winner and 'OOO' not in winner) and '_' in i:
#     print('Game not finished')
# else:
#     if 'XXX' in winner:
#         print('X wins')
#     else:
#         print('O wins')

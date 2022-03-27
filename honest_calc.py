# list of possible messages
msg = ["Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"
       ]

# list of possible operators
ops = ["+", "-", "*", "/"]

# calculator memory
memory = 0


def is_one_digit(v):
    if v == int(v):
        v = int(v)
        return (10 > v > -10) and (len(str(v)) == 1)
    else:
        return False


def check(v1, v2, v3):
    mesg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        mesg += msg[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        mesg += msg[7]
    if (v1 == 0 or v2 == 0) and (v3 in ["*", "+", "-"]):
        mesg += msg[8]
    if mesg != "":
        mesg = msg[9] + mesg
        print(mesg)


def calculate(first, second, op):
    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return float(first * second)
    elif op == "/":
        if second == 0:
            return "zero_div"
        else:
            return first / second


def save_memory(res):
    global memory
    if is_one_digit(res):
        msg_index = 10
        while True:
            print(msg[msg_index])
            answer = input()
            if answer == "y" or answer == "Y":
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    memory = res
                    break
            else:
                if answer == "n" or answer == "N":
                    break
                else:
                    continue
    else:
        memory = res


while True:
    print(msg[0])
    calc = input("").split()

    # sprawdzamy x
    if calc[0] == "M":
        x = memory
    else:
        try:
            x = int(calc[0])
        except ValueError:
            try:
                x = float(calc[0])
            except ValueError:
                print(msg[1])
                continue

    # sprawdzamy y
    if calc[2] == "M":
        y = memory
    else:
        try:
            y = int(calc[2])
        except ValueError:
            try:
                y = float(calc[2])
            except ValueError:
                print(msg[1])
                continue

    oper = calc[1]
    if oper in ops:
        check(x, y, oper)
        result = calculate(x, y, oper)
        if result != "zero_div":
            print(result)
            while True:
                print(msg[4])
                answer = input()
                if answer == "y" or answer == "Y":
                    # TODO: tu spróbujemy wpisać funkcję 'save_memory()'
                    save_memory(result)
                    break
                else:
                    if answer == "n" or answer == "N":
                        break
                    else:
                        continue
            while True:
                print(msg[5])
                answer = input()
                if answer == "y" or answer == "Y":
                    break
                elif answer == "n" or answer == "N":
                    exit(0)
                else:
                    continue
            continue
        else:
            print(msg[3])
            continue
    else:
        print(msg[2])
        continue


# # write your code here
# msg_0 = "Enter an equation"
#
# msg_1 = "Do you even know what numbers are? Stay focused!"
#
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
#
# # finish = False
#
# while True:
#     print(msg_0)
#     calc = input("").split()
#     try:
#         x = float(calc[0])
#         y = float(calc[2])
#     except ValueError:
#         print(msg_1)
#         continue
#     oper = calc[1]
#     if oper == "+" or oper == "-" or oper == "*" or oper == "/":
#         break
#     else:
#         print(msg_2)
#         continue

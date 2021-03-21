formatters = "plain bold italic link inline-code header ordered-list unordered-list line-break"

cmd = input("- Choose a formatter: > ")

out_text = []
# out_text = ""


def out_print():
    md_text = ""
    for md_line in out_text:
        md_text += md_line
    print(md_text)


def plain():
    text = input("- Text: > ")
    out_text.append(text)
    # out_text.
    out_print()


def bold():
    text = input("- Text: > ")
    md_line = "**" + text + "**"
    out_text.append(md_line)
    out_print()


def italic():
    text = input("- Text: > ")
    md_line = "*" + text + "*"
    out_text.append(md_line)
    out_print()


def inline():
    text = input("- Text: > ")
    md_line = "`" + text + "`"
    out_text.append(md_line)
    out_print()


def link():
    label = input("- Label: > ")
    url = input("- URL: > ")
    md_line = "[" + label + "](" + url + ")"
    out_text.append(md_line)
    out_print()


def header():
    level = int(input("- Level: > "))
    while level > 6 or level < 1:
        print("The level should be within the range of 1 to 6")
        level = int("- Level: > ")
    text = input("- Text: > ")
    md_line = level * "#" + " " + text + "\n"
    out_text.append(md_line)
    out_print()


def line():
    out_text.append("\n")
    out_print()


def olist():
    n_rows = int(input("- Number of rows: > "))
    while n_rows < 1:
        print("The number of rows should be greater than zero")
        n_rows = int(input("- Number of rows: > "))
    for i in range(n_rows):
        text = input("- Row #" + str(i + 1) + ": > ")
        md_line = str(i + 1) + ". " + text + "\n"
        out_text.append(md_line)
    out_print()


def ulist():
    n_rows = int(input("- Number of rows: > "))
    while n_rows < 1:
        print("The number of rows should be greater than zero")
        n_rows = int(input("- Number of rows: > "))
    for i in range(n_rows):
        text = input("- Row #" + str(i + 1) + ": > ")
        md_line = "* " + text + "\n"
        out_text.append(md_line)
    out_print()


def newline():
    out_text.append("\n")
    out_print()


while cmd != "!done":
    if cmd == "":
        pass
    elif cmd == "plain":
        plain()
    elif cmd == "bold":
        bold()
    elif cmd == "italic":
        italic()
    elif cmd == "inline-code":
        inline()
    elif cmd == "link":
        link()
    elif cmd == "header":
        header()
    elif cmd == "line-break":
        line()
    elif cmd == "ordered-list":
        olist()
    elif cmd == "unordered-list":
        ulist()
    elif cmd == "new-line":
        newline()
    elif cmd == "!help":
        print("Available formatters:", formatters)
        print("Special commands: !help !done")
    else:
        print("Unknown formatting type or command. Please try again")

    cmd = input("- Choose a formatter: > ")

# na końcu zapisujemy wyniki
md_text = ""
for md_line in out_text:
    md_text += md_line
# print(md_text)

file = open('output.md', 'w')
file.write(md_text)
file.close()

# # write your code here
# print("# John Lennon")
# print("or ***John Winston Ono Lennon*** was one of *The Beatles*.")
# print("Here are the songs he wrote I like the most:")
# print("* Imagine")
# print("* Norwegian Wood")
# print("* Come Together")
# print("* In My Life")
# print("* ~~Hey Jude~~ (that was *McCartney*)")

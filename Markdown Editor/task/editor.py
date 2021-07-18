# write your code here
def add_plain():
    global text_body
    print("Text:", end="")
    text_ = input()
    text_body += text_


def add_bold():
    global text_body
    print("Text:", end="")
    text_ = input()
    text_ = "**{}**".format(text_)
    text_body += text_


def add_italic():
    global text_body
    print("Text:", end="")
    text_ = input()
    text_ = "*{}*".format(text_)
    text_body += text_


def add_inline():
    global text_body
    print("Text:", end="")
    text_ = input()
    text_ = "`{}`".format(text_)
    text_body += text_


def add_new_line():
    global text_body
    text_body += "\n"


def add_header():
    global text_body
    print("Level:", end="")
    while True:
        level_ = int(input())
        if level_ < 1 or level_ > 6:
            print("The level should be within the range of 1 to 6")
            continue
        break
    print("Text:", end="")
    text_ = input()
    text_ = "{} {}".format("#" * level_, text_)
    text_body += text_ + "\n"


def add_link():
    global text_body
    print("Label:", end="")
    label_ = input()
    print("URL:", end="")
    url_ = input()
    text_ = "[{}]({})".format(label_, url_)
    text_body += text_


def add_list(list_type):
    global text_body
    list_sign = "*"
    list_comma = ""
    if list_type == "o":
        list_sign = "0"
        list_comma = "."
    while True:
        print("Number of rows:", end="")
        rows_ = int(input())
        if rows_ < 1:
            print("The number of rows should be greater than zero")
            continue
        break
    for i_ in range(rows_):
        print("Row #{}:".format(i_ + 1), end="")
        row_ = input()
        if list_type == "o":
            list_sign = str(int(list_sign) + 1)
        text_ = "{}{} {}".format(list_sign, list_comma, row_)
        text_body += text_ + "\n"


def save_body():
    global text_body
    with open("output.md", "w") as file_:
        file_.write(text_body)


formatters = ["plain", "bold", "italic", "header", "link",
              "inline-code", "ordered-list", "unordered-list", "new-line"]
commands = ["!help", "!done"]
text_body = ""
while True:
    print("Choose a formatter:", end="")
    option = input()
    if option not in formatters and option not in commands:
        print("Unknown formatting type or command")
        continue
    if option == "!done":
        save_body()
        break
    if option == "!help":
        print("Available formatters:", " ".join(formatters))
        print("Special commands:", " ".join(commands))
    if option == "plain":
        add_plain()
    if option == "bold":
        add_bold()
    if option == "italic":
        add_italic()
    if option == "header":
        add_header()
    if option == "link":
        add_link()
    if option == "inline-code":
        add_inline()
    if option == "new-line":
        add_new_line()
    if option == "ordered-list" or option == "unordered-list":
        add_list(option[0])

    print(text_body)

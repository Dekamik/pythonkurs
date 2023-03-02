def hello_world():
    print("Hello, World!")


def hello_world_single_quotes():
    print('Hello, World!')


def hello_input():
    subject = input()
    print("Hello, " + subject)


def format_hello():
    subject = input()
    print(f"Hello, {subject}")


def substring():
    text = "Hello, World!"
    print(text[2:5])


def contains():
    name = "Dennis"
    substring = "r"
    if substring in name:
        print(f"It contains {substring}! :D")
    else:
        print(f"It doesn't contain {substring} :(")


if __name__ == "__main__":
    contains()

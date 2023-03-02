def hello_world():
    print("Hello, World!")


def hello_world_single_quotes():
    print('Hello, World!')


def hello_input():
    name = input("Name: ")
    print("Hello, " + name)


def format_hello():
    name = input("Name: ")
    print(f"Hello, {name}")


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


def str_methods():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    print(list)

    list_as_str = ", ".join(list)
    print(list_as_str)

    list_lower = [name.lower() for name in list]
    print(list_lower)

    list_upper = [name.upper() for name in list]
    print(list_upper)

    list_capitalized = [name.capitalize() for name in list_lower]
    print(list_capitalized)


if __name__ == "__main__":
    hello_world()
    # hello_world_single_quotes()
    # hello_input()
    # format_hello()
    # substring()
    # contains()
    # str_methods()

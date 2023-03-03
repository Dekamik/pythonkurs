def if_else_elif():
    if True:
        return 1
    elif False:
        return -1
    else:
        return 0


def tertiary():
    return 1 if True else -1 if False else 0


def logical_operators():
    print("--- or ---")
    print(False or False)
    print(True or False)
    print(False or True)
    print(True or True)

    print("\n--- and ---")
    print(False and False)
    print(True and False)
    print(False and True)
    print(True and True)

    print("\n--- not ---")
    print(not True)
    print(not False)


def match(command):
    match command:
        case "read":
            print("read selected")

        case "write":
            print("write selected")

        case _:
            print("unknown command")


def scope():
    if True:
        text = "Hello"
    else:
        text = "Good-bye"

    print(text)


if __name__ == "__main__":
    logical_operators()
    # scope()

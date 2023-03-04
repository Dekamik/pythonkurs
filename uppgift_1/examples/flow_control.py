from enum import Enum


def if_else_elif():
    if True:
        return 1
    elif False:
        return -1
    else:
        return 0


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


def is_vs_equals():
    """
    == is for value equality. Use it when you want to know if two objects have the same value.
    is is for reference equality. Use it when you want to know if two references refer to the same object in memory.
    """

    class Fruit(Enum):
        APPLES = 1
        ORANGES = 2

    appl = Fruit.APPLES
    print(appl is Fruit.APPLES)
    print(Fruit.APPLES is Fruit.ORANGES)

    nobody = None
    print(nobody is None)
    print(nobody is not None)

    def fun_fun_function():
        pass

    func = fun_fun_function
    print(func is fun_fun_function)


def while_loop():
    i = 0
    while i < 10:
        print(i)
        i += 1


def for_in_range():
    for i in range(10):
        print(i)


def for_in_list():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    for name in list:
        print(name)


def loop_continue():
    list = ["Adam", "Bertil", "Albert", "Caesar", "David", "Erik", "Filip"]
    for name in list:
        if name == "Albert":
            print("Du hör inte hemma här")
            continue
        print(name)


def loop_break():
    list = ["Adam", "Bertil", "Albert", "Caesar", "David", "Erik", "Filip"]
    for name in list:
        if name == "Albert":
            break
        print(name)


def tertiary():
    return 1 if True else -1 if False else 0


def match(command):
    match command:
        case "read":
            print("read selected")

        case "write":
            print("write selected")

        case _:
            print("unknown command")


if __name__ == "__main__":
    logical_operators()
    # is_vs_equals()
    # while_loop()
    # for_in_range()
    # for_in_list()
    # loop_continue()
    # loop_break()

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


def list_comprehension():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    [print(name) for name in list]


def list_comprehension_2():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    new_list = [name for name in list if "a" in name]
    print(new_list)


if __name__ == "__main__":
    # while_loop()
    # for_in_range()
    # for_in_list()
    # list_comprehension()
    list_comprehension_2()

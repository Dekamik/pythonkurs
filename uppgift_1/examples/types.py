def primitives():
    i = 1
    f = 1.0
    s = "Hello"
    b = True


def non_primitive():
    list = [1, 2, 3, 4]
    dict = {"one": 1, "two": 2, "three": 3, "four": 4}
    tuple = (1, 2, 3, 4)
    s = set("one", "two", "three", "four")


def type_hint(path: int) -> str:
    if path == 1:
        return "one"
    elif path == 2:
        return 2
    return False


if __name__ == "__main__":
    print(type_hint(2))

from datetime import date


def primitives():
    n = None
    i = 1
    f = 1.0
    s = "Hello"
    b = True

    print(type(n))
    print(type(i))
    print(type(f))
    print(type(s))
    print(type(b))


def non_primitives():
    l = [1, 2, 3, 4]
    d = {"one": 1, "two": 2, "three": 3, "four": 4}
    t = (1, 2, 3, 4)
    s = set(["one", "two", "three", "four"])

    print(type(l))
    print(type(d))
    print(type(t))
    print(type(s))


def implicit_conversion():
    i = 1
    f = 1.0
    print(i == f)


def explicit_conversion():
    i = 1
    print(type(i))

    i = "1"
    print(type(i))


def type_hint(path: int) -> str:
    if path == 1:
        return "one"
    elif path == 2:
        return 2
    return False


def casting():
    age_raw = input("How old will you be this year? ")
    print(f"{age_raw} {type(age_raw)}")

    age = int(age_raw)
    print(f"{age} {type(age)}")

    birth_year = date.today().year - age
    print(f"You were born in {birth_year}")


if __name__ == "__main__":
    primitives()
    # non_primitives()
    # implicit_conversion()
    # explicit_conversion()
    # casting()
    # ret = type_hint(3)
    # print(type(ret))

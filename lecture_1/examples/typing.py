from datetime import date


def primitives():
    i = 1
    f = 1.0
    s1 = "Hello"
    s2 = 'Hello'
    b = True

    print(type(i))
    print(type(f))
    print(type(s1))
    print(type(b))


def int_literals():
    decimal = 42
    hexadecimal = 0x2A
    octal = 0o52
    binary = 0b0010_1010

    # fdjsaphgeruiagh
    """
    fdasffdsjfods
    """
    s1 = "42 = " + str(decimal)
    s2 = f"42 = {decimal}"

    print(f"{int(decimal)} = {decimal}")
    print(f"{hex(hexadecimal)} = {hexadecimal}")
    print(f"{oct(octal)} = {octal}")
    print(f"{bin(binary)} = {binary}")


def non_primitives():
    my_list = [1, 2, 3, 4]
    my_tuple = (1, 2, 3, 4)
    my_dict = {
        "one": 1,
        "two": 2, 
        "three": 3, 
        "four": 4
    }
    my_set = set(["one", "one", "two", "three", "three", "three", "four"])

    print(type(my_list))
    print(type(my_tuple))
    print(type(my_dict))
    print(type(my_set))

    print(f"my_list[0] = {my_list[0]}")
    print(f"my_tuple[0] = {my_tuple[0]}")
    print(f"my_dict['one'] = {my_dict['one']}")
    print(f"'one' in my_set = {'one' in my_set}")


def list_as_stack():
    stack = [1, 2, 3, 4]
    print(stack)

    stack.append(5)
    print(f"Pushed 5 to the stack")
    print(stack)

    five = stack.pop()
    print(f"Popped {five} from the stack")
    print(stack)


def list_as_queue():
    queue = [1, 2, 3, 4]
    print(queue)

    queue.insert(0, 0)
    print(f"Inserted 0 into the queue")
    print(queue)

    next = queue.pop()
    print(f"Popped {next} from the queue")
    print(queue)


def implicit_conversion():
    x = 1
    y = 0.555555555555555555555555555555555555555555555555555555555555555555
    z = x + int(y)
    print(f"i = {x} ({type(x)})\nf = {y} ({type(y)})\nz = {z} ({type(z)})")


def explicit_conversion():
    i = 1
    print(type(i))

    i = "1"
    print(type(i))


def type_hint(path: int) -> list[dict] | dict | None:
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
    # primitives()
    # int_literals()
    # non_primitives()
    # list_as_stack()
    # list_as_queue()
    # implicit_conversion()
    # explicit_conversion()
    # casting()
    ret = type_hint("grjaeoighier")
    print(f"{ret} {type(ret)}")

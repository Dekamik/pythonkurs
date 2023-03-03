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


def int_literals():
    decimal = 42
    hexadecimal = 0x2A
    octal = 0o52
    binary = 0b0010_1010

    print(f"{int(decimal)} = {decimal}")
    print(f"{hex(hexadecimal)} = {hexadecimal}")
    print(f"{oct(octal)} = {octal}")
    print(f"{bin(binary)} = {binary}")


def non_primitives():
    my_list = [1, 2, 3, 4, 5]
    my_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
    my_tuple = (1, 2, 3, 4)
    my_set = set(["one", "two", "three", "four"])

    print(type(my_list))
    print(type(my_dict))
    print(type(my_tuple))
    print(type(my_set))

    print(my_list[0])  # get at index 0 (first one)

    # Slicing = [start:end]
    # get all from index 1, to index 3 (index 3 not included)
    print(my_list[1:3])
    print(my_list[:2])  # get the first two items
    print(my_list[2:])  # index 2 to end
    print(my_list[:-2])  # from beginning until index -2 (len(my_list) - 2 = 2)
    print(my_list[-2:])  # index -2 to end
    # Works with tuples and strings aswell

    print(my_dict["one"])
    print(my_tuple[0])
    print("one" in my_set)


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
    # int_literals()
    # non_primitives()
    # list_as_stack()
    # list_as_queue()
    # implicit_conversion()
    # explicit_conversion()
    # casting()
    # ret = type_hint(3)
    # print(type(ret))

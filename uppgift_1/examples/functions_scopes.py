def normal_function():
    print("Hi")


def xhibit():
    def function_in_function():
        print("So you can function, while you function")

    function_in_function()


def local_scope():
    if True:
        text = "Hello"
    else:
        text = "Good-bye"

    print(text)


global_variable = "Hello"


def print_global_variable():
    print(global_variable)


def declaring_global_variable_inside_local_scope():
    """
    This must be called before calling print_b
    """
    global b
    b = 10


def print_b():
    print(b)


if __name__ == "__main__":
    # normal_function()
    # xhibit()
    # local_scope()
    # print_global_variable()
    # declaring_global_variable_inside_local_scope()
    # print_b()

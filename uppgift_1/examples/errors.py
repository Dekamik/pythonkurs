

class MyError(Exception):
    """Thrown at my own lesiure"""


def raise_exception():
    raise MyError("No")


def handle_raised_exception():
    try:
        raise MyError("Take that!")
    except MyError:
        print("I don't think so!")


def do_finally():
    try:
        raise MyError("Take that!")
    except MyError:
        print("Gotcha!")
    finally:
        print("Good catch!")

    try:
        raise MyError("Take that!")
    finally:
        print("I am done for!")


def else_in_try_except():
    try:
        pass
    except MyError:
        print("Catched!")
    else:
        print("No error was raised")
    finally:
        print("We're done here")


if __name__ == "__main__":
    raise_exception()
    # handle_raised_exception()
    # do_finally()
    # else_in_try_except()

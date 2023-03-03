class MyError(Exception):
    """Thrown at my own lesiure"""


class MyValueError(ValueError):
    """See above"""


def raise_exception():
    raise MyError("No")


def handle_raised_exception():
    try:
        raise MyError("Take that!")
    except MyError:
        print("Denied!")


def do_finally():
    try:
        raise MyError("Take that!")
    except MyError as e:
        print(f"Gotcha! This one said: {e}")
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


def error_inheritance():
    try:
        raise MyValueError("Wrong!")
    except ValueError as e:
        print(f"We capture value errors. This one said: {e}")


def multiple_error_types():
    try:
        raise MyValueError("Foiled again!")
    except (MyError, MyValueError) as e:
        print(e)
    except Exception as e:
        print(f"unhandled exception: {e}")


def pass_exception():
    try:
        raise MyError()
    except MyError as e:
        print("This error was found, I'm gonna do something and then pass it on")
        raise e


if __name__ == "__main__":
    raise_exception()
    # handle_raised_exception()
    # do_finally()
    # else_in_try_except()
    # error_inheritance()
    # multiple_error_types()

import sys


def exc_hook(exc_type, exc_value, exc_traceback):
    print("An error occurred")


sys.excepthook = exc_hook


def main():
    raise Exception("Uncaught error")


if __name__ == "__main__":
    main()

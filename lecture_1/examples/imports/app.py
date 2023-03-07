from lib_dir.lib_b import LibClass
from lib_a import print_banana, loose_var


def main():
    print(loose_var)
    print_banana()

    class_ = LibClass()


if __name__ == "__main__":
    main()

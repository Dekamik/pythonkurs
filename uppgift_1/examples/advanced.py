import random
import sys


def list_comprehension():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    [print(name) for name in list]


def list_comprehension_with_conditional():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    new_list = [name for name in list if "a" in name]
    print(new_list)


def generators():
    def generator_function():
        for i in range(10):
            yield i

    list_ = list(generator_function())
    print(list_)

    numbers = [num + 1 for num in generator_function()]
    print(numbers)

    gen = generator_function()
    print(next(gen))
    print(next(gen))
    print(next(gen))

    generator_expression = (i for i in range(10))
    print(list(generator_expression))

    even_gen = (i for i in range(10) if i % 2 == 0)
    print(list(even_gen))


def generator_efficiency():
    """
    Generators are efficient due to lower memory usage and the fact that 
    we don't need to wait until all elements have been generated before 
    we start iterating.

    If however the list is smaller than the running machine's available 
    memory, then list comprehensions can be faster to evaluate than the
    equivalent generator expression.

    If speed is an issue and memory isn't, then a list comprehension is
    likely a better tool for the job.
    """
    nums_squared_lc = [i ** 2 for i in range(10000)]
    print(sys.getsizeof(nums_squared_lc))

    nums_squared_gc = (i ** 2 for i in range(10000))
    print(sys.getsizeof(nums_squared_gc))


def slicing():
    my_list = [i for i in range(6)]
    print(my_list)

    # Slicing create sub-arrays using this notation: [start:end]
    print(my_list[1:3])  # get all from index 1, to index 3 (index 3 excluded)
    print(my_list[:2])  # get the first two items
    print(my_list[2:])  # index 2 to end
    print(my_list[:-2])  # from beginning until index -2 (len(my_list) - 2 = 4)
    print(my_list[-2:])  # index -2 to end
    print(my_list[1:-2])  # from index 1 to index -2
    print(my_list[-2:-1])  # from index -2 to index -1 (next to last)
    # Works with tuples and strings aswell


def all_any():
    data = [
        [
            {
                "name": "Sven",
                "role": "teacher"
            },
            {
                "name": "Anders",
                "role": "teacher"
            }
        ],
        [
            {
                "name": "Sven",
                "role": "teacher"
            },
            {
                "name": "Jonas",
                "role": "pupil"
            }
        ]
    ]

    for list in data:
        if all([person["role"] == "teacher" for person in list]):
            print("all: Contains only teachers")
        else:
            print("all: Other than teachers found")

    for list in data:
        if any([person["role"] == "pupil" for person in list]):
            print("all: Contains pupils")
        else:
            print("all: Contains no pupils")


def min_max_sum():
    numbers = [random.randint(0, 100) for _ in range(20)]
    print(numbers)

    print(f"Smallest number is {min(numbers)}")
    print(f"Largest number is {max(numbers)}")
    print(f"Sum of all numbers is {sum(numbers)}")


if __name__ == "__main__":
    list_comprehension()
    # list_comprehension_with_conditional()
    # generators()
    # generator_efficiency()
    # slicing()
    # all_any()
    # min_max_sum()

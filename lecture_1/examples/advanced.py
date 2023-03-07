import random
import sys


def comprehension():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]
    [print(name) for name in list]


def list_comprehension_with_conditional():
    list = ["Adam", "Bertil", "Caesar", "David", "Erik", "Filip"]

    loop_list = []
    for name in list:
        if "a" in name:
            loop_list.append(name)
    print(loop_list)

    comp_list = [name for name in list if "a" in name]
    comp_list.sort(reverse=True)
    print(comp_list)


def dict_comprehension():
    län = ["Stockholms Län", "Västra Götalands Län", "Skåne Län"]
    residensstäder = ["Stockholm", "Göteborg", "Malmö"]

    loop_dict = {}
    for (key, value) in zip(län, residensstäder):
        loop_dict[key] = value
    print(loop_dict)

    comp_dict = {key: value for (key, value) in zip(län, residensstäder) if "stockholm" not in key.lower()}
    print(comp_dict)


def set_comprehension():
    names = ["Adam", "Bertil", "Caesar", "David",
             "David", "Erik", "Erik", "Erik"]

    unique_names = {name.lower(): name.upper() for name in names}
    print(unique_names)


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

    generator_comprehension = (i for i in range(10))
    print(list(generator_comprehension))

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

    amount_1 = "49.99 kr"
    amount_2 = "299.99 kr"

    num_1 = float(amount_1[:-3])
    num_2 = float(amount_2[:-3])

    sum = num_1 + num_2


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

    for list_ in data:
        if all([person["role"] == "teacher" for person in list_]):
            print(f"Contains only teachers: {list_}")
        else:
            print(f"Other than teachers found: {list_}")

    for list_ in data:
        if any([person["role"] == "pupil" for person in list_]):
            print(f"Does contains pupils: {list_}")
        else:
            print(f"Does not contain pupils: {list_}")


def min_max_sum():
    numbers = [random.randint(0, 100) for _ in range(20)]
    print(numbers)

    print(f"Smallest number is {min(numbers)}")
    print(f"Largest number is {max(numbers)}")
    print(f"Sum of all numbers is {sum(numbers)}")


def unpacking_args(*args):
    print(args)


def unpacking_kvargs(**kvargs):
    print(kvargs)


def unpacking_both(*args, **kvargs):
    print(args)
    print(kvargs)


def unpacking_into_collections(list_or_tuple: list | tuple, dict_: dict):
    new_list = [
        0,
        *list_or_tuple
    ]
    new_dict = {
        "c": 3,
        **dict_
    }
    print(new_list)
    print(new_dict)

    unpacking_both(*list_or_tuple, **dict_)


if __name__ == "__main__":
    # comprehension()
    # list_comprehension_with_conditional()
    # dict_comprehension()
    # set_comprehension()
    # generators()
    # generator_efficiency()
    # slicing()
    # all_any()
    min_max_sum()
    # unpacking_args("a", "b", "c")
    # unpacking_kvargs(one="a", two="b", three="c")
    # unpacking_both("a", "b", three="c", four="d")
    # unpacking_into_collections([1, 2, 3, 4], {"a": 1, "b": 2})

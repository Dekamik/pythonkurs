import random


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
    all_any()
    # min_max_sum()

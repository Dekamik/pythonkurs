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


if __name__ == "__main__":
    all_any()

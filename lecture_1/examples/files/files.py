import csv
import json
import os


def read_old():
    f = None  # Inte helt nödvändig
    try:
        f = open("lecture_1/examples/files/test.csv")
        content = f.readlines()
        print(content)
    finally:
        if f is not None:
            f.close()


def read_new():
    with open("lecture_1/examples/files/test.csv", "r") as f:
        content = f.readlines()
        print(content)


def write_file():
    with open("lecture_1/examples/files/hello.txt", "w") as f:
        f.write("Hello!")


def read_csv():
    with open("lecture_1/examples/files/test.csv") as f:
        r = csv.reader(f, delimiter=",")
        for row in r:
            print(", ".join(row))


def read_csv_as_dict():
    with open("lecture_1/examples/files/test.csv") as f:
        r = csv.DictReader(f)
        for row in r:
            print(row)


def write_csv():
    data = {
        "pets": [
            {
                "name": "Gizmo",
                "type": "Cat"
            },
            {
                "name": "Gandalf",
                "type": "Cat"
            }
        ]
    }

    with open("lecture_1/examples/files/pets.csv", "w", newline="") as f:
        r = csv.writer(f, delimiter=",")

        r.writerow(["name", "type"])
        for pet in data["pets"]:
            r.writerow([pet["name"], pet["type"]])


def write_csv_from_dict():
    data = {
        "pets": [
            {
                "name": "Gizmo",
                "type": "Cat"
            },
            {
                "name": "Gandalf",
                "type": "Cat"
            }
        ]
    }

    with open("lecture_1/examples/files/pets.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "type"])
        w.writeheader()
        for pet in data["pets"]:
            w.writerow(pet)


def write_json():
    data = {
        "pets": [
            {
                "name": "Gizmo",
                "type": "Cat"
            },
            {
                "name": "Gandalf",
                "type": "Cat"
            }
        ]
    }

    with open("lecture_1/examples/files/pets.json", "w") as f:
        content = json.dumps(data)
        f.write(content)


def read_json():
    with open("lecture_1/examples/files/pets.json") as f:
        data = json.loads(f.read())
        print(data)
        print(type(data))


if __name__ == "__main__":
    # print(os.listdir())
    # read_old()
    # read_new()
    # write_file()
    # read_csv()
    # read_csv_as_dict()
    # write_csv()
    write_csv_from_dict()
    # write_json()
    # read_json()

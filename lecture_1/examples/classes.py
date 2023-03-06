from dataclasses import dataclass
from datetime import date
from enum import Enum


class Department(Enum):
    C_SUITE = 1
    ADMIN = 2
    IT = 3


@dataclass
class Person:
    name: str
    birthdate: date


class Employee(Person):
    def __init__(self, name: str, birthdate: date, stamina: float, department: Department):
        super().__init__(name, birthdate)
        self.stamina = stamina
        self.department = department

    def work(self, hours: float):
        self.stamina -= hours

    def rest(self, hours: float):
        self.stamina += hours / 3.2

    def __str__(self) -> str:
        return f"{self.name} at {self.department}, born {self.birthdate.isoformat()}, stamina: {self.stamina}"


def employee_example():
    employee = Employee("Jens",
                        date.fromisoformat("1981-06-07"),
                        15,
                        Department.IT)
    print(employee)

    for i in range(5):
        employee.work(8)
        employee.rest(16)
        print(f"stamina after day {i + 1}: {employee.stamina}")

    [employee.rest(24) for _ in range(2)]

    print(f"stamina after 2 days rest: {employee.stamina}")


class AccessibilityConventions:
    def normal_accessible_method(self):
        """Is visible like usual"""
        print("Call me anytime ;)")

    def _do_not_import(self):
        """Internal use: does not import in statements like 'from AccessibilityConventions import *'"""
        pass

    def class_(self):
        """Avoids clashing with Python keywords"""
        pass

    def let_me_do_it_for_you(self):
        """Has full ability to call __very_private_method"""
        print("Let me do it for you")
        self.__very_private_method()

    def __very_private_method(self):
        """
        Mangles the name to _AccessibilityConventions__very_private_method, 
        mainly to avoid naming conflicts between the current class and its subclasses
        """
        print("Hey, stop it!")

    def __str__(self):
        """leading and trailing double underscores are reserved for magic names"""
        for _ in range(10):
            """Shows that I don't care about the range variable"""
            pass


def accessibility_example():
    [print(member) for member in dir(AccessibilityConventions)]

    class_ = AccessibilityConventions()
    class_.normal_accessible_method()
    class_.let_me_do_it_for_you()

    try:
        class_.__very_private_method()
    except AttributeError as e:
        print(e)

    class_._AccessibilityConventions__very_private_method()


if __name__ == "__main__":
    employee_example()
    # accessibility_example()

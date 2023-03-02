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
        return f"{self.name} at {self.department}"


if __name__ == "__main__":
    employee = Employee("Jens", "1981-06-07", 15, Department.IT)
    print(employee)

    for i in range(5):
        employee.work(8)
        employee.rest(16)
        print(f"stamina after day {i + 1}: {employee.stamina}")

    [employee.rest(24) for _ in range(2)]

    print(f"stamina after 2 days rest: {employee.stamina}")

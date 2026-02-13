
# Завдання 1

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(
        self,
        name: str,
        salary: float,
        department: str,
        programming_language: str,
        team_size: int
    ):
        # Явно ініціалізуємо базові частини з обох гілок наслідування
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language

        if team_size < 0:
            raise ValueError("team_size не може бути від'ємним")
        self.team_size = team_size


# ---- Тест (простий, без бібліотек) ----
def test_teamlead_has_manager_and_developer_attrs():
    tl = TeamLead(
        name="Олег",
        salary=5000,
        department="R&D",
        programming_language="Python",
        team_size=7
    )

    assert hasattr(tl, "name")
    assert hasattr(tl, "salary")
    assert hasattr(tl, "department")              # з Manager
    assert hasattr(tl, "programming_language")    # з Developer
    assert hasattr(tl, "team_size")               # власний

    # Додатково: перевірка значень
    assert tl.department == "R&D"
    assert tl.programming_language == "Python"
    assert tl.team_size == 7

    print("✅ Test passed: TeamLead має атрибути Manager та Developer")


# Запуск тесту
test_teamlead_has_manager_and_developer_attrs()



# Завдання 2

from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Figure):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("side має бути > 0")
        self.__side = side  # приватна

    def area(self) -> float:
        return self.__side ** 2

    def perimeter(self) -> float:
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("width і height мають бути > 0")
        self.__width = width
        self.__height = height  # приватні

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("radius має бути > 0")
        self.__radius = radius  # приватна

    def area(self) -> float:
        return math.pi * (self.__radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius


class Triangle(Figure):
    """
    Трикутник за трьома сторонами.
    Площа: формула Герона.
    """
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Сторони мають бути > 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Неможливо створити трикутник з такими сторонами")
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c


# ---- Створення об'єктів та цикл ----
figures = [
    Square(5),
    Rectangle(4, 6),
    Circle(3),
    Triangle(3, 4, 5),
]

for fig in figures:
    print(f"{fig.__class__.__name__}: площа = {fig.area():.2f}, периметр = {fig.perimeter():.2f}")
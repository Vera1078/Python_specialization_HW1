# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from pathlib import Path


class TestName:
    """Проверка правильности ввода ФИО."""

    def __set_name__(self, owner, name):
        self.param_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value: str):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Неверные данные для ФИО!")
        instance.__dict__[self.param_name] = value


class TestRate:
    """Класс-дескриптор для проверки выставленных оценок."""

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = name

    def __set__(self, instance, value):
        self._validate(value)
        instance.__dict__[self.param_name] = value


    def __get__(self, instance, owner):
        return instance.__dict__[self.param_name]

    def _validate(self, value):
        if not isinstance(value, int):
            raise TypeError("Неверный тип для оценки!")
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{value} вне диапазона [{self.min_value}, {self.max_value}]")


# диапазон оценок по предметам
_MIN_RATE = 2
_MAX_RATE = 5

# диапазон оценок по тестам
_MIN_TEST = 0
_MAX_TEST = 100


class Discipline:
    """Класс дисциплина."""
    rate_value = TestRate(_MIN_RATE, _MAX_RATE)
    test_value = TestRate(_MIN_TEST, _MAX_TEST)
    name = TestName()

    def __init__(self, name: str, rate_value: int, test_value: int):
        self.name = name
        self.rate_value = rate_value
        self.test_value = test_value

    def __str__(self):
        return f'{self.name} - {self.rate_value}, {self.test_value}'

    def __repr__(self):
        return f'Discipline({self.name}, {self.rate_value}, {self.test_value})'

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


_DISCIPLINES = ["Математика",
                "Физика",
                "Химия",
                "История",
                "Литература",
                ]


class Student:
    """Класс студент."""
    family = TestName()
    name = TestName()
    second_name = TestName()

    def __init__(self, family: str, name: str, second_name: str):
        self.family = family
        self.name = name
        self.second_name = second_name
        self._progress = []
        self._load_progress()

    @property
    def progress(self):
        return self._progress

    @property
    def short_name(self):
        return f"{self.family} {self.name[0]}.{self.second_name[0]}."

    def __str__(self):
        return f'{self.family} {self.name} {self.second_name}'

    def _load_progress(self):
        file_name = self.short_name + 'csv'
        if Path(file_name).exists():
            with open(file_name, "r", encoding="UTF-8") as file:
                csv_reader = csv.reader(file, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
                for row in csv_reader:
                    new_discipline = Discipline(row[0], int(row[1]), int(row[2]))
                    self.append_to_progress(new_discipline)

    def show_progress(self):
        result = "     Предмет    | оценка | тест \n"
        for discipline in self._progress:
            result += f"{discipline.name:16}|{discipline.rate_value:7} |{discipline.test_value:5}\n"
        return result

    def find_discipline_in_progress(self, discipline: Discipline) -> bool:
        result = False
        for disc in self._progress:
            if discipline == disc:
                result = True
                break
        return result

    def append_to_progress(self, discipline: Discipline):
        if discipline.name in _DISCIPLINES and not self.find_discipline_in_progress(discipline):
            self._progress.append(discipline)
        else:
            raise ValueError(f"{discipline.name} - недопустимая дисциплина, или уже есть в списке!")


if __name__ == '__main__':
    student_1 = Student('Иванов', 'Иван', 'Иванович')
    student_2 = Student('Петров', 'Петр', 'Петрович')

    print(student_1)
    print(student_2)

    student_1.append_to_progress(Discipline('Математика', 2, 20))
    student_1.append_to_progress(Discipline('Физика', 5, 50))
    student_1.append_to_progress(Discipline('Химия', 3, 30))

    print(student_1.short_name)
    print(student_1.show_progress())

    # student_2.append_to_progress(Discipline('Химия', 4, 30))
    # student_2.append_to_progress(Discipline('Биология', 3, 30))
    #
    # print(student_2.short_name)
    # print(student_2.show_progress())

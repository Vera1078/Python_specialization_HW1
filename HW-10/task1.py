# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:
    def __init__(self, name):
        self.name = name

    def get_special_info(self):
        return f'Дополнительной информации пока нет'

class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        # self.name = name
        self.depth = depth

    def get_special_info(self):
        return f'Рыба {self.name}: глубина обитения {self.depth} м'


class Bird(Animals):
    def __init__(self, name, wings):
        # self.name = name
        super().__init__(name)
        self.wings = wings

    def get_special_info(self):
        return f'Птица {self.name}: размах крыльев {self.wings} см'


class Mammal(Animals):
    def __init__(self, name, coat):
        # self.name = name
        super().__init__(name)
        self.coat = coat

    def get_special_info(self):
        return f'Млекопитающее {self.name}: длина шерсти {self.coat} см'

class Farm:
    def get_animal(self, type_animal, name, special_info):
        types_animals = {
            'Fish': Fish,
            'Bird': Bird,
            'Mammal': Mammal
        }
        if type_animal in types_animals:
            return types_animals[type_animal](name, special_info)
        else:
            print(f'Животного {type_animal} нет, но можно создать')
            return Animals(name)

farm = Farm()
animal_x = farm.get_animal('Bird', 'Пташка', 10)
print(animal_x.get_special_info())
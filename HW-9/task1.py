# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import json
from random import randint
import csv
import math

def discr_in_csv_decor(func):
    dict_file = {}
    def wrapper(file_name, *args, **kwargs):
        with open(file_name + '.csv', 'r', newline='', encoding='utf-8') as f:
            file_csv = csv.reader(f, delimiter=',')
            for row in file_csv:
                result = func(int(row[0]), int(row[1]), int(row[2]))
                rows = f'a = {row[0]}, b = {row[1]}, c = {row[2]}'
                dict_file[str(rows)] = str(result)
        return dict_file
    return wrapper

# Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл
def write_in_json(func):
    def wrapper(file_name, file_name_csv_file, *args, **kwargs):
        with open(file_name + '.json', 'w', encoding='utf=8') as file_json:
            json.dump(func(file_name_csv_file), file_json, indent=4, separators=(',', ':'), ensure_ascii=False)
        print('Запись корней дискриминанта в файл JSON прошла успешно')
    return wrapper


# Запись CSV file с тремя случайными числами в каждой строке
def csv_write(name_csv_file: str, count_rows: int):
    with open(name_csv_file + '.csv', 'w', newline='', encoding='utf-8') as f:
        file_csv = csv.writer(f)
        for _ in range(1, count_rows + 1):
            k = []
            for _ in range(1, 4):
                k.append(randint(1, 9))
            file_csv.writerow(k)
    print(f'Запись значений в формат CSV прошла успешно')

# Чтение CSV file
def csv_read(name_csv_file):
    with open(name_csv_file + '.csv', 'r', newline='', encoding='utf-8') as f:
        file_csv = csv.reader(f, delimiter=',')
        for i in file_csv:
            print(i)



# Декоратор поиска корней из значений файла CSV
# Декоратор записи в файл JSON
@write_in_json
@discr_in_csv_decor
# функция поиска корней
def roots_discr(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return f'Корни уравнения: x1 = {round(x1, 1)}, x2 = {round(x2, 1)}'

    elif discr == 0:
        x = -b / (2 * a)
        return f'Корень уравнения: x = {round(x, 2)}'
    else:
        return "Корней нет"


csv_write('file_random_number', 100)
roots_discr('json_file_roots_discr', 'file_random_number')
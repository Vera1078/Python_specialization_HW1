# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
# Взяла задачу : # Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# # Распечатайте его как pickle строку (ДЗ 8, задача 2).
import csv
import pickle


class ReadAsCsv:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        with open(self.csv_file, 'r', newline='', encoding='utf-8') as f1:
            csv_read = list(csv.reader(f1))
            headers = csv_read.pop(0)
            lst = []
            for row in csv_read:
                dct = {}
                for i, cell in enumerate(row):
                    dct[headers[i]] = cell
                lst.append(dct)
            pickle_res = pickle.dumps(lst)
            print(pickle_res)


read = ReadAsCsv('file.csv')
read.read_csv()

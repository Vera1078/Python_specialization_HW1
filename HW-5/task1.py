# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файimport Path


from os.path import dirname, splitext, basename

def path_to_tuple(my_path):
    return dirname(my_path), splitext(basename(my_path))[0], splitext(my_path)[1][1:]


absolute_path = r"C:\Users\lipp2\PycharmProjects\Python_specialization_HW1\sem5\task6.py"
print(path_to_tuple(absolute_path))

# не понимаю, почему в выводе как разделитель появляется ДВОЙНОЙ  слэш. избавиться от лишних слэшей не смогла





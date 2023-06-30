# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def reverse_key(**kwargs):
    temp = {}
    for key, value in kwargs.items():
        if not isinstance(value, str):
            value = str(value)
        temp[value] = key
    return temp


print(reverse_key(asd=[150, 500, -200], abc=[150, 500, -200], cab=[850, 500, -200]))
# Создайте функцию генератор чисел Фибоначчи
# (см. Википедию)


def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(8):
    print(num)

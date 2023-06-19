# Выведите в консоль таблицу умножения от 2х2 до 9х10, как на школьной тетрадке.

print(' ' * 20 + 'ТАБЛИЦА УМНОЖЕНИЯ')
print("")

for i in range(2, 11):
    for j in range(2, 6):
        print(j, "x", i, "=", j * i, end="\t"*2)
    print("")

print("")

for i in range(2, 11):
    for j in range(6, 10):
        print(j, "x", i, "=", j * i, end="\t"*2)
    print("")

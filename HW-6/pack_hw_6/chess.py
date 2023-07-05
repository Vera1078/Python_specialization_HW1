# 1. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# 2. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок

from random import randint


def check_position(pos: str) -> bool:
    queens = [int(q) for q in pos.split()]
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            # проверка на один ряд или одну колонку
            if queens[j] // 10 == queens[i] // 10 or (queens[j] - queens[i]) % 10 == 0:
                return False
            # проверка на диагональ "вправо-вниз"
            if ((queens[j] // 10 > queens[i] // 10 and queens[j] % 10 > queens[i] % 10) or
                (queens[i] // 10 > queens[j] // 10 and queens[i] % 10 > queens[j] % 10)) and \
                    (queens[j] - queens[i]) % 11 == 0:
                return False
            # проверка на диагональ "влево-вниз"
            if ((queens[j] // 10 > queens[i] // 10 and queens[j] % 10 < queens[i] % 10) or
                (queens[i] // 10 > queens[j] // 10 and queens[i] % 10 < queens[j] % 10)) and \
                    (queens[j] - queens[i]) % 9 == 0:
                return False
    return True


def print_position(pos: str) -> None:
    queens = [int(q) for q in pos.split()]
    board = [[f'{i}'] + ['.'] * 8 for i in range(1, 9)]
    for queen in queens:
        board[queen // 10 - 1][queen % 10] = 'Q'
    print(' ', *[f'{i}' for i in range(1, 9)])
    for row in board:
        print(*row)


def random_position() -> str:
    pos = []
    while len(pos) < 8:
        queen = f'{randint(1, 8)}{randint(1, 8)}'
        if queen not in pos:
            pos.append(queen)
    return ' '.join(i for i in pos)


def get_all_positions() -> list[str]:
    results = []
    for cur_queen in range(11, 19):
        result = [str(cur_queen)]
        row = 2
        cell = 1
        while row < 9:
            while cell < 9:
                reviewed_queen = str(row * 10 + cell)
                tested_position = ' '.join(result) + ' ' + reviewed_queen
                if check_position(tested_position):
                    result.append(reviewed_queen)
                    if len(result) == 8:
                        results.append(' '.join(result))
                    if reviewed_queen[0] == '8' or len(result) == 8:
                        result.pop()
                        removed_queen = int(result.pop())
                        row = removed_queen // 10
                        cell = removed_queen % 10 + 1
                    else:
                        row += 1
                        cell = 1
                elif reviewed_queen[-1] == '8':
                    removed_queen = int(result.pop())
                    row = removed_queen // 10
                    cell = removed_queen % 10 + 1
                else:
                    cell += 1
                if not result:
                    break
            row += 1
            cell = 1
            if not result:
                break
    print(f'Все решения: {results}')
    print(f'Всего решений: {len(results)}')
    return results

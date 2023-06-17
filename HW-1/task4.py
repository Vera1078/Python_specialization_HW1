# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа  должна подсказывать «больше» или «меньше» после каждой попытки

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
tries_counter = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while tries_counter != 0:
    user_num = int(input ('Угадайте задуманное число в диапазоне от 0 до 1000. Ваше число: '))
    match num:
        case num if user_num == num:
            print('Bingo! Вы угадали! Задумано число {num}')
            break
        case num if user_num > num:
            tries_counter -= 1
            print(f'Число {user_num} больше загаданного, у Вас осталось {tries_counter} попытки(ок).')

        case num if user_num < num:
            tries_counter -= 1
            print(f'Число {user_num} меньше загаданного, у Вас осталось {tries_counter} попытки(ок).')
else:
        print(f'Вы проиграли! Попытки закончились, а число угадать не удалось. Было задумано число {num}')
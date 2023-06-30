# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# from math import sqrt
#
# num = int(input('Введите число от 0 до 100 000: '))
# primary = True
#
# if int(num) < 0 or int(num) > 100000:
#     print("Число не удовлетворяет требованиям! Попробуйте еще раз.")
# elif num == 0 or num == 1:
#     print('Число ни простое, ни составное')
# else:
#     for i in range(2, int(sqrt(num)+1)):
#         if num % i == 0:
#             primary = False
#             print(f'Число {num} СОСТАВНОЕ')
#             break
#     if primary:
#         print(f'Число {num} ПРОСТОЕ')



# Второй способ
MIN_NUM = 1
MAX_NUM = 100_000
QUANTITY_OF_DIVISORS_OF_PRIME_NUM = 2
result = None

while True:
    num = int(input('Введите целое число щт 1 до 100 000: '))
    if MIN_NUM <= num <= MAX_NUM:
        break

for i in range(2, int((num ** 0.5) + 1)):
    if num % i == 0:
        result = 'составное'
        break
    else:
        result = 'простое'

print(f'Число {num} -> {result}')


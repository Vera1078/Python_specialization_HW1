# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions
from math import gcd

n1, d1 = map(int, input("Введите первую дробь (вида a/b): ").split('/'))
n2, d2 = map(int, input("Введите вторую дробь (вида a/b): ").split('/'))
print('Мои методы: ')
if d1 == d2:
    sum_n = (n1+n2)//gcd(n1 + n2, d1)
    sum_d = d1//gcd(n1 + n2, d1)
    print('{}/{}'.format(sum_n, sum_d))
else:
    cd = int(d1 * d2 / gcd(d1, d2))
    rn = int(cd / d1 * n1 + cd / d2 * n2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    sum1 = n//gcd(n, d)
    sum2 = d//gcd(n, d)
    print('{}/{}'.format(sum1, sum2) if n != d else n)

n12 = n1 * n2
d12 = d1 * d2
mult1 = n12//gcd(n12, d12)
mult2 = d12//gcd(n12, d12)
print ('{}/{}'.format(mult1, mult2))

print('Проверочные методы: ')

print(fractions.Fraction(n1, d1) + fractions.Fraction(n2, d2))
print(fractions.Fraction(n1, d1) * fractions.Fraction(n2, d2))


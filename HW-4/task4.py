# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
import logging
import sys

from _decimal import Decimal


def add_money(money: Decimal):
    global cur_money, money_in_out_counter

    if money % 50 == 0:
        cur_money += money
        print(f'Добавлены средства в размере {money}\n')
        money_in_out_counter += 1
        logging.info(f"Внесено {money} у.е.")

    else:
        print('Ошибка. Количество вносимых средств должно быть кратно 50')


def get_money(money: Decimal):
    global cur_money, money_in_out_counter
    if cur_money - money < 0:
        print('Недостаточно средств на счете.\n')
        logging.info(f'Недостаточно средств на счете.')
    elif money % 50 == 0:
        commission = calc_commission(money=money)
        cur_money -= money + commission
        logging.info(f'Снято {money} у.е., удержана комиссия {commission} у.е.')
        print(f'Списание средств. Взята комиссия {commission}')
        money_in_out_counter += 1
    else:
        print('Ошибка. Количество вносимых средств должно быть кратно 50')

def calc_commission(money: Decimal) -> Decimal:
    global withdraw_percent, withdraw_min, withdraw_max, cur_money
    commission = money * withdraw_percent

    if commission < withdraw_min:
        return withdraw_min
    elif commission > withdraw_max:
        return withdraw_max
    else:
        return commission


def check_operation_counter():
    global bonus_percent, cur_money, money_in_out_counter
    if money_in_out_counter == 3:
        bonus = cur_money*bonus_percent
        cur_money += bonus
        print(f'Начислен бонус за 3 операции {bonus}\n')
        money_in_out_counter = 0


def get_wealth_tax():
    global cur_money, rich_percent
    if cur_money > max_balance:
        commission = cur_money*rich_percent
        print(f'Взята комиссия за богатство 10% {commission}у.е.\n')
        cur_money -= cur_money*rich_percent


cur_money = Decimal('0')
money_in_out_counter = 0
withdraw_percent = Decimal('0.015')
withdraw_min = Decimal(30)
withdraw_max = Decimal(600)
bonus_percent = Decimal('0.03')
max_balance = Decimal('5_000_000')
rich_percent = Decimal('0.1')

def run_atm():
    global cur_money
    choice = -1

    while choice != 0:
        print('---Главное меню---')
        check_operation_counter()
        get_wealth_tax()
        print(f'Текущий баланс = {cur_money}')
        print('Пополнение счета - выберите 1.\n Снятие средств - выберите 2.\n Выход - выберите 0.')
        choice = int(input('Выш выбор: '))

        match choice:
            case 1:
                add_money(money=Decimal(input('Введите сумму для пополнения кратную 50: ')))

            case 2:
                get_money(money=Decimal(input('Введите сумму для снятия кратную 50: ')))

            case 0:
                print('Работа завершена')
                logging.info(f"Сессия завершена")
                sys.exit()

logging.basicConfig(level=logging.INFO, filename="operetions_2.log", format="%(asctime)s %(message)s")
run_atm()


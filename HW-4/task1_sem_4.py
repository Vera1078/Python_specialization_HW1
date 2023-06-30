# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
# на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def remove_s():
    glob_dict = globals()
    for var in list(glob_dict):
        if len(var) > 1 and var[-1] == 's' and str(type(glob_dict[var])) != "<class 'function'>":
            glob_dict[var[:-1]] = glob_dict[var]
            glob_dict[var] = None

datas = "Hello, world!"
s = [20, 10, 1978]
names = "Катя", "Ира", "Валя"
sx = (37, 18, 44)

print(datas, '\n', s, '\n', names, '\n', sx)

remove_s()

print('------------------------')
print(f'Переменная datas = {datas}')
print(f'Переменная s = {s}')
print(f'Переменная names = {names}')
print(f'Переменная sx = {sx}')
print(f'Переменная data = {data}')
print(f'Переменная name = {name}')
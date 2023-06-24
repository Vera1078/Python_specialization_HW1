# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов

my_list = [4, 8, True, 'dff', 8, 4, True, 'fff', 7, 2, 8]
tmp = []
for item in my_list:
    if my_list.count(item) > 1:
        tmp.append(item)

res = list(set(tmp))
print(res)
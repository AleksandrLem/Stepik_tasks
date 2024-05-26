# Напишите программу для подсчета количества единиц каждого вида
# товара из приобретенных каждым покупателем интернет-магазина.

# Программа должна вывести список всех покупателей в лексикографическом порядке,
# после имени каждого покупателя — двоеточие, затем список названий всех
# приобретенных им товаров в лексикографическом порядке, после названия
# каждого товара — количество единиц товара. Информация о каждом товаре
# выводится на отдельной строке.

# сортируем список, чтобы потом выводить данные в лексикографическом порядке
lst_all = sorted(['Вячеслав Ручка 1', 'Филипп Ручка 1', 'Виктория Перо 3',
       'Вячеслав Линейка 4', 'Виктория Тетрадь 7', 'Вячеслав Ручка 29',
       'Филипп Циркуль 1'])

# создаем список со списками [имя, товар, количество]
lst_all = [strg.split() for strg in lst_all]

# преобразуем количество товара из str в int
lst_all = [[l[0], l[1], int(l[2])] for l in lst_all]

print(lst_all)
print()

# создаем словарь, где ключом будет имя, значением - список со списками товаров
# это нужно, чтобы у каждого имени покупателя был свой список товаров
dct_name = {}
for lst in lst_all:
    dct_name[lst[0]] = dct_name.get(lst[0], list())+[[lst[1], lst[2]]]
print(dct_name)
print()

# проходим по словарю, чтобы для каждого имени покупателя создать
# словарь с покупками, при этом если будут встречаться два одинаковых
# наименования товара с разным количеством, например ['Ручка', 1], ['Ручка', 29], то
# оставляем одно уникальное наименование товара, а количество товара суммируем,
# получится {'Ручка': 30}

for key, value in dct_name.items():
    dct_val = {}
    for lst in value:
        dct_val[lst[0]] = dct_val.get(lst[0], 0)+lst[1]
    dct_name[key] = dct_val
print(dct_name)


# выводим результат в соответствии с условием задачи
for key, value in dct_name.items():
    print(f'{key}:')
    for k, v in value.items():
        print(k, v)


# здесь пример как можно суммировать значения, если вытаскиваем из
# списка один и тот же ключ с разными значениями
# tst_lst = [['Ручка', 1], ['Ручка', 3], ['Ручка', 7],
#            ['Тетрадь', 7], ['Тетрадь', 1], ['Линейка', 4]]

# dct = {}
# for lst in tst_lst:
#     dct[lst[0]] = dct.get(lst[0], 0)+lst[1]
# print()
# print(dct)


# короткое и, наверное, наилучшее решение
# data = {}

# for _ in range(int(input())):
#     name, product, count = input().split()
#     data.setdefault(name, {})
#     data[name][product] = data[name].get(product, 0) + int(count)

# for person, products in sorted(data.items()):
#     print(f'{person}:')
#     for product, count in sorted(products.items()):
#         print(product, count)
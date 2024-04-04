# Дополните приведенный код так, чтобы он объединил содержимое двух
# словарей dict1 и dict2: если ключ есть в обоих словарях,
# добавьте его в результирующий словарь со значением, равным сумме
# соответствующих значений из первого и второго словаря; если ключ есть
# только в одном из словарей, добавьте его в результирующий словарь с
# его текущим значением. Результирующий словарь необходимо присвоить
# переменной result.



dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98,
         't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123,
         'w': 111, 'z': 666}

result = {}
# нам нужен исходный словарь dict2, поэтому создаем его копию
dict3 = dict2.copy()
# делаем конкетацию словарей dict1 и dict2, в итоге у нас получится
# один общий словарь, в котором будут все исходные значения словаря
# dict1 и к ним будут добавлены исходные значения словаря dict2
dict2.update(dict1)
print(dict2)

# теперь у нас есть один большой словарь dict2, в котором есть все ключи из
# исходного словаря dict1 и исходного словаря dict2
# проходим циклом for по словарю dict2
# в итоговый словарь result добавляем все ключи из обновленного словаря dict2,
# а значения этих ключей мы берем из исходного словаря dict1 и словаря dict2
# и суммируем эти значения
for key in dict2:
    result.setdefault(key, (dict1.get(key, 0)+dict3.get(key, 0)))
print(result)
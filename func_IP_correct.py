# IP-адрес – уникальный числовой идентификатор устройства в
# компьютерной сети, работающей по протоколу TCP/IP.

# В 4-й версии IP-адрес представляет собой
# 32-битное число. Адрес записывается в виде четырёх десятичных чисел
# (октетов) со значением от
# 0 до 255 (включительно), разделённых точками, например,
# 192.168.1.2
# 192.168.1.2.

# Напишите программу с использованием встроенной функции all()
# для проверки корректности IP-адреса: все ли октеты в
# IP-адресе – числа со значением от
# 0 до 255.

# Формат входных данных
# На вход программе подается строка в формате x.x.x.x, где x – непустой набор
# символов 0-9, a-z.

# Формат выходных данных
# Программа должна вывести True если введенная строка – корректный IP-адрес
# и False в противном случае.


try:
    s_all = all(map(lambda num: 0<=int(num)<=255, input('num=').split('.')))
    print(s_all)
except ValueError:
    print(False)

# или можно так:
# print(all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, input().split('.'))))
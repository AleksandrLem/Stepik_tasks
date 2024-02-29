# На вход программе подается строка натуральных чисел.
# Из элементов строки формируется список чисел.

# Напишите программу сортировки списка чисел в
# порядке неубывания суммы их цифр. При этом, если
# два числа имеют одинаковую сумму цифр, следует
# сохранить их взаиморасположение в начальном списке.

# Формат входных данных
# На вход программе подается строка текста,
# содержащая натуральные числа, разделенные пробелами.

# Формат выходных данных
# Программа должна вывести отсортированный
# список чисел в соответствии с условием задачи,
# разделяя его элементы одним пробелом.

'''Пример
Sample Input 1:
12 14 79 7 4 123 45 90 111

Sample Output 1:
12 111 4 14 123 7 45 90 79'''



str_lst = '111 14 79 7 4 123 90 45 12 171'.split()
# str_lst = [int(_) for _ in input().split()]

# создаем функцию, которая будет считать сумму цифр числа
def sum_num(strg):
    sum_n = 0
    for num in strg:
        sum_n += int(num)
    return sum_n

# эта же функция в коротком виде
def comparator(n):
    return sum([int(i) for i in str(n)]), n

# делаем сортировку, в качестве ключа передаем функцию sum_num
# распаковываем список, выводим на экран

print(*sorted(str_lst, key=sum_num))
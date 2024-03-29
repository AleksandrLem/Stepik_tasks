# На вход программе подается строка натуральных чисел.
# Из элементов строки формируется список чисел.

# Напишите программу сортировки списка чисел в порядке
# неубывания суммы их цифр. При этом, если у двух чисел
# одинаковая сумма цифр, их следует вывести в порядке неубывания.

# Формат входных данных
# На вход программе подается строка текста,
# содержащая натуральные числа, разделенные пробелами.

# Формат выходных данных
# Программа должна вывести отсортированный
# список чисел в соответствии с условием задачи,
# разделяя его элементы одним пробелом.



'''Пример
Sample Input 1:
111 14 79 7 4 123 90 45 12 171

Sample Output 1:
12 111 4 14 123 7 45 90 171 79'''



str_lst = '111 14 79 7 4 123 90 45 12 171'.split()

# сначала создаем список из чисел, затем сортируем его
int_lst = [int(i) for i in str_lst]
int_lst.sort()
print(int_lst)

# создаем функцию, которая будет считать сумму цифр числа
# значение strg должно быть str, т.к. нам нужна сумма цифр числа
def sum_num(strg):
    sum_n = 0
    for num in str(strg):
        sum_n += int(num)
    return sum_n

# эта же функция в коротком виде
def comparator(n):
    return sum([int(i) for i in str(n)]), n

# делаем сортировку, в качестве ключа передаем функцию sum_num
# распаковываем список, выводим на экран

print(*sorted(int_lst, key=sum_num))

'''Короткое решение!!!!!'''
# def comparator(n):
#     return sum([int(i) for i in str(n)]), n

# numbers = [int(i) for i in input().split()]

# print(*sorted(numbers, key=comparator))

# зачем добавляется ", n" в "sum([int(i) for i in str(n)]), n"?
# чтобы сортировка удовлетворяла условию задачи.
# Так как кортежи сравниваются поэлементно, то, если совпадут суммы,
# будут сравниваться сами числа.

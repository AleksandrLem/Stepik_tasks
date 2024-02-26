# На вход программе подаются два натуральных числа
# n и m, каждое на отдельной строке — количество строк и
# столбцов в матрице. Далее вводятся сами
# элементы матрицы — слова, каждое на отдельной строке;
# подряд идут элементы сначала первой строки, затем второй, и т.д.

# Напишите программу, которая сначала считывает
# элементы матрицы один за другим, затем выводит их в виде матрицы.

# Формат входных данных
# На вход программе подаются два числа
# n и m — количество строк и столбцов в матрице, далее идут
# n×m слов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести считанную матрицу, разделяя
#ее элементы одним пробелом.


n = int(input('количество строк матрицы: '))
m = int(input('количество столбцов матрицы: '))

matrix = []
# создаем матрицу n x m
for i in range(n):
    cols = []
    for j in range(m):
        strk = input('строка текста: ')
        cols.append(strk)
    matrix.append(cols)

print(matrix)

# выводим на экран матрицу n x m
# вывод по строкам...
for rows in range(n):
    for cols in range(m):
        print(matrix[rows][cols], end=' ')
    print()

# вывод по столбцам
for cols in range(m):
    for rows in range(n):
        print(matrix[rows][cols], end=' ')
    print()

'''Короткое решение'''
# n, m = int(input()), int(input())
# matrix = [[input() for _ in range(m)] for _ in range(n)]

# for row in matrix:
#     print(*row)
# Даны оценки по математике трёх учеников в 10-балльной шкале.
# Напишите программу, которая выводит такие оценки, которые встречаются
# не более, чем у двух учеников.

# Значит все, кроме тех, которые встречаются у всех трёх
# Для тех, кому нужна подсказка - объединение всех множеств за исключением
# пересечения всех множеств


s1 = set(int(i) for i in '1 5 4 2 5 6 6 2 3 3 5 2'.split())
s2 = set(int(i) for i in '2 3 5 10 2 10 2 6 7 10 10 6'.split())
s3 = set(int(i) for i in '1 4 6 9 8 7 0 9 0 9 8 10'.split())

print(*sorted((s1|s2|s3).difference(s1&s2&s3)))

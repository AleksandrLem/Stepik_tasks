# На вход программе подаются три строки текста с вещественными числами,
# значениями абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства.
# Напишите программу для проверки расположения всех точек с введенными
# координатами внутри либо на поверхности шара с центром в начале
# координат и радиусом R = 2.

# Формат входных данных
# На вход программе подаются три строки текста с вещественными числами,
# разделенными символом пробела – абсциссы, ординаты и аппликаты точек в
# трехмерной системе координат.

# Формат выходных данных
# Программа должна вывести True если все точки с введенными
# координатами находятся внутри или на границе шара и False, если вне.

# Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.

# Примечание 2. Уравнение поверхности шара (сферы) имеет вид:

# x**2 + y**2 + z**2 = R**2


# Примечание 3. Для решения задачи используйте встроенные функции all() и zip().

# Примечание 4. Используйте следующие названия abscissas, ordinates, applicates
# для соответствующих списков.

# ввод данных
abscissas = [float(num) for num in input('x=').split()] # координата x
ordinates = [float(num) for num in input('y=').split()] # координата y
applicates = [float(num) for num in input('z=').split()] # координата z


# собираем данные в один список с картежами, где каждый картеж
# состоит из координат x, y, z
x_y_z = zip(abscissas, ordinates, applicates)


# в каждом картеже находим сумму квадратов координат, т.е.
# x**2+y**2+z**2
xyz_map = map(lambda tpl: sum([i**2 for i in tpl]), x_y_z)


# проверяем будут ли суммы квадратов в картежах меньше
# либо равны квадрату радиуса, т.е. R**2 = 2**2 = 4
radius_ok = all(map(lambda el: el<=4, xyz_map))

print(radius_ok)
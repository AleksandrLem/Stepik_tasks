# Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B).
# Считается, что такие цвета хорошо гармонируют друг с другом.

# Напишите программу, которая по трем компонентам заданного цвета,
# находит компоненты противоположного цвета.

# Формат входных данных
# На вход программе подается строка, содержащая три целых
# неотрицательных числа, компоненты R, G и B начального цвета,
# разделенные символом пробела.

# Формат выходных данных
# Программа должна вывести три компонента R, G и B
# противоположного цвета, разделенные символом пробела.


rgb_invert = map(lambda el: 255-el, [int(i) for i in input('el=').split()])
print(*rgb_invert)

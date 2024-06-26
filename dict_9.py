# На вход программе подаются два предложения. Напишите программу,
# которая определяет, являются они анаграммами или нет. Ваша программа
# должна игнорировать регистр символов, знаки препинания и пробелы.

# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести YES , если предложения – анаграммы и
# NO в противном случае.

# Примечание. Кроме слов в тексте могут присутствовать пробелы и
# знаки препинания .,!?:;-. Других символов в тексте нет.



s1 = 'qwerty! poiu?'
s2 = 'ertyqw ipou'

s3 = sorted(list(''.join([i.strip('.,!?:;-').lower() for i in s1.split()])))
s4 = sorted(list(''.join([i.strip('.,!?:;-').lower() for i in s2.split()])))

print('YES' if s3==s4 else 'NO')
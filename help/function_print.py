# Функция print Python выводит заданные объекты на стандартное устройство вывода (экран) или отправляет
# их текстовым потоком в файл. Полный синтаксис функции print(): \
# print(*objects, sep=' ', end='n', file=sys. stdout, flush=False)


print('hello')
# hello

print('hello', 'world', sep='-')
# hello-world

# sep — это может быть строка, которую необходимо вставлять между значениями, по умолчанию — пробел.

print('hello', 'world', end='b')
# hello worldb

print(' ')
# end — это строка, которая добавляется после последнего значения.
# По умолчанию — это перенос на новую строку (\n).
# С помощью аргумента end программист может самостоятельно определить окончание выражения print.

item_list = ['world', 'python', 'best']

# вывод списка в одну строку
for item in item_list:
    print(item, end=' ')
# world python best


# file — файлоподобный объект (поток). По умолчанию — это sys.stdout.
# Здесь можно указать файл, в который нужно записать или добавить данные из функции print.

file = open('print.txt', 'a+')

for item in item_list:
    print(item, file=file)
file.close()

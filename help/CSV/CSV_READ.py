""" Модуль csv_read """

import csv

# Простое чтение из файла kp_data.csv
# Получаем итератор объекта
with open('kp_data.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    print(F_N_READER)  # <_csv.reader object at 0x000001B8E6F55820>
    print(type(F_N_READER))  # <class '_csv.reader'>
    for row in F_N_READER:
        print(row)
        # out : ['hostname', 'vendor', 'model', 'location']
        # out : ['kp1', 'Cisco', '2960', 'Moscow']

# Преобразование итератора в список
with open('kp_data.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    print(list(F_N_READER))
    # out [['hostname', 'vendor', 'model', 'location'], ['kp1', 'Cisco', '2960', 'Moscow'],
    # ['kp2', 'Cisco', '2960', 'Novosibirsk'], ['kp3', 'Cisco', '2960', 'Kazan'],
    # ['kp4', 'Cisco', '2960', 'Tomsk']]
    # Headers:  ['hostname', 'vendor', 'model', 'location']
    # Получаем список списков

# Разделение строки заголовков от содержимого
with open('kp_data.csv') as f_n:
    F_N_READER = csv.reader(f_n)
    F_N_HEADERS = next(F_N_READER)
    print('Headers: ', F_N_HEADERS)
    for row in F_N_READER:
        print(row)
    # out : Headers:  ['hostname', 'vendor', 'model', 'location']
    # ['kp1', 'Cisco', '2960', 'Moscow']
    # Выделяю заголовок

# Вывод результата с помощью метода DictReader
with open('kp_data.csv') as f_n:
    F_N_READER = csv.DictReader(f_n)
    for row in F_N_READER:
        print(row)
        print(row['hostname'], row['model'])

    # {'hostname': 'kp1', 'vendor': 'Cisco', 'model': '2960', 'location': 'Moscow'}
    # kp1 2960
    # {'hostname': 'kp2', 'vendor': 'Cisco', 'model': '2960', 'location': 'Novosibirsk'}
    # kp2 2960

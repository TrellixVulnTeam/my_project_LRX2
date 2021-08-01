# Синтаксис:

# next(iterator, default)

# Параметры:
# iterator - объект итератора, в котором определен метод __next__(),
# default - значение по умолчанию, которое будет возвращено вместо исключения StopIteration.
# Возвращаемое значение:
# следующий элемент итераторa.
# Описание:
# Функция next() возвращает следующий элемент итератора, вызвав его метод __next__().
my_list = [1, 2, 3]

iter_list = iter(my_list)

print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list, 0))


# 1
# 2
# 3
# 0
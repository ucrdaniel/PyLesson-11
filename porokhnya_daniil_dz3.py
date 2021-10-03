# 3.
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = []
while True:
    try:
        x = input('Введите натуральное число либо нажмите Enter, чтобы прекратить:')
        if x == '': break
        if x.isnumeric():
            print('numeric ', x)
            a.append(int(x))
        elif x[0] == '-':
            if x[1:].isnumeric():
                print('negative - ', x[1:])
                a.append(int(x))
        else:
            raise MyError('Ты что вводишь? Это не цифры. Смотреть надо...')
    except MyError as err:
        print(err)
print(a)
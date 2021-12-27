import random
import sys


# Главная функция реализует интерфейс с пользователем
def main():
    mass = []
    punkt = '0'
    while punkt != 'Q' and punkt != 'q':
        print('\nГлавное меню:',
              '\nP. Печатать массив (Print)',
              '\nC. Создать массив (Create)',
              '\nD. Удалить массив (Delete)',
              '\nT. Создать тестовый массив (Test)',
              '\nA. Добавить элемент в массив (Append)',
              '\nS. Сортировать элементы массива (Sort)',
              '\nH. Вычислить характеристику (Character)',
              '\nN. Количество элементов значений (Number)',
              '\nR. Удалить элемент по индексу (Remove At)',
              '\nM. Изменить элемент по индексу (Modify At)',
              '\nB. Перевернуть элементы массива (Backward)',
              '\nF. Заполнить случайными числами (randomFill)',
              '\nV. Переставить элементы местами (my Variant)',
              '\nO. Вычисленить максимум из разностей по модулю между соседними элементами (my Variant)'
              '\nQ. Завершить и выйти из программы (Quit)')

        punkt = (input('Введите команду:>'))

        if punkt == 'P' or punkt == 'p':
            P(mass)
        elif punkt == 'C' or punkt == 'c':
            C(mass)
        elif punkt == 'D' or punkt == 'd':
            D(mass)
        elif punkt == 'T' or punkt == 't':
            T(mass)
        elif punkt == 'A' or punkt == 'a':
            A(mass)
        elif punkt == 'S' or punkt == 's':
            S(mass)
        elif punkt == 'H' or punkt == 'h':
            H(mass)
        elif punkt == 'N' or punkt == 'n':
            N(mass)
        elif punkt == 'R' or punkt == 'r':
            R(mass)
        elif punkt == 'M' or punkt == 'm':
            M(mass)
        elif punkt == 'B' or punkt == 'b':
            B(mass)
        elif punkt == 'F' or punkt == 'f':
            F(mass)
        elif punkt == 'V' or punkt == 'v':
            V(mass)
        elif punkt == 'O' or punkt == 'o':
            O(mass)
        elif punkt == 'Q' or punkt == 'q':
            print('Program shutdown')
        else:
            print('Такой команды нет')


# Печать элементов массива в одну строку
def P(arr):
    size = len(arr)
    if size == 0:
        print('Элементов нет (пусто)')
    else:
        for i in range(size):
            print(arr[i], end=', ')
        print()


# Создание тестового массива
def T(arr):
    D(arr)
    tst = [3, -2, 6, -5, 9, 0, 1, -4]
    for i in range(len(tst)):
        arr.append(tst[i])
    P(arr)


# Удаление всех элементов массива
def D(arr):
    arr.clear()
    P(arr)


# Создание нового массива
def C(arr):
    size = int(input('Введите размер массива [0..99]:>'))
    if size < 0 or size > 99:
        print('Неверный размер массива')
    else:
        D(arr)
        for i in range(size):
            arr.append(1)
    P(arr)


# Удаление элемента по индексу
def R(arr):
    size = len(arr)
    if size == 0:
        print('Элементов нет (пусто)')
    else:
        print('Введите индекс [0 -', size - 1, end=']')
        i = int(input(':>'))
        if i < 0 or i >= size:
            print('Некорректный индекс')
        else:
            arr.pop(i)
    P(arr)


# Изменение элемента по индексу
def M(arr):
    size = len(arr)
    if size == 0:
        print('Элементов нет (пусто)')
    else:
        print('Введите индекс [0 -', size - 1, end=']')
        i = int(input(':>'))
        if i < 0 or i >= size:
            print('Некорректный индекс')
        else:
            arr[i] = int(input('Введите значение элемента:>'))
    P(arr)


# Добавление элемента в массив
def A(arr):
    m = int(input('Введите значение элемента:>'))
    arr.append(m)
    P(arr)


# Переворот элементов массива
def B(arr):
    arr.reverse()
    P(arr)


# Сортировка элементов массива
def S(arr):
    arr.sort()
    P(arr)


# Количество элементов массива с заданным значением
def N(arr):
    m = int(input('Введите значение элемента для поиска:>'))
    print('Массив содержит ', arr.count(m), ' таких элементов')


# Заполнение массива случайными числами
def F(arr):
    size = len(arr)
    for i in range(size):
        sign = random.randint(0, 2)
        if sign > 0:
            sign = 1
        else:
            sign = -1
        arr[i] = random.randint(1, 99) * sign
    P(arr)


# Расчёт характеристики (сумма) по элементам массива
def H(arr):
    summa = 0
    size = len(arr)
    for i in range(size):
        summa = summa + arr[i]
    print('Сумма элементов =', summa)


# Перестановка элементов массива (по заданию)
def V(arr):
    size = len(arr)
    if size < 2:
        print('Недостаточно элементов для перестановки')
    else:
        check = False
        for i in range(1, size):
            if (arr[i] % 2 == arr[i - 1] % 2) and (arr[i] != arr[i-1]) and check == False:
                value = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = value
                check = True
            else:
                check = False
    P(arr)


def O(arr):
    ct = 0
    size = len(arr)
    if size == 0:
        print(-1 * sys.maxsize)
    elif size == 1:
        print(abs(arr[0]))
    else:
        for i in range(1, size):
           if abs(arr[i] - arr[i-1]) > ct:
               ct = abs(arr[i] - arr[i-1])
        print(ct)


# Запуск главной функции
if __name__ == '__main__':
    main()

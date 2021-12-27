import random

# Набор тестовых матриц в виде кортежа словарей
test = ({'rows': 3, 'cols': 4, 'mass': [[3, 2, 6, 5],
                                        [9, 0, 1, 4],
                                        [7, 1, 8, 0]]
         },
        {'rows': 4, 'cols': 2, 'mass': [[3, 2],
                                        [6, 5],
                                        [9, 0],
                                        [1, 4]]
         },
        {'rows': 2, 'cols': 2, 'mass': [[7, 1],
                                        [8, 0]]
         }
        )


# Главная функция реализует интерфейс с пользователем
def main():
    print('Лаба: Матрица')
    # Создание рабочей матрицы в виде словаря
    # Значения матрицы хранятся в виде списка в списке
    matrix = {'rows': 0, 'cols': 0, 'mass': [[]]}
    # Переменная для пункта меню, выбранного пользователем
    punkt = '?'
    # Организация цикла опроса пользователя
    while (punkt != 'Q' and punkt != 'q'):
        # Вывод перечня пунктов меню
        if punkt == '?':
            print('\nГлавное меню:',
                  '\nP. Печатать матрицу (Print)',
                  '\nD. Удалить матрицу (Delete)',
                  '\nC. Создать нулевую матрицу (Create)',
                  '\nT. Создать тестовую матрицу (Tests)',
                  '\nZ. Заполнить матрицу змейкой (Snake)',
                  '\nH. Вычислить характеристику (cHaracter)',
                  '\nM. Изменить элемент по индексам (Modify)',
                  '\nV. Переставить элементы местами (Variant)',
                  '\nF. Заполнить заданным значением (Filling)',
                  '\nR. Заполнить случайными значениями (Random)',
                  '\nQ. Завершить и выйти из программы (Quit)')

        # Печать словаря c рабочей матрицей
        elif punkt == '0':
            print(matrix)
            # Обработка выбранных пунктов меню
        elif punkt == 'P':  # Печать
            P(matrix)
        elif punkt == 'D':  # Удаление
            D(matrix)
            print()
        elif punkt == 'C':  # Создание нулевой
            C(matrix)
            P(matrix)
        elif punkt == 'T':  # Создание тестовой
            T(matrix)
            P(matrix)
        elif punkt == 'M':  # Изменение
            M(matrix)
        elif punkt == 'F':  # Заполнение
            F(matrix)
            P(matrix)
        elif punkt == 'R':  # Случайные
            R(matrix)
            P(matrix)
        elif punkt == 'H':  # Характеристика
            H(matrix)
        elif punkt == 'Z':  # Зигзаг
            Z(matrix)
            P(matrix)
        elif punkt == 'V':  # Перестановка
            V(matrix)
            P(matrix)
        else:
            print('Такой команды нет')

        # Запрос пункта меню у пользователя
        punkt = (input('Введите команду:>')).upper()

    print('Программа завершена')


# Печать элементов матрицы
def P(matrix):
    # Получение размера матрицы
    rows = matrix['rows']
    cols = matrix['cols']
    print('Матрица ', '[', rows, 'x', cols, ']:', sep='')
    # Проверка, что в матрице есть элементы
    if rows * cols == 0:
        print('(пусто)')
    else:
        # Печать элементов матрицы по строкам
        for row in range(rows):
            for col in range(cols):
                print(matrix['mass'][row][col], end=',\t')
            print()
        print()


# Удаление элементов матрицы
def D(matrix):
    # Итерирование по строкам матрицы
    for row in range(matrix['rows']):
        print(row, ':', matrix['mass'][row], end=' -> ')
        # Удаление строки матрицы (списка значений)
        matrix['mass'][row].clear()
        print(matrix['mass'][row])

    print(matrix['mass'], end=' -> ')
    # Удаление матрицы (списка ссылок)
    matrix['mass'].clear()
    # Обнуление размера
    matrix['rows'] = 0
    matrix['cols'] = 0
    print(matrix)


# Создание нулевой матрицы
def C(matrix):
    # Блок ввода количества строк матрицы
    number = input('Введите количество строк матрицы [2..19]:>').strip()
    # Проверка, что введенное значение состоит только из цифр
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в целое число с проверкой на диапазон
    else:
        rows = int(number)
        if rows < 2 or rows > 19:
            print('Количество строк выходит за допустимый диапазон')
            return

    # Блок ввода количества столбцов матрицы
    number = input('Введите количество столбцов матрицы [2..19]:>').strip()
    # Проверка, что введенное значение состоит только из цифр
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в число с проверкой на диапазон
    else:
        cols = int(number)
        if cols < 2 or cols > 19:
            print('Количество столбцов выходит за допустимый диапазон')
            return

    # Другой способ удаления матрицы
    for line in matrix['mass']: line.clear()
    matrix['mass'].clear()

    # Создание новой матрицы (создание списка в списке)
    matrix['mass'] = [[0 for col in range(cols)] for row in range(rows)]
    # Сохранение размера матрицы
    matrix['rows'] = rows
    matrix['cols'] = cols


# Создание матрицы на основе тестовой матрицы
def T(matrix):
    global test

    # Блок выбора тестовой матрицы
    number = input('Выберите тестовую матрицу [1,2,3]:>')
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в целое число с проверкой на диапазон
    else:
        number = int(number) - 1
        if number < 0 or number > 2:
            print('Ошибка: введён недопустимый номер тестовой матрицы')
            return

    # Удаление текущей матрицы
    for line in matrix['mass']: line.clear()
    matrix['mass'].clear()

    # Копирование тестовой матрицы в текущую матрицу
    massiv = test[number]
    matrix['rows'] = massiv['rows']
    matrix['cols'] = massiv['cols']
    matrix['mass'] = [[massiv['mass'][row][col] for col in range(massiv['cols'])] for row in range(massiv['rows'])]


# Изменение элемента матрицы по двум индексам
def M(matrix):
    # Получение размера матрицы
    rows = matrix['rows']
    cols = matrix['cols']
    # Проверка, что в матрице есть элементы
    if rows * cols == 0:
        print('Элементов нет (пусто)')
        return

    # Блок ввода номера строки
    print('Введите номер строки [1..', rows, end=']')
    number = input(':>').strip()
    # Проверка, что введенное значение состоит только из цифр
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в целое число с проверкой на диапазон
    else:
        row = int(number)
        if row < 1 or row > rows:
            print('Ошибка: номер строки выходит за допустимый диапазон')
            return

    # Блок ввода номера столбца
    print('Введите номер столбца [1..', cols, end=']')
    number = input(':>').strip()
    # Проверка, что введенное значение состоит только из цифр
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в число с проверкой на диапазон
    else:
        col = int(number)
        if col < 1 or col > cols:
            print('Ошибка: номер столбца выходит за допустимый диапазон')
            return

    # Блок ввода нового значения
    print('Введите новое значение элемента [', matrix['mass'][row - 1][col - 1], end=']', sep='')
    number = input(':>').strip()
    # Проверка, что введенное значение состоит только из цифр
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в число с проверкой на диапазон
    else:
        number = int(number)

    # Изменение значения элемента
    matrix['mass'][row - 1][col - 1] = number


# Заполнение матрицы случайными значениями
def R(matrix):
    for row in range(matrix['rows']):
        for col in range(matrix['cols']):
            matrix['mass'][row][col] = random.randint(1, 999)


# Заполнение матрицы заданным значением
def F(matrix):
    # Получение размера матрицы
    rows = matrix['rows']
    cols = matrix['cols']
    # Проверка, что в матрице есть элементы
    if rows * cols == 0:
        print('Элементов нет (пусто)')
        return

    # Блок ввода заполнителя матрицы
    number = input('Введите значение элементов матрицы:>').strip()
    # Проверка, что введенное значение состоит только из цифр
    if not number.isdigit():
        print("Ошибка: требуется ввести цифровое значение")
        return
    # Преобразование значения в число
    else:
        number = int(number)

    # Заполнение матрицы введенным значением
    for row in range(rows):
        for col in range(cols):
            matrix['mass'][row][col] = number


# Расчёт характеристики (сумма элементов) матрицы (по заданию)
def H(matrix):
    averageRows = 0
    amountOfRowEls = 0
    for row in range(matrix['rows']):
        if row%2 == 0:
            for col in range(matrix['cols']):
                averageRows = averageRows + matrix['mass'][row][col]
                amountOfRowEls=amountOfRowEls+1
    averageRows = averageRows/amountOfRowEls
    averageColumns = 0
    amountOfColumnEls = 0
    for row in range(matrix['rows']):
        for col in range(matrix['cols']):
            if col%2==1:
                averageColumns = averageColumns + matrix['mass'][row][col]
                amountOfColumnEls=amountOfColumnEls+1
    averageColumns = averageColumns/amountOfColumnEls
    print('Разность среднего арифм. четн. столбцов и нечетн. строк =', averageRows, amountOfRowEls, averageColumns, amountOfColumnEls)


# Перестановка элементов матрицы (по заданию)
def V(matrix):
    # Получение размера матрицы
    rows = matrix['rows']
    cols = matrix['cols']
    # Проверка, что в матрице достаточно элементов
    if rows < 2 or cols < 2:
        print('Недостаточно элементов для перестановки')
        return
    columnIndex = input('Введите номер столбца, если хотите перевернуть всю матрицу, нажмите enter:>').strip()
    if not columnIndex.isdigit():
        for row in range(rows//2):
            rowPicked = matrix['mass'][row]
            matrix['mass'][row] = matrix['mass'][rows-row-1]
            matrix['mass'][rows-row-1] = rowPicked
    else:
        for row in range(rows//2):
            columnIndex = int(columnIndex)
            rowMemberPicked = matrix['mass'][row][columnIndex]
            matrix['mass'][row][columnIndex] = matrix['mass'][rows-row-1][columnIndex]
            matrix['mass'][rows - row - 1][columnIndex] = rowMemberPicked


# Заполнение матрицы зигзагом (по заданию)
def Z(matrix):
    # Получение размера матрицы
    rows = matrix['rows']
    cols = matrix['cols']
    # Проверка, что в матрице достаточно элементов
    if rows < 2 or cols < 2:
        matrix['mass'][0][0] = 1

    if rows*cols%2==0:
        number = 0
        rightDown = 1
        row = 0
        col = cols-1
        while number<rows*cols:
            if rightDown==1 and row<rows and col<cols:
                number+=1
                print('(', row, ',', col, ') = ', matrix['mass'][row][col], ' -> ', (3 * number * number - number) / 2,
                      sep='')
                matrix['mass'][row][col] = (3*number*number - number)/2
                row+=1
                col+=1
            elif rightDown==1 and (row == rows or col == cols):
                rightDown = 0
                if row==rows:
                    row-=1
                    col-=2
                else:
                    col-=1
            elif rightDown==0 and row>=0 and col>=0:
                number+=1
                print('(', row, ',', col, ') = ', matrix['mass'][row][col], ' -> ', (3 * number * number - number) / 2, sep='')
                matrix['mass'][row][col] = (3 * number * number - number) / 2
                row-=1
                col-=1
            elif rightDown==0 and (row <0 or col <0):
                rightDown = 1
                if row< 0 and col < 0:
                    row+=2
                    col=0
                elif row < 0:
                    row+=1
                else:
                    row+=2
                    col=0
    else:
        number = 0
        rightDown = 0
        row = rows - 1
        col = 0
        while number < rows * cols:
            if rightDown == 1 and row < rows and col < cols:
                number += 1
                print('(', row, ',', col, ') = ', matrix['mass'][row][col], ' -> ', (3 * number * number - number) / 2,
                      sep='')
                matrix['mass'][row][col] = (3 * number * number - number) / 2
                row += 1
                col += 1
            elif rightDown == 1 and (row == rows or col == cols):
                rightDown = 0
                if row == rows:
                    row -= 1
                else:
                    col -= 1
                    row -= 2
            elif rightDown == 0 and row >= 0 and col >= 0:
                number += 1
                print('(', row, ',', col, ') = ', matrix['mass'][row][col], ' -> ', (3 * number * number - number) / 2,
                      sep='')
                matrix['mass'][row][col] = (3 * number * number - number) / 2
                row -= 1
                col -= 1
            elif rightDown == 0 and (row < 0 or col < 0):
                rightDown = 1
                if row < 0 and col < 0:
                    row += 1
                    col += 2
                elif row < 0:
                    row += 1
                    col += 2
                else:
                    col = 0



# Запуск главной функции
if __name__ == '__main__':
    main()

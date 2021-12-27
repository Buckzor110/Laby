# Подключение модуля работы со временем и модуля работы с файлами
import time
import os.path


# Функция определяет режимы доступа к файлу или папке
# (R - на чтение, W - на запись, X - на исполнение)
def checkAccess(filename):
    filemode = ''
    if os.access(filename, os.R_OK):  filemode += 'R'
    if os.access(filename, os.W_OK):  filemode += 'W'
    if os.access(filename, os.X_OK):  filemode += 'X'
    return filemode


# Функция получает и печатает содержание директории
def Directories():
    # Получение пути к текущей директории
    path = os.getcwd()
    # Полагаем, что результат корректен
    ok = True
    # Цикл печати содержания директории
    while ok:
        print('Директория: ', path, ('[монтированная]' if os.path.ismount(path) else ''))

        # Получение содержания текущей директории
        names = os.listdir(path)
        names.sort()

        # Печать списка папок в текущей директории
        for name in names:
            # Формирование полного имени с путем
            item = path + '\\' + name
            # Проверка, что полное имя является папкой
            if os.path.isdir(item):
                # Получение даты и времени создания папки
                when = time.ctime(os.path.getctime(item))
                # Перевод имени папки в верхний регистр
                name = name.upper()
                # Печать информации о папке
                print(name.ljust(40), (chr(32) * 7), when)

        # Печать списка файлов в текущей директории
        for name in names:
            # Формирование полного имени с путем
            item = path + '\\' + name
            # Проверка, что полное имя является файлом
            if os.path.isfile(item):
                # Получение размера файла в байтах
                size = str(os.path.getsize(item))
                # Получение даты и времени изменения файла
                when = time.ctime(os.path.getmtime(item))
                # Перевод имени файла в нижний регистр
                name = name.lower()
                # Разбиение имени на пару (имя - расширение)
                pair = os.path.splitext(name)
                # Печать информации о файле
                print(pair[0].ljust(40), pair[1][1:].center(7), when, size.rjust(12), checkAccess(item))

        # Печать общей информации о директории
        print('Всего имен: ', len(names), '\n')

        # Полагаем, что результат не корректен, пока имя не введено
        ok = False
        # Цикл ввода имени директории
        while not ok:
            path = input('Введите имя директории [Пусто-Отмена]:>').strip()
            # Если введена пустая строка, то отмена обработки и возврат
            if path == '':
                print('Завершение просмотра директори')
                break

            # Проверка корректности имени директории
            if not checkFilename(path):
                print('Ошибка: имя директории не корректное')
                continue

            # Проверка существования директории
            if not os.path.isdir(path):
                print('Ошибка: такой директории не существует')
                continue

            # Имя директории корректное и она существует
            ok = True

    print(chr(13))


# Функция проверки имени файла на корректность
# (True - имя корректно или False - имя ошибочное)
def checkFilename(name):
    # Проверить, что имя содержит букву диска
    idx = name.find(':')
    # Если имя содержит диск
    if idx != -1:
        # Проверить, что двоеточие является вторым символом
        # и первым символом является латинская буква
        if idx != 1 or name[0].upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
    # Если буква диска с двоеточием находятся в начале имени
    # или имя не содержит буквы диска, то проверить на слеши
    idx = name.count('\\\\')
    # Если имя содержит двойные слеши
    if idx > 0:
        return False
    # Проверить, что имя не заканчивается на слеш
    if name.endswith('\\'):
        return False
    # Проверить, что имя не содержит запрещенных символов
    for idx in name:
        if idx in '\"<*?|>':
            return False
    return True


# Функция для форматирования строк результата
def Format(name, value):
    print(name.ljust(40, '_'), str(value).rjust(10, ':'))


# Функция обработки текста из файла
def main():
    print('Лаба: Строки и текстовые файлы')
    Ok = ''
    while Ok == '':
        name = '*'
        # Цикл ввода имени файла или директории
        while name == '*':
            # Ввод имени файла с фрагментом текста
            name = input('Введите имя файла [Пусто-Отмена]:>').strip()
            # Если введена пустая строка, то отмена обработки и завершение
            if name == '': return
            # Если введена звёздочка, то вотображение содержания директории
            if name == '*': Directories()

            # Проверка корректности имени файла
        if not checkFilename(name):
            print('Ошибка: имя файла не корректное')
            continue

        # Проверка существования файла
        if not os.path.exists(name):
            print('Ошибка: файл с указанным именем не существует')
            continue

        # Открытие файла на чтение
        try:
            file = open(name, encoding="utf8")
        except IOError:
            print('Ошибка: невозможно открыть файл на чтение')
            continue

        # Чтение текста из файла
        text = file.read()

        print(text)
        # Закрытие файла
        file.close()

        # Определение общего количества символов в тексте
        count = len(text)

        # Инициализация счётчиков
        count1 = count2 = count3 = count4 = 0

        # Обработка текста по одному символу
        for ch in text:
            # Проверка условий по заданию
            if ch in 'аеёиоуэюя':
                count1 += 1
            elif ch in 'БВДЖЗЙПМНР':
                count2 += 1
            elif ch == ' ':
                count3 += 1
            else:
                count4 += 1

        # Вывод результатов обработки
        print('Результаты обработки символов:')
        Format('Русских строчных гласных букв', count1)
        Format('Русских прописных звонких согласных букв', count2)
        Format('Пробельных символов', count3)
        Format('Прочих символов в тексте', count4)
        Format('Всего символов в тексте', count)

        # Объявление переменной для получения списка слов
        mass = text.split()

        # Определение количества слов
        count = len(mass)

        # Инициализация счётчиков
        count1 = count2 = count3 = 0

        # Обработка списка слов
        for word in mass:
            word = word.lower()
            # Проверка условий по каждому слову по заданию
            if word.find('енн') != (-1) or word.find('очк') != (-1):
                count1 += 1
                print('- ' + word + ' сч1=' + str(count1))
            if word.startswith('рас') or word.startswith('под'):
                count2 += 1
                print('- ' + word + ' сч2=' + str(count2))
            if word.endswith('ый') or word.endswith('ая'):
                count3 += 1
                print('- ' + word + ' сч3=' + str(count3))

        # Вывод результатов обработки слов
        print('Результаты обработки слов:')
        Format('Слов, содержащих \"енн\"/\"очк"', count1)
        Format('Слов, начинающихся с \"рас\"/\"под\"', count2)
        Format('Слов, заканчивающихся на \"ый\"/\"ая\"', count3)
        Format('Всего слов в тексте', count)

        # Подтверждение обработки ещё одного файла
        Ok = input('\nОбработать ещё один файл? [enter]')

    print('\nПрограмма завершена\n')


# Запуск главной функции
if __name__ == '__main__':
    main()

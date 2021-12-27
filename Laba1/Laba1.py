# Подключение математической библиотеки
import math
# Вычисление функции f(u,v) по заданию
def f(u, t):
	if u > t/4: result = math.pow(u, 2) + math.pow(t, 2)
	elif u < t/4: result = math.sqrt(t) + math.sqrt(u)
	else: result = (abs(u - t))/2
	return result

# Главная функция реализует ввод данных и вычисление функции z(x,y)
def main():
    Yes = 'да'
    while (Yes == 'да') or (Yes == 'yes'):
        # Ввод значений
        x = float(input('Введите X-значение:>'))
        y = float(input('Введите Y-значение:>'))
        # Расчёт функции
        z1 = f(math.sqrt(abs(math.pow(x, 2) - math.pow(y, 2))), math.pow(math.tan(y/x), 3))
        z2 = f(math.sin(x)/math.log(x, 10.0), math.pow(math.cos(y/x), 3))
        z3 = z1 + z2 + math.sin(f(math.exp(x)/y, math.sqrt(math.acos(abs(y-x)))))
        # Вывод результата
        print('Результат: Z({0}, {1})={2}'.format(round(x, 2), round(y, 2), round(z3, 2)))
        print('Z=', z3)
        # Подтверждение ввода новых значений
        Yes = input('Повторить ввод [да|yes]:>')
        Yes = Yes.lower()
        print()

# Запуск главной функции
if __name__ == '__main__':
    main()

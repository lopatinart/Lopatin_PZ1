# Даны положительные числа A и B (A > Б). На отрезке длины A размещено
# максимально возможное количество отрезков длины Б (без наложений). Не
# используя операции умножения и деления, найти длину незанятой части отрезка A.

# Ввод длины большего отрезка A
a = input('Введите длину большего отрезка A>> ')

# Обработка исключений
while type(a) != int:
    try:
        a = int(a)
        # Проверка на положительность числа A
        if a < 0:
            print("Неправильно ввели!")
            a = input('Введите длину большего отрезка A>> ')
    except ValueError:
        print("Неправильно ввели!")
        a = input('Введите длину большего отрезка A>> ')

# Ввод длины меньшего отрезка B
b = input('Введите длину меньшего отрезка B>> ')

# Обработка исключений
while type(b) != int:
    try:
        b = int(b)
        # Проверка на положительность числа B
        if b < 0:
            print("Неправильно ввели!")
            b = input('Введите длину меньшего отрезка B>> ')
    except ValueError:
        print("Неправильно ввели!")
        b = input('Введите длину меньшего отрезка B>> ')

# Проверка, что число A больше B
if a > b:
    total_occupied = 0  # Переменная для хранения занятой длины
    segments_count = 0  # Переменная для подсчета отрезков

    # Цикл для размещения отрезков B в отрезке A
    while total_occupied + b <= a:
        total_occupied += b  # Увеличиваем занятую длинну на отрезок B
        segments_count += 1   # Подсчитываем кол-во отрезков

    # Вычисляем длину незанятой части отрезка A
    unused_length = a - total_occupied

    # Выводим результат
    print(f"Длина незанятой части отрезка A: {unused_length}")
else:
    print("Неправильно ввели! \nЧисло A должно быть больше числа B!")
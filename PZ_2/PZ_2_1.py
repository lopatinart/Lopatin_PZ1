# Дано трехзначное число.
# Вывести число, полученное при прочтении исходного числа справа налево.

num = input('Введите трехзначное число>> ')

while type(num) != int:  # обработка исключений
  try:
    num = int(num)
    if 99 < num < 1000:  # обработка не трехзначных чисел
      break
    else:
      print("Вы неправильно ввели число!")
      num = input("Введите новое число>> ")
  except ValueError:
    print("Вы неправильно ввели число!")
    num = input("Введите новое число>> ")


num = str(num)  # обработка числа
num = (num[::-1])
print(int(num))
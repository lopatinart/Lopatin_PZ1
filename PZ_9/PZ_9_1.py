# Дан словарь на 6 персон, найти и вывести их средний возраст. (Пример,
# {"Андрей": 32, "Виктор": 29, "Максим": 18, …}, среднее 26,33).


list_of_Person = {
    "Андрей": 32,
    "Виктор": 29,
    "Максим": 18,
    "Наталья": 52,
    "Олег": 17,
    "Владимир": 41
}

print(f'Список людей>> {list_of_Person}\n')

srznach = 0

for name in list_of_Person:
    srznach += list_of_Person[name]

print(f'Средний возраст>> {srznach / len(list_of_Person)}')

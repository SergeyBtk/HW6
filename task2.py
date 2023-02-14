# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
random_numeros = []
i = 0
while i < 15: #задаем длину списка
    random_numeros.append(randint(1, 20))
    i = i + 1
print(random_numeros)
result = []
number1 = int(input('Введите первое число диапазона: '))
number2 = int(input('Введите второе число диапазона: '))
j = 0
for i in random_numeros:
    if i >= number1 and i <= number2:
        result.append(j)
    j += 1
print(result)

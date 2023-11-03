"""
Используя цикл for in, range c одним параметром и условные операторы ( там где они требуется ), вывести в консоль
через запятую числа до 20
через запятую четные числа до 20
через запятую нечетные числа до 20
baz если число кратно 3, bar если кратно 5 до 20
"""

for i in range(20):
    print(i, end=',')

print(f'\n{"-"*80}')  # this line using only dividing tasks

for i in range(20):
    if i % 2 == 0:
        print(i, end=',')

print(f'\n{"-"*80}')  # this line using only dividing tasks

for i in range(20):
    if i % 2 != 0:
        print(i, end=',')

print(f'\n{"-"*80}')  # this line using only dividing tasks

for i in range(20):
    if i % 3 == 0 and i != 0:
        print('baz', i)
    if i % 5 == 0 and i != 0:
        print('bar', i)

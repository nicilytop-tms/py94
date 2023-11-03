"""
Используя распаковку, цикл for in и кортежи в списке как исх. данные (задать самому):
- вывести в консоль только первый элемент каждого внутреннего кортежа
- вывести в консоль, все кроме первого элемента каждого внутреннего кортежа
"""

DATA = [('one', 'two', 'three'), ('four', 'five', 'six')]

for first, *others in DATA:
    print(first)

print(f'\n{"-"*80}')  # this line using only dividing tasks

for first, *others in DATA:
    for el in others:
        print(el)

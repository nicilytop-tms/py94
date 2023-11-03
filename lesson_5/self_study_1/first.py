"""
Написать функцию, которая, используя цикл for in, запрашивает у пользователя его
имя, возраст и пол и возвращает эти данные в кортеже.

Важно сделать проверку на пол, так как у пользователя только два варианта. (муж жен) и
во избежания ошибок - предоставить эту выборку (муж жен) пользователю перед вводом.
"""


def get_sex():
    choices = 'male', 'female'

    while True:
        sex = input(f'Input your sex please ({choices[0]} or {choices[1]}): ')  # better to do via 'or'.join(choices)
        if sex in choices:
            return sex

        print('Not valid value, try again')


def get_user_data():
    data = []

    for field in ['name', 'age', 'sex']:
        if field == 'sex':
            sex = get_sex()
            data.append(sex)
        else:
            data.append(input(f'Input your {field} please: '))

    return tuple(data)

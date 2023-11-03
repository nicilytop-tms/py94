"""
Создать список пользователей users = [{‘email’: ‘some@mail.ru’, ‘password’: ‘123pass’}, {..}, ..]
Сделать функции get_email - которая будет запрашивать email у пользователя и возвращать его,
get_password которая будет спрашивать пароль и возвращать его, и
check_data - которая будет принимать и проверять полученные данные (email, password) на наличие их в списке users
и если есть такой пользователь с введенными данными, возвращать email иначе возвращать строку с ошибкой.

Учесть, что структура данных пользователя, может меняться в будущем.
К примеру, {‘email’: ‘some@mail.ru’, ‘password’: ‘123pass’, ‘age’: 12}

А так же, нужно запускать эти функции в правильном порядке в глобальной области видимости, до тех пор,
пока пользователь вместо email не введет exit.
В этом случае - печатать в консоль прощальное сообщение, и завершать программу.
"""

ERROR_MESSAGE = 'Err. User not found'
EXIT_MESSAGE = 'exit'
users = [
    {'email': 'some@mail.ru', 'password': '123pass'},
    {'email': 'some1@mail.ru', 'password': '1234pass'},
    {'email': 'some2@mail.ru', 'password': '12345pass'},
]


def get_email():
    return input('Email: ')


def get_password():
    return input('Password: ')


def check_data(email, password):
    for user in users:
        email_checked = user.get('email') == email
        password_checked = user.get('password') == password
        if email_checked and password_checked:
            return email
    return ERROR_MESSAGE


while True:
    user_email = get_email()
    if user_email == EXIT_MESSAGE:
        print('Bye')
        break

    result = check_data(email=user_email, password=get_password())
    if result == ERROR_MESSAGE:
        print(result)

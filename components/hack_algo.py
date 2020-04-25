def hack_n_password_for_all_logins(login_generator, password_generator, request, limit=1000):
    login_state = None
    while True:
        login, login_state = login_generator(login_state)
        if login is None:
            break

        password_state = None
        for i in range(limit):
            password, password_state = password_generator(password_state)
            if password is None:
                break

            if request(login, password):
                print('SUCCESS', login, password)
                break


def hack_n_login_for_all_passwords(login_generator, password_generator, request, limit=100):
    password_state = None
    while True:
        password, password_state = password_generator(password_state)
        if password is None:
            break

        login_state = None
        for i in range(limit):
            login, login_state = login_generator(login_state)
            if login is None:
                break

            if request(login, password):
                print('SUCCESS', login, password)
                break


def hack_login_password_random(login_generator, password_generator, request, limit=10000):
    login_state = None
    password_state = None
    for attempt in range(limit):
        login, login_state = login_generator(login_state)
        password, password_state = password_generator(password_state)
        if login is None or password is None:
            break
        if request(login, password):
            print('SUCCESS', login, password)

from components import hack_algo, generators, requesters

hack_algo.hack_login_password_random(
    generators.generate_logins,
    generators.generate_passwords_brute_force,
    requesters.request_local_server
)

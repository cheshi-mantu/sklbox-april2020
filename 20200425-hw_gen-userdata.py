"""
password generator based on user data
name, surname, email address, birthdate
"""
import requests
# makingthe authentication
# user data is stored like name surname email
users_db = {"admin":["Alec","Baldwin", "alec_baldwin@famous.com","1958-04-03"],
            "jack": ["Jack", "Black", "bj@huh.eh", "1969-08-28"],
            "cat":["Cathelyn", "Stark","cath@winterfell.com", "1500-02-28"]}
def auth(username, password):
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': username, 'password': password})
    return response.status_code

def traverse_db(db):
    for key, value in db.items():
        pass_gen(key, value)
#generator
def pass_gen(username, user_data):
    #adding empty string to 1st position in the list
    user_data.insert(0,"")
    for i in range(len(user_data)):
        for j in range(len(user_data)):
            print (user_data[i]+user_data[j])


traverse_db(users_db)

#quite a strange development



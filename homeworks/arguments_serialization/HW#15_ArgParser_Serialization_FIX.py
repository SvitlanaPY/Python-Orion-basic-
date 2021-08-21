"""
1. Написати програму яка буде зберігати username і email в файл json.
    При наявності користувачів перед тим як додати юзера програма повинна перевірити чи не існує на данний момент користувача з таким username і email,
    якщо існує вивести помилку.
"""
import json
import os.path

if os.path.isfile("users.json"):
    with open("users.json", "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = []
else:
    data = []

# Initial version:
# with open("users.json", "r") as file:
#     data = json.load(file)
#     # data = [{'user_name': 'Kurt', 'last_name': 'Cobain', 'email': 'KurtCobain@gmail.com'}, {'user_name': 'Kate', 'last_name': 'Lee', 'email': 'KateLee@gmail.com'}, {'user_name': 'Nick', 'last_name': 'Rome', 'email': 'NickRome@gmail.com'}]
#     # print(type(data))   # <class 'list'>

while True:
    user_name = input("Enter username (or Q to exit): ")
    if user_name == 'Q':
        break
    email = input("Enter user's email (or Q to exit): ")
    if email == 'Q':
        break
    new_elem = {}
    for elem in data:
        if user_name == elem['user_name'] or email == elem['email']:
            print("WARNING: User with such name or email already exists. Try again")
            break
    else:
        new_elem['user_name'] = user_name
        new_elem['email'] = email
        data.append(new_elem)

with open('users.json', 'w') as file_f:
    json.dump(data, file_f, indent=4)


print("THE END")


# INPUTS FOR TESTING:
# (1) positive case (when entered user does not exist in file):
# user_name = David
# email = DavidJonson@gmail.com


# (2) negative case (when entered user already exists in a file):
# user_name = Nick
# email = NickRome@gmail.com
# OUTPUTS: "WARNING: User with such name or email already exists. Try again"

import json


def getUsers():
    with open("innlogging/users.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    return data

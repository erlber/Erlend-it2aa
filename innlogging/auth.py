import json

class Auth:
    def __init__(self):
        self.users = self.getUsers()

    def login(self, userName, password):
        for user_id in self.users:
            if self.users[user_id]["userName"] == userName and self.users[user_id]["password"] == password:
                return True
            
    def getUsers(self):
        with open("innlogging/users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
        
    def registrer(self):
        pass

import datetime


class GameDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.games = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.games = {}

        for line in self.file:
            picture, name, size, price, description, os, processor, graphics, storage = line.strip().split(";")
            self.games[picture] = (name, size, price, description, os, processor, graphics, storage)

        self.file.close()

    def get_user(self, picture):
        if picture in self.games:
            return self.games[picture]
        else:
            return -1

    # def add_user(self, email, password, name, dateofbirth, nationality, phonenumber):
    #     if email.strip() not in self.games:
    #         self.games[email.strip()] = (password.strip(), name.strip(), dateofbirth.strip(), nationality.strip(), phonenumber.strip(), self.get_date())
    #         self.save()
    #         return 1
    #     else:
    #         print("Email already exists")
    #         return -1

    # def validate(self, email, password):
    #     if self.get_user(email) != -1:
    #         return self.games[email][0] == password
    #     else:
    #         return False

    def save(self):
        with open(self.filename, "w") as f:
            for name in self.games:
                f.write(name + ";" + self.games[name][0] + ";" + self.games[name][1] + ";" + self.games[name][2] + ";" + self.games[name][3] +";" + self.games[name][4] +";" + self.games[name][5] +";" + self.games[name][6] +"\n")

    #@staticmethod
    # def get_date():
    #     return str(datetime.datetime.now()).split(" ")[0]

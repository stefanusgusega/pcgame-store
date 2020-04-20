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
            picture, name, size, price, description, os, processor, graphics, storage,link = line.strip().split(";")
            self.games[picture] = (name, size, price, description, os, processor, graphics, storage,link)

        self.file.close()

    def get_user(self, picture):
        if picture in self.games:
            return self.games[picture]
        else:
            return -1

    def save(self):
        with open(self.filename, "w") as f:
            for name in self.games:
                f.write(name + ";" + self.games[name][0] + ";" + self.games[name][1] + ";" + self.games[name][2] + ";" + self.games[name][3] +";" + self.games[name][4] +";" + self.games[name][5] +";" + self.games[name][6] +";" + self.games[name][7] +"\n")

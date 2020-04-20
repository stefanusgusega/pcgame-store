import datetime

class EwalletDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, balance = line.strip().split(";")
            self.users[email] = balance

        self.file.close()

    def get_balance(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user] + "\n")

    def substract_balance(self, email, amount):
        if email.strip() in self.users:
            user_data = self.get_balance(email)
            if user_data != -1:
                if int(self.users[email]) - int(amount) > 0:
                    self.users[email] = str(int(self.users[email]) - amount)
                    self.save()                
                    return 1
                else:
                    print("Money is not enough!")
                    return -1
        else:
            print("Email doesn't exist!")
            return -1

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from env import PASSWORD, EMAIL

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

    # def add_user(self, email, password, name, dateofbirth, nationality, phonenumber, balance):
    #     if email.strip() not in self.users:
    #         self.users[email.strip()] = (password.strip(), name.strip(), dateofbirth.strip(), nationality.strip(), phonenumber.strip(), self.get_date(),balance.strip())
    #         self.save()
    #         return 1
    #     else:
    #         print("Email already exists")
    #         return -1

    # def validate(self, email, password):
    #     if self.get_user(email) != -1:
    #         return self.users[email][0] == password
    #     else:
    #         return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user] + "\n")

    # def send_email(self, email, token):
    #     msg = MIMEMultipart()
        
    #     message = "Dear, \nYour token to change your password is " + token + ".\nCopy and paste it to your PCGame Store App\n Thank you."
    #     password = PASSWORD
    #     msg['From'] = EMAIL
    #     msg['To'] = email
    #     msg['Subject'] = "Forgot Password - PCGameStore Apllication"
        
    #     msg.attach(MIMEText(message, 'plain'))
    #     server = smtplib.SMTP('smtp.gmail.com: 587')
    #     server.starttls()
        
    #     server.login(msg['From'], password)
    #     server.sendmail(msg['From'], msg['To'], msg.as_string())
    #     server.quit()

    # def change_password(self, email, newpassword):
    #     if email.strip() in self.users:
    #         user_data = self.get_user(email)
    #         if user_data != -1:
    #             self.users[email.strip()] = (newpassword, user_data.full_name, user_data.dateofbirth, user_data.nationality, user_data.phonenumber, user_data.created,user_data.balance)
    #             self.save()
    #         return 1
    #     else:
    #         print("Email doesn't exist")
    #         return -1
    def substract_balance(self, email, amount):
        if email.strip() in self.users:
            user_data = self.get_balance(email)
            if user_data != -1:
                self.users[email] = str(int(self.users[email]) - amount)
                self.save()
            return 1
        else:
            print("Email doesn't exist")
            return -1

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

import re
class Check ():
    def check_national_id (self, n_id):
        self.national_id = n_id 
        correct_national_id = False
        while correct_national_id == False:
            check = re.match(r"^\d{10}$", self.national_id)
            if check != None:
                correct_national_id = True
                return self.national_id
            else:
                self.national_id = input("Invalid National ID!\nPlease Enter it again: ")

    def check_phone_number (self, tel):
        self.phone_number = tel
        correct_phone_number = False
        while correct_phone_number == False:
            check = re.match(r"^09\d{9}$", self.phone_number)
            if check != None:
                correct_phone_number = True
                return self.phone_number
            else:
                self.phone_number = input("Invalid Phone Number!\nPlease Enter it again: ")

    def check_email (self, email):
        self.email = email
        correct_email = False
        while correct_email == False:
            check = re.match(r"^\w+@[A-z]{5,6}\.[A-z]{3,4}$", self.email)
            if check != None:
                correct_email = True
                return self.email
            else:
                self.email = input("Invalid Email!\nPlease Enter it again: ")    

    def check_username (self, username):
        self.username = username
        correct_username = False
        while correct_username == False:
            check = re.match(r"[\w\-@#,]{8,20}$", self.username)
            if check != None:
                correct_username = True
                return self.username
            else:
                self.username = input("Invalid Username!\nPlease make another one: ")

    def check_password (self, password):
        self.password = password
        correct_password = False
        while correct_password == False:
            check = re.match(r"^.*(?=.{8,20})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", self.password)
            if check != None:
                correct_password = True
                return self.password
            else:
                self.password = input("It's not a strong Password!\nEnter another one: ")
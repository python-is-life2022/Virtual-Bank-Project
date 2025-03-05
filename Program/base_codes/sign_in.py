from mysql.connector import *
from random import randint
from check_inputs import Check
cnx = Connect(username = "root",
              password = "amir1379",
              host = "localhost",
              database = "virtual_bank")
print ("Connected Successfully!")
query = cnx.cursor()
class New_User ():
    def __init__ (self, f_name, l_name, age, b_date, n_id, tel, email, address, save, username, password):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.birth_date = b_date
        self.national_id = n_id
        self.phone_number = tel
        self.email = email
        self.address = address
        self.saving = save
        self.username = username
        self.password = password
    
    def create_account_number (self):
        correct_account_number = False
        while correct_account_number == False:
            try:
                account_number_list = [str(randint(0, 9)) for i in range (16)]
                self.account_number = ''.join(account_number_list)
            except IntegrityError:
                duplicate_account_number = False
                query.execute("SELECT account_number FROM users")
                account_numbers = query.fetchall()
                i = 0
                while duplicate_account_number == False:
                    if self.account_number in account_numbers[i]:
                        duplicate_account_number = True
            except Exception as ex:
                print (type(ex))
            else:
                correct_account_number = True

    def create_cart_password (self):
        cart_password_list = [str(randint(0, 9)) for i in range(4)]
        self.cart_password = ''.join(cart_password_list)

    def insert_into_user_table (self):
        correct_info, excecption_raised = False, False
        while correct_info == False and excecption_raised == False:
            try:
                query.execute("INSERT INTO users (f_name, l_name, age, b_date, n_id, tel, email, address, b_save, account_number, cart_pass, username, pass_w)"\
                            "VALUES (\'%s\', \'%s\', \'%i\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%i\', \'%s\', \'%s\', \'%s\', \'%s\')" % (self.first_name,
                                                                                                                                                    self.last_name,
                                                                                                                                                    self.age,
                                                                                                                                                    self.birth_date,
                                                                                                                                                    self.national_id,
                                                                                                                                                    self.phone_number,
                                                                                                                                                    self.email,
                                                                                                                                                    self.address,
                                                                                                                                                    self.saving,
                                                                                                                                                    self.account_number,
                                                                                                                                                    self.cart_password,
                                                                                                                                                    self.username,
                                                                                                                                                    self.password))
            except IntegrityError:
                duplicate_national_id, duplicate_phone_number, duplicate_email, duplicate_username = False, False, False, False
                query.execute ("SELECT n_id, tel, email, username FROM users")
                unique_fields = query.fetchall()
                i = 0
                check = Check()
                while duplicate_national_id == False and duplicate_phone_number == False and duplicate_email == False and duplicate_username == False:
                    if self.national_id in unique_fields[i]:
                        self.national_id = check.check_national_id(input("One user found with this National ID!\nEnter it again: "))
                        duplicate_national_id = True
                    if self.phone_number in unique_fields[i]:
                        self.phone_number = check.check_phone_number(input("One user found with this Phone Number!\nEnter it again: "))
                        duplicate_phone_number = True
                    if self.email in unique_fields[i]:
                        self.email = check.check_email(input("One user found with this Email Address!\nEnter it again: "))
                        duplicate_email = True
                    if self.username in unique_fields[i]:
                        self.username = check.check_username(input("One user found with this Username!\nMake another one: "))
                        duplicate_username = True
                    i += 1
            except DataError:
                print ("\nInvalid Input!")
                excecption_raised = True
            except Exception as ex:
                print (type(ex))
                excecption_raised = True
            else:
                cnx.commit()
                print(f"\nGreat {self.first_name} {self.last_name}*Thank you for Choosing our Bank.")
                correct_info = True
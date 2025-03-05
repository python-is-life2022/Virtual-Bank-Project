from check_inputs import Check
from mysql.connector import *
cnx = Connect(username= "root",
              password = "amir1379",
              host = "localhost",
              database = "virtual_bank")
query = cnx.cursor()
class Login():
    def __init__ (self, username, password):
        self.username = username
        self.password = password
    
    def enter_username_and_password (self):
        self.find_username = False
        self.correct_password = False
        query.execute("SELECT username, pass_w FROM users")
        usernames_passwords = query.fetchall()
        i = 0
        while i < len(usernames_passwords) and self.find_username == False:
            if self.username == usernames_passwords[i][0]:
                self.find_username = True
                while self.correct_password == False:
                    if self.password == usernames_passwords[i][1]:
                        self.correct_password = True
                    else:
                        check = Check()
                        question = int(input("Incorrect Password!\n1)Forgotten Password\n2)Try Again\nWhich one:"))
                        match question:
                            case 1:
                                self.password = check.check_password(input("Please create new Password: "))
                                query.execute("UPDATE users SET pass_w = \'%s\' WHERE username = \'%s\'" % (self.password, self.username))
                                cnx.commit()
                                print ("\nChanges Saved Succesfully.")
                                self.correct_password = True
                            case 2:
                                self.password = input("Please Enter your Password again: ")
                            case _:
                                print ("Invalid Number!")
            i += 1
        if self.find_username == False:
            print ("User not found!")
        return self.find_username, self.correct_password
            
    def money_transfer(self):
        self.money = int(input("How much money do you want to Transfer: "))
        self.cart_id = input("Enter the account number that you want to Transfer money to that: ")
        query.execute("SELECT b_save FROM users WHERE username = \'%s\' AND pass_w = \'%s\'" % (self.username,
                                                                                               self.password))
        self.saving = query.fetchone()[0]
        if self.saving > self.money:
            try:
                query.execute("SELECT f_name, l_name, b_save FROM users WHERE account_number = \'%s\'" % self.cart_id) 
                info_list = query.fetchone()
                self.first_name = info_list[0]
                self.last_name = info_list[1]
                self.increse_saving = info_list[2]
            except DataError:
                print ("Wrong Data Type!")
            except TypeError:
                print("User Not found with this Account Number!")
            except Exception as ex:
                print (type(ex))
            else:
                trf = int(input(f"Do you want to transfer {self.money} dollars to {self.first_name} {self.last_name}?\n1)Yes\n2)No\nWhich one: "))
                match trf:
                    case 1:
                        self.increse_saving += self.money
                        query.execute("UPDATE users SET b_save = \'%i\' WHERE account_number = \'%s\'" % (self.increse_saving,
                                                                                                        self.cart_id))
                        cnx.commit()
                        query.execute("SELECT b_save FROM users WHERE username = \'%s\'" % self.username)
                        self.descrese_saving = query.fetchone()[0]
                        self.descrese_saving -= self.money
                        query.execute("UPDATE users SET b_save = \'%i\' WHERE username = \'%s\'" % (self.descrese_saving,
                                                                                                    self.username))
                        cnx.commit()
                        print("\nMoney Transfered.")
                    case 2:
                        print("\nTransfered Canceled!")
        elif self.saving == self.money:
            print ("You Can't Transfer All of your money!")
        else:
            print ("Not enough inventory!")
    
    def deposit_money (self):
        self.money = int(input("How much money do you want to Deposit: "))
        query.execute ("SELECT b_save FROM users WHERE username = \'%s\' AND pass_w = \'%s\'" % (self.username, self.password))
        self.increse_saving = query.fetchone()[0]
        self.increse_saving += self.money
        query.execute("UPDATE users SET b_save = \'%i\' WHERE username = \'%s\' AND pass_w = \'%s\'" % (self.increse_saving,
                                                                                                        self.username,
                                                                                                        self.password))
        cnx.commit()
        print("Changes Saved Succesfully.")

    def taking_inventory (self):
        query.execute("SELECT f_name, l_name, b_save, account_number FROM users WHERE username = \'%s\' and pass_w = \'%s\'" % (self.username, 
                                                                                                                                self.password))
        user_info = query.fetchone()
        print (f"\n{user_info[0]} {user_info[1]} with Account Number: {user_info[3]}\nYour Inventory: {user_info[2]}")

    def delete_account (self):
        self.choose = int(input("Do you really want to delete your account from our bank:\n1)Yes\n2)No\nChoose: "))
        match self.choose:
            case 1:
                query.execute("DELETE FROM users WHERE username = \'%s\' AND pass_w = \'%s\'" % (self.username, self.password))
                cnx.commit()
                print ("We are very sorry that you deleted your account :*(")
            case 2:
                print ("We are very glad that your opinion changed :)")
            case _:
                print ("Invalid Input!")
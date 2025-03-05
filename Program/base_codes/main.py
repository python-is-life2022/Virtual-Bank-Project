import re
from check_inputs import Check
from sign_in import New_User
from login import Login
from datetime import datetime

program_parts = int(input("1)Create Bank Account\n2)Logging in your Account\nChoose one part: "))
match program_parts:
    case 1:
        print ("***Welcome to your Bank***")
        first_name = input("Please Enter your Firstname: ").title()
        last_name = input("Please Enter your Lastname: ").title()
        correct_birth_date = False
        while correct_birth_date == False:
            birth_date = input("Please Enter your Birthdate with this Format(yyyy-mm-dd): ")
            birth_date_parts = re.split(r"[\-/,:]", birth_date)
            birth_date_year = int(birth_date_parts[0])
            birth_date_month = int(birth_date_parts[1])
            birth_date_day = int(birth_date_parts[2])
            if birth_date_month >= 1 and birth_date_month <= 12 and birth_date_day >= 1 and birth_date_day <= 31:
                today_year = datetime.today().year
                today_month = datetime.today().month
                today_day = datetime.today().day
                if today_month < birth_date_month:
                    age = (today_year - birth_date_year) - 1
                elif today_month == birth_date_month:
                    if today_day < birth_date_day:
                        age = (today_year - birth_date_year) - 1
                    else:
                        age = today_year - birth_date_year
                else:
                    age = today_year - birth_date_year
                correct_birth_date = True
            else:
                print ("Invalid Date!")
        check = Check()
        n_id = check.check_national_id(input("Please Enter your National ID: "))
        tel = check.check_phone_number(input("Please Enter your Phone Number: "))
        email = check.check_email(input("Please Enter your Email Address: "))
        address = input("Please Enter your Address: ")
        correct_saving = False
        while correct_saving == False:
            saving = int(input("Please deposit at least $100 into your account: "))
            if saving >= 100:
                correct_saving = True
            else:
                print ("It's less than $100!\n")
        username = check.check_username(input("Please make a Username for yourself: "))
        password = check.check_password(input("Please make a strong password for yourself: "))
        user = New_User(first_name, last_name, age, birth_date, n_id, tel, email, address, saving, username, password)
        user.create_account_number()
        user.create_cart_password()
        user.insert_into_user_table()
    case 2:
        print ("Logging Page: \n")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        log = Login(username, password)
        result_username, result_password = log.enter_username_and_password()
        if result_username == True and result_password == True:
            log_part = int(input("\nOperations:\n1)Transfer Money\n2)Deposit Money\n3)Taking Inventory\n4)Delete Account\nWhich operation do you want: "))
            match log_part:
                case 1:
                    log.money_transfer()
                case 2:
                    log.deposit_money()
                case 3:
                    log.taking_inventory()
                case 4:
                    log.delete_account()
                case _:
                    print ("Invalid Input!")
    case _:
        print ("Invalid Input!")
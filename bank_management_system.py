class Bank:
    def __init__(self, name):
        self.name = name
        self.__total_balance = 0
        self.__total_loan_amount = 0
        self.__can_take_loan = True
        self.user_list = {}
        self.admin_list = {}
        self.history = {}

    def get_balance(self):
        return self.__total_balance

    def get_loan_balance(self):
        return self.__total_loan_amount

    @property
    def can_loan(self):
        return self.__can_take_loan

    @can_loan.setter
    def can_loan(self, switch):
        self.__can_take_loan = switch

    def deposit(self, amount):
        self.__total_balance += amount

    def withdraw(self, amount):
        if self.__total_balance >= amount:
            self.__total_balance -= amount
            return True
        else:
            return False


class Admin:
    def __init__(self, name):
        self.name = name
        self.loan = 0
        self.balance = 0
        self.type = "Admin"
    
    def create_account(self, bank_obj, phone_number, email_address, home_address):
        self.phone_number = phone_number
        self.email_address = email_address
        self.home_address = home_address
        print(f"Admin Account Created in {bank_obj.name}\n")
        bank_obj.admin_list[self.name] = 1
    
    def total_balance_of_bank(self, bank_name):
        if self.name in bank_name.admin_list:
            print(f"Total Balance of {bank_name.name} is {bank_name.get_balance()}")
        else:
            print(f"Admin not Authorized to get access of {bank_name.name}")
    
    def can_take_loan(self, bank_name):
        if self.name in bank_name.admin_list:
            bank_name.can_loan = not bank_name.can_loan
        else:
            print(f"Admin account not found.")


class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.loan = 0
        self.type = "User"

    def create_account(self, bank_obj, phone_number, email_address, home_address):
        self.phone_number = phone_number
        self.email_address = email_address
        self.home_address = home_address
        print(f"User Account Created in {bank_obj.name}\n")
        bank_obj.user_list[self.name] = 1

    def deposit(self, bank_obj, amount):
        if self.name in bank_obj.user_list:
            bank_obj.deposit(amount)
            self.balance += amount
            print(f"Deposited {amount} BDT in {bank_obj.name}")
        else:
            print("No account")

    def withdraw(self, bank_name, amount):
        if self.name in bank_name.user_list:
            if bank_name.withdraw(amount):
                self.balance -= amount
                print(f"{amount} BDT Withdrawn from {bank_name.name}")
            else:
                print(f"Can't withdraw. {bank_name.name} is bankrupt.")
        else:
            print("No account")
        
    def check_user_balance(self, bank_name):
        if self.name in bank_name.user_list:
            print(f"User: {self.name} Balance: {self.balance} in {bank_name.name}")
        else:
            print("No account")
    
    def take_loan_from_bank(self, bank, amount):
        if self.name in bank.user_list:
            if bank.can_loan:
                if self.balance * 2 >= (self.loan + amount):
                    if bank.withdraw(amount):
                        self.loan += amount
                        bank.get_loan_balance += amount
                        print(f"Loan taken: {amount} BDT")
                    else:
                        print("Can't take a loan. Withdrawal failed.")
                else:
                    print("Can't take a loan. The loan amount exceeds twice your balance.")
            else:
                print("Loan is not enabled.")
        else:
            print("No account")
    
    def balance_transfer(self, bank_name, new_user, amount):
        if self.name in bank_name.user_list and new_user.name in bank_name.user_list:
            if self.balance >= amount:
                self.balance -= amount
                new_user.balance += amount
                print(f"{amount} Transferred to {new_user.name}")
            else:
                print("Not enough balance")
        else:
            print("Can't Transfer. No account")
    
    def transaction_history(self, bank_name):
        if self.name in bank_name.user_list:
            for i in bank_name.history[self.name]:
                print(i)
        else:
            print("No account")


bank = Bank("MyBank")
A = Admin("A")
A.create_account(bank, "1234567890", "A@example.com", "Admin's Home Address")

Ua = User("Ua")
Ua.create_account(bank, "9876543210", "Ua@example.com", "User's Home Address")

A.total_balance_of_bank(bank)
Ua.deposit(bank, 1000)
A.total_balance_of_bank(bank)
Ua.withdraw(bank, 500)
A.total_balance_of_bank(bank)

# Ua.take_loan_from_bank(bank, 200)
# Ua.check_user_balance(bank)

# Ub = User("Ub")
# Ub.create_account(bank, "1111111111", "Ub@example.com", "Ub's Home Address")

# Ua.balance_transfer(bank, Ub, 100)
# Ua.check_user_balance(bank)
# Ub.check_user_balance(bank)

# Ua.transaction_history(bank)
# Ub.transaction_history(bank)

# Assignment 10
# Question2@
class Car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model 
        self.year = year
    
    def dispaly_info(self):
        return f'The car is a {self.model} from {self.make} that was made in the year {self.year}'

car1 = Car('Testla', 'Cyber Truck', 2023)

print(car1.dispaly_info())
print(car1.model)

#Question 3:
class BankAccount:
    bank_name = "Tech4Girls Bank"
    def __init__(self, account_holder):
        self. balance = 0
        self.account_holder = account_holder
        

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'\n Your account has been updated. Your new balance is {self.balance}'
        else:
            print('\n Invalid amount. Please try again')

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            return f'\n Your account has been debited with {amount}'
        else:
            print(f'\n Your balance is insufficient to proceed')
       
    @staticmethod
    def bank_policy():
        return f'\n Bank Policy: Terms and policies apply to every package !!!'

    @classmethod
    def get_bank_name(cls):
        return f'\n This is {cls.bank_name} '

cus1 = BankAccount('Beatrice')
cus2 = BankAccount('Samuella')

cus1.deposit(100)
cus2.deposit(500)

cus1.withdraw(10000)
cus2.withdraw(100)

BankAccount.bank_policy()
print(BankAccount.bank_policy())
print(BankAccount.get_bank_name())


#Question 4
class Employee:
    def __init__(self, name,position):
        self.name = name
        self. position = position

    def get_details(self):
        return f"\nYou are{self.name} and you hold the position of {self.position}"
    
    
    class Manager():
        super():
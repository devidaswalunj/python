
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self._account_number = account_number
        self.__balance = balance

    def __update_balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.__balance:
            self.__update_balance(-amount)
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def show_account_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self._account_number)
        print("Account Balance:", self.__balance)


b = BankAccount("Devidas", 123456, 5000)

print("Account Holder:", b.account_holder)

print("Account Number:", b._account_number)
print("Private Balance:", b._BankAccount__balance)

b.deposit(2000)

b.withdraw(1000)

print("\nFinal Account Details:")
b.show_account_details()
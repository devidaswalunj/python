class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self._account_number = account_number
        self.__balance = balance



b = BankAccount("Devidas", 123456, 5000)


print("Account Holder:", b.account_holder)
print("Account Number:", b._account_number)
# Single Level Inheritance
# Single Parent - Single Child
# Child class inherits from a single parent class
# Parent class = Superclass
# Child class = Subclass / Inherited class


# Parent class / Superclass
class Account:
    def __init__(self, acc_no, acc_holder_name):
        self.acc_no = acc_no
        self.acc_holder_name = acc_holder_name

    def deposit(self, amount):
        print(f"{self.acc_holder_name} deposited {amount} in your account")


# Child class / Subclass
class SavingAccount(Account):
    def __init__(self, acc_no, acc_holder_name, interest_rate):
        super().__init__(acc_no, acc_holder_name)
        self.interest_rate = interest_rate

    def rate(self):
        print(
            f"{self.acc_holder_name} with account number {self.acc_no} "
            f"has an interest rate of {self.interest_rate}%"
        )


# Creating objects
s1 = SavingAccount(1542478, "Ram", 10)
s2 = SavingAccount(7842478, "Sita", 12)

# Displaying details
print("Single Level Inheritance")

print(s1.acc_no)
print(s1.acc_holder_name)
print(s1.interest_rate)
s1.rate()
# Calling inherited method
s1.deposit(50000)
s2.deposit(60000)



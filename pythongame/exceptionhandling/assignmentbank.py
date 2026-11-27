class  UnsufficientBalance(Exception):
    def __init__(self,msg):
        self.msf=msg
class Minimumbalance(Exception):
    def __init__(self,msg):
        self.msf=msg

class bank(UnsufficientBalance,Minimumbalance):
    def __init__(self,amount):
        self.balance=5000
    def deposit(self):
        self.balance +=self.amount
        self.withdraw()
    def withdraw(self):
        if self.balance<self.amount and 500>self.amount :
            raise Minimumbalance("amount not should be less than 500rs")
        elif self.balance <self.amount:
            raise Minimumbalance("amount is greter  than balance")
        else:
            self.balance-=self.amount
            print("money debited")
            print(self.balance)

b=bank(4000)

class SBI():
    def calculate(self):
            self.interest = self.loan * self.rate_of_interest * self.no_of_year / 100
            self.total = self.loan + self.interest
            print("Amount of Loan:", self.loan)
            print("Number of year:", self.no_of_year)
            print("Rate of interest:", self.rate_of_interest)
            print("Total interest:", self.interest)
            print("Total loan amount to paid:", self.total)

class HDFC():
    def calculate(self):
            self.interest = self.loan * self.rate_of_interest * self.no_of_year / 100
            self.total = self.loan + self.interest
            print("Amount of Loan:", self.loan)
            print("Number of year:", self.no_of_year)
            print("Rate of interest:", self.rate_of_interest)
            print("Total interest:", self.interest)
            print("Total loan amount to paid:", self.total)            

class AXIS():
    def calculate(self):
            self.interest = self.loan * self.rate_of_interest * self.no_of_year / 100
            self.total = self.loan + self.interest
            print("Amount of Loan:", self.loan)
            print("Number of year:", self.no_of_year)
            print("Rate of interest:", self.rate_of_interest)
            print("Total interest:", self.interest)
            print("Total loan amount to paid:", self.total)
class Bank():
    def __init__(self,loan,rate_of_interest,no_of_year,obj):
          self.loan=loan
          self.rate_of_interest=rate_of_interest
          self.no_of_year=no_of_year
          obj.calculate(self)



b=Bank(50000,8,8,SBI())
print()
b=Bank(50000,8,8,HDFC())
print()
b=Bank(50000,8,8,AXIS())






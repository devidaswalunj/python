class Bank():

    def __init__(self, name, loan, no_of_year, rate_of_interest):
        self.name = name
        self.loan = loan
        self.no_of_year = no_of_year
        self.rate_of_interest = rate_of_interest
        self.calculate()

    def display(self):
        print("Bank Name:", self.name)
        print("Amount of Loan:", self.loan)
        print("Number of year:", self.no_of_year)
        print("Rate of interest:", self.rate_of_interest)
        print("Total interest:", self.interest)
        print("Total loan amount to paid:", self.total)


class SBI(Bank):

    def calculate(self):
        self.interest = self.loan * self.rate_of_interest * self.no_of_year / 100
        self.total = self.loan + self.interest
        self.display()


class HDFC(Bank):

    def calculate(self):
        self.interest = self.loan * self.rate_of_interest * self.no_of_year / 100
        self.total = self.loan + self.interest
        self.display()


class Axis(Bank):

    def calculate(self):
        self.interest = self.loan * self.rate_of_interest * self.no_of_year / 100
        self.total = self.loan + self.interest
        self.display()




s = SBI("SBI", 50000, 8, 10)

print("*********************************")

h = HDFC("HDFC", 50000, 8, 9)

print("*********************************")

a = Axis("Axis", 50000, 8, 11)
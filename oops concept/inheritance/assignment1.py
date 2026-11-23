class Bank():

    def display(self):
        print("Bank Name:",self.name)
        print("Amount of Loan:",self.loan)
        print("Number of year:",self.no_of_year)
        print("Rate of interest:",self.rate_of_interest)
        print("total interest:",self.interest)
        print("total loan amount to paid:",self.total)
class SBI(Bank):
    def __init__(self,name,loan,no_of_year,rate_of_interest):
        self.name=name
        self.loan=loan
        self.no_of_year=no_of_year
        self.rate_of_interest=rate_of_interest
        self.calculate()
       

    def calculate(self):
        self.interest=self.loan*self.rate_of_interest*self.no_of_year/100
        self.total=self.loan+self.interest
        self.display()

class HDFC(Bank):
    def __init__(self,name,loan,no_of_year,rate_of_interest):
        self.name=name
        self.loan=loan
        self.no_of_year=no_of_year
        self.rate_of_interest=rate_of_interest
        self.calculate()
        

    def calculate(self):
        self.interest=self.loan*self.rate_of_interest*self.no_of_year/100
        self.total=self.loan+self.interest
        self.display()


class Axis(Bank):
    def __init__(self,name,loan,no_of_year,rate_of_interest):
        self.name=name
        self.loan=loan
        self.no_of_year=no_of_year
        self.rate_of_interest=rate_of_interest
        self.calculate()
       
        
    def calculate(self):
        self.interest=(self.loan*self.rate_of_interest*self.no_of_year)/100
        self.total=self.loan+self.interest
        self.display()
a=Axis("Axis",50000,8,10)
S=SBI("SBI",40000,6,10)
h=HDFC("HDFC",65000,9,10)

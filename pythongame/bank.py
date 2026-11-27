
class SBI():
    def CreditScore(self):
        if self.Credit_Score >= 750:
            self.credits = "You have a good Credit Score!"
            self.interest_rate_on_credit_score = 0

        elif self.Credit_Score >= 650:
            self.credits = "You have an Average Credit Score!"
            self.interest_rate_on_credit_score = 2

        else:
            self.credits = "You have not a good Credit Score!"
            self.interest_rate_on_credit_score = 3

        return self.interest_rate_on_credit_score

    def check_interest_rate(self):

        if self.Type_of_Loan == "Personal Loan":
            self.interest_rate = 8 + self.CreditScore()

        elif self.Type_of_Loan == "Home Loan":
            self.interest_rate = 7 + self.CreditScore()

        elif self.Type_of_Loan == "Vehicle Loan":
            self.interest_rate = 9 + self.CreditScore()

        elif self.Type_of_Loan == "Education Loan":
            self.interest_rate = 4 + self.CreditScore()

        elif self.Type_of_Loan == "Business Loan":
            self.interest_rate = 11 + self.CreditScore()

        elif self.Type_of_Loan == "Agriculture Loan":
            self.interest_rate = 6 + self.CreditScore()

        else:
            print("Please enter correct loan type")
            return None

        return self.interest_rate

    def calculate(self):

        self.interest = (
            self.loan * self.interest_rate * self.no_of_year) / 100

        self.total = self.loan + self.interest
class HDFC():

    def CreditScore(self):
    
            if self.Credit_Score >= 750:
                self.credits="You have a good Credit Score!"
                self.interest_rate_on_credit_score = 0
    
            elif self.Credit_Score >= 650:
                self.credits="You have a AverageCredit Score!"
                self.interest_rate_on_credit_score = 1.5
    
            else:
                self.credits="You have not a good Credit Score!"
                self.interest_rate_on_credit_score = 3
            return self.interest_rate_on_credit_score

    def check_interest_rate(self):

        if self.Type_of_Loan == "Personal Loan":
            self.interest_rate = 8.5+self.CreditScore()

        elif self.Type_of_Loan == "Home Loan":
            self.interest_rate = 9+self.CreditScore()

        elif self.Type_of_Loan == "Vehicle Loan":
            self.interest_rate = 6+self.CreditScore()

        elif self.Type_of_Loan == "Education Loan":
            self.interest_rate = 4.5+self.CreditScore()

        elif self.Type_of_Loan == "Business Loan":
            self.interest_rate = 10+self.CreditScore()

        elif self.Type_of_Loan == "Agriculture Loan":
            self.interest_rate = 5+self.CreditScore()

        else:
            print("Please enter correct loan type")
            return None

        return self.interest_rate

    def calculate(self):

        self.interest = (self.loan * self.interest_rate * self.no_of_year ) / 100

        self.total = self.loan + self.interest

class AXIS():

    def CreditScore(self):
    
            if self.Credit_Score >= 750:
                self.credits="You have a good Credit Score!"
                self.interest_rate_on_credit_score = 0

            elif self.Credit_Score >= 650:
                self.credits="You have a AverageCredit Score!"
                self.interest_rate_on_credit_score = 2
    
            else:
                self.credits="You have not a good Credit Score!"
                self.interest_rate_on_credit_score =3.5


    def check_interest_rate(self):

        if self.Type_of_Loan == "Personal Loan":
            self.interest_rate = 9.5+self.CreditScore()

        elif self.Type_of_Loan == "Home Loan":
            self.interest_rate = 8.5+self.CreditScore()

        elif self.Type_of_Loan == "Vehicle Loan":
            self.interest_rate = 6.5+self.CreditScore()

        elif self.Type_of_Loan == "Education Loan":
            self.interest_rate = 4.5+self.CreditScore()

        elif self.Type_of_Loan == "Business Loan":
            self.interest_rate = 11+self.CreditScore()

        elif self.Type_of_Loan == "Agriculture Loan":
            self.interest_rate = 6+self.CreditScore()

        else:
            print("Please enter correct loan type")
            return None

        return self.interest_rate

    def calculate(self):

        self.interest = (self.loan * self.interest_rate * self.no_of_year ) / 100

        self.total = self.loan + self.interest



class B_app(SBI,HDFC,AXIS):

    def __init__(self, Customer_name, Bank_name, loan, no_of_year, Credit_Score, Monthly_Income, Type_of_Loan):

        self.Customer_name = Customer_name
        self.Bank_name = Bank_name.upper()
        self.loan = loan
        self.no_of_year = no_of_year
        self.Credit_Score = Credit_Score
        self.Monthly_Income = Monthly_Income
        self.Type_of_Loan = Type_of_Loan
        self.find_bank()
        self.display()
    def find_bank(self):

        if self.Bank_name == "SBI":
            SBI.CreditScore(self)
            SBI.check_interest_rate(self)
            SBI.calculate(self)

        elif self.Bank_name == "HDFC":
            HDFC.CreditScore(self)
            HDFC.check_interest_rate(self)
            HDFC.calculate(self)
            

        elif self.Bank_name == "AXIS":
            AXIS.CreditScore(self)
            AXIS.check_interest_rate(self)
            AXIS.calculate(self)
            

        else:
            print("Please enter a correct bank name")
            return

        

    
    def display(self):
        print("\n*****************LOAN DETAILS**********************")
        print(f"Dear {self.Customer_name} {self.credits}")
        print("Customer Name:", self.Customer_name)
        print("Bank Name:", self.Bank_name)
        print("Loan Type:", self.Type_of_Loan)
        print("Loan Amount:", self.loan)
        print("Number of Years:", self.no_of_year)
        print("Credit Score:", self.Credit_Score)
        print("Monthly Income:", self.Monthly_Income)
        print(f"original Interest rate in your {self.Type_of_Loan} : ",self.interest_rate-self.CreditScore())
        print(f" your credit Score is {self.Credit_Score} base on interest rate is: ", self.CreditScore())
        print("Total Rate of Interest:", self.interest_rate, "%")
        print("Total Interest:", self.interest)
        print("Total Loan Amount to be Paid:", self.total)


# -----------------------------------------------------------------------------------

Customer_name = input("Enter your name: ")
Bank_name = input('''
SBI
HDFC
AXIS
Enter bank name:''')

loan = float(input("How much loan do you require? "))

no_of_year = int(input("For how many years do you want the loan? "))

Credit_Score = int(input("Enter your credit score: "))

Monthly_Income = float(input("Enter your monthly income: "))

Type_of_Loan = input("""
1) Personal Loan
2) Home Loan
3) Vehicle Loan
4) Education Loan
5) Business Loan
6) Agriculture Loan

Enter your loan type: """)


b = B_app(Customer_name, Bank_name, loan, no_of_year, Credit_Score, Monthly_Income,Type_of_Loan)
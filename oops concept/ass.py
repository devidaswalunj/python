#create a class calculator create to instance variable (from user), create 4 instance method add sub mul div


class calculator():
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def add(self):
        add=self.number1+self.number2
        print("addition : ",add)

    def sub(self):
        sub=self.number1-self.number2
        print("substraction : ",sub)
    def mul(self):
        mul=self.number1*self.number2
        print("multiplication: ",mul)
    def div(self):
        div=self.number1/self.number2
        print("division: ",div)

number1=eval(input("enter number 1: "))
number2=eval(input("enter number 2: "))
c1=calculator(number1,number2)
c1.add()
c1.sub()
c1.mul()
c1.div()




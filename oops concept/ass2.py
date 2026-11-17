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
choice=eval(input(''' 

1.addition
2.substraction
3.multiplication
4.division           
enter your choice:''' ))

if choice==1:
    c1.add()
elif choice==2:
    c1.sub()
elif choice==3:
    c1.mul()
elif choice==4:
    c1.div()
else:
    print("wrong choice")




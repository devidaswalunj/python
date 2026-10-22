#Accept a number from user and check whether the number is prime or not
"""
number=int(input("enter the number for check it is prime or not: "))
while number>0:
    for i in range(2,number):
        if number<=1:
                print("entered number is not prime")
        else:
           if number %i==0:
            print("entered number is not prime", number)
            break
    else:   
            print("entered number is prime", number)

    number=0
    """
#################################

number = int(input("Enter the number: "))
flag=0
for i in range(2, number):
        if number % i == 0:
                flag=1
                break
if flag==1:
        print("Number is not prime:", number)
else:
        print("Number is prime:", number)



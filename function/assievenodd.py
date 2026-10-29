# def check_number(num):
#     if num%2==0:
#         print("number is even: ",num)
#     else:
#         print("number is odd: ",num)
# num=int(input("enter the number : "))
# check_number(num)



# Function to find the factorial of a number
def fact(num):
    fact = 1    

    for i in range(1, num + 1):
        fact = fact * i

    return fact

num = int(input("Enter the number: "))
nu = fact(num)

print("Factorial of number:", nu)

#using while loop
def fact(num):
    fact = 1    

    while num>=1:
        fact = fact * num
        num=num-1

    return fact

num = int(input("Enter the number: "))
nu = fact(num)

print("Factorial of number:", nu)

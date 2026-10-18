"""
conditional statement
1)if
2)if    else
3) if   elif    else

"""
'''
n1=int(input("Enter the number:"))

if n1<15:
    print("entered number is less than 15!")
print(n1)

n1=int(input("Enter the 1 number:"))
n2=int(input("Enter the 2 number:"))

if n1>n2:
    print("max: ", n1)
else:
    print("max: ", n2)

'''
state=input("enter the state:  ")
if state=="Maharashtra":
    print("capital:mumbai")
elif state=="Gujarat":
    print("capital:gandinagar")
elif state=="Uttar Pradesh":
    print("capital:luckhnow")
else:
    print("invalid state")


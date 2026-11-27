#try except

try:
    n1=eval(input("enter the n1: "))
    n2=eval(input("enter the n2: "))
    n3=n1/n2
    print("n3: ",n3)
except:
    print("some error")

print("code executed")
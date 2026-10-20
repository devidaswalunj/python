#1 print number from 1 to 10
'''
i=1
while i<11:
    print(i)
    i=i+1

#2 accept a number and print its table   

num=int(input("enter the number"))
i=1
while i<11:
    print(num*i)
    i=i+1
#accept name from user until you enter your name
a="devidas"
i=1
s=1
while i==s:
    name=input("enter your name: ")
    if name==a:
        print("stoped")
        s=s+1



#4accept a number and print reverse of that number
num=int(input("enter a number: "))
while num>0:
    str1=str(num)
    #print(type(str1))
    #print(str1)
    a=str1[::-1]
    num=0
print(int(a))
'''
num=int(input("enter a number: "))
rev=0
while num>=0:
    
    d=num%10
    rev=rev*10+d
    num=num//10

print(rev)












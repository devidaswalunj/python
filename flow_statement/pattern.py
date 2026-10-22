#1 2 3 4 6 7 8 9 10(use only 1 while loop)

i=1
while i<11:
        if i==5:
            i+=1
            continue
        else:
            print(i,end=" ")
            i+=1


print("\n")
#another way to print 1 2 3 4 6 7 8 9 10
i=1
while i<11:
    for i in range(1,11):
        if i==5:
            i+=1
            continue
        else:
            print(i,end=" ")
            i+=1

print("\n")
#Accept a number from user and check whether the number is prime or not
number = int(input("Enter the number: "))

if number <= 1:
    print("Number is not prime:", number)
else:
    i = 2
    while i < number:
        if number % i == 0:
            print("Number is not prime:", number)
            break
        i += 1

    else:
        print("Number is prime:", number)








number=int(input("enter the number enter a number to find it is palindrome or not: "))
num=number
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
print(rev)
if rev==number:
    print("number is palindrome number")
else:
    print("number is not palindrome number")






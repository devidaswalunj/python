num1=int(input("enter the 1st subject mark:"))
num2=int(input("enter the 2nd subject mark:"))
num3=int(input("enter the 3rd subject mark:"))
num4=int(input("enter the 4th subject mark:"))
num5=int(input("enter the 5th subject mark:"))
total_mark=num1+num2+num3+num4+num5
percentage=total_mark/5
print("percentage is : ", percentage)
if percentage>=75:
    print(f"percentage is {percentage} and pass with Distinction")
elif percentage>=60 and percentage<75:
    print(f"percentage is {percentage} and pass with First class")
elif percentage>=50 and percentage<60:
    print(f"percentage is {percentage} and pass with Second class")
elif percentage>=40 and percentage<50:
    print(f"percentage is {percentage} and pass ")
else:
    print(f"percentage is {percentage} and fail")

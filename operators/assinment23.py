#create a list from even number 1 to 100 which is divisible by 7
l1=[]
for i in range(1,101):
    if i%2==0:
        if i%7==0:
            l1.append(i)
print(l1)

l1=[]
for i in range(0,100,2):
        if i%7==0:
            l1.append(i)
print(l1)

l1=[]
for i in range(1,100):
        if i%2==0 and i%7==0 :
            l1.append(i)
print(l1)

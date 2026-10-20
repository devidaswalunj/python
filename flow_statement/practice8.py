"""
for i in range(4):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("+++++++++++++++++++")
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()
print("+++++++++++++++++++")
#4
for i in range(1,5):
    for j in range(1,i+1):
        if i==3:
            print(j,end="")
        else:
            print("*",end="")
    print()
print("+++++++++++++++++++")




"""


for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#for i in range(5):
#    print("*" * i)
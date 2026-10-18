str="Python"
a=0
b=-len(str)
for x in str:
    print(f"character is : {x} and positive index is :{a} or negative index is: {b}")
    a+=1
    b+=1

print("=======================================================================================================")
#another way
str="Python"
a=0
b=len(str)
for x in str:
    print(f"character is : {x} and positive index is :{a} or negative index is: {a-b}")
    a+=1




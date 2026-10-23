#string data type:
 #method and built-in function of string data type

"""
s="python is a programming language"
#indexing
print(s[0])

#silicing
print(s[0:6])

#mathematical op
s="python"
s1="java"
print(s+s1)
print(s*3)
#membership operator
s2="python is a programming language"
s3="python"
print(s3 in s2)
print("java" not in s2)

#comparison operator
s4="python"
s5="Python"
print(s4 <s5)

state1=input("enter the state:  ")
state=state1.strip() #remove both side space
#state=state1.rstrip()  #remove right side space
#state=state1.lstrip()   #remove left side space

if state=="Maharashtra":
    print("capital:mumbai")
elif state=="Gujarat":
    print("capital:gandinagar")
elif state=="Uttar Pradesh":
    print("capital:luckhnow")
else:
    print("invalid state")
"""

#find,rfind,index
ss="python is a programming language"
s=ss.find("is")
print(s)

s=ss.rfind("is") # it five the last index of "is" but it give position of first "is" from right side
print(s)

s=ss.index("is")
print(s)

s=ss.find("s", 5,15)  #find "s" from index 5 to 15
print(s)

s=ss.find("java")  #if not found return -1
print(s)
s=ss.index("java")  #if not found return error




"""


"""




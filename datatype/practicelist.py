#1)Create a list [10, 20, 30, 40, 50] and print each element using a for loop.
l1=[10, 20, 30, 40, 50]
for i in l1:
    print(i)

#2)Given l = [10, 20, 30, 40, 50], calculate the sum using a loop, without using sum().
l = [10, 20, 30, 40, 50]
total=0
for i in l:
    total +=i
print("total: ", total)

#3)Given l = [11, 20, 33, 40, 52, 67, 80], count how many numbers are even.
l = [11, 20, 33, 40, 52, 67, 80]
total=0
for i in l:
    if i%2==0:
        total+=1
print("count of  even number: ",total)

#4)Given l = [45, 12, 89, 34, 67], find the largest number without using max().
l = [45, 12, 89, 34, 67]
m=0
for i in l: 
    if i>m:
        m=i
print("max:",m)

#5)Start with l = [10, 20, 40, 50]. Insert 30 at index 2, then print the list

l = [10, 20, 40, 50]
l.insert(2,30)
print(l)


#6)Given l = [10, 20, 10, 30, 20, 40, 10], create a new list containing each number only once. Do not use set().
l = [10, 20, 10, 30, 20, 40, 10]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print("unique number:",l1)

#7)Given l = [1, 2, 3, 4, 5], print the elements in reverse order using a loop.
l = [1, 2, 3, 4, 5]
l1=[]
for i in l:
    l1.insert(0,i)
print("reverse:",l1)


#8)Find the positions of a number#
#Given l = [10, 20, 10, 30, 10, 40], find and print every index where the value 10 occurs.
l = [10, 20, 10, 30, 10, 40]
start=0
for i in range(start,len(l)):
    ind=l.index(10,start,len(l))
    start=start+1
    print(ind)
    
#9)Separate positive and negative numbers
#Given l = [10, -5, 20, -8, 0, 15, -2], create two lists: one for positive numbers and one for negative numbers. 
# Do not include 0 in either list.
l = [10, -5, 20, -8, 0, 15, -2]
pos=[]
neg=[]
for i in l:
    if i==0:
        pass
    elif i>0:
        pos.append(i)
    else:
        neg.append(i)
print("possitive",pos)
print("negative",neg)


#10Find common elements in two lists
#Given a = [10, 20, 30, 40] and b = [30, 40, 50, 60], 
#create a new list containing the common elements.
a = [10, 20, 30, 40] 
b = [30, 40, 50, 60]
same=[]
for i in a:
    for j in b:
        if i==j:
            same.append(i)
print("similar data", same)




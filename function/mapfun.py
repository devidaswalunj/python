
#3double of a number 
def doublen(x):
    return x*2
l1=[1,2,3,4,5,6]
res=list(map(doublen,l1))
print(res)

#using lambda function
l1=[1,2,3,4,5,6]
res=list(map(lambda x: x*2,l1))
print(res)

#mul of two list using lambda() function
l1=[1,2,3,4]
l2=[10,20,30,40]
res=list(map(lambda x,y: x*y,l1,l2))
print(res)
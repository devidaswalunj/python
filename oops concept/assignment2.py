class find():
    count=0
    def __init__(self):
        find.count +=1

f=find()
f1=find()
f2=find()
f3=find()
print( "total object: ",find.count)

#also print using @classmethod
class find():
    count=0
    def __init__(self):
        find.count +=1
    @classmethod
    def clamethod(cls):
        print("no of object:", find.count)

f=find()
f1=find()
f2=find()
f3=find()
find.clamethod()
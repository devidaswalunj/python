
#method overloading  using variablelength arg
class Test():
    def summ(self,*n):
        total=0
        for i in n:
            total+=i
        print("total:",total)
t=Test()
t.summ()
t.summ(10,20)
t.summ(10,20,30,50)




# #1 method overloading using default argument
# class Test:
#     def summ(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             res=a+b+c
#             print("addition: ",res)
#         elif a!=None and b!=None:
#             res=a+b
#             print("addition: ",res)
#         else:
#             print("please provide at leat 2 number")
# t=Test()
# t.summ(10,20,30)
# t.summ(10,20)
# t.summ("python", "java")
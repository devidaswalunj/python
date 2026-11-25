class Bank():
    def __init__(self):
        print("bank constructor")
    def m1(self):
        print("this is bank method")

class SBI(Bank):
    def __init__(self):
        print("this is sbi constructor")
        super().m1()
s=SBI()






# class Bank():
#     def __init__(self):
#         print("bank constructor")
#     def m1(self):
#         print("this is bank method")

# class SBI(Bank):

#     pass

# s=SBI()
# s.m1()
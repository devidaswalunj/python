class TooYoungExceptionError(Exception):
    def __init__(self,msg):
        self.msf=msg

age=int(input("enter your age: "))
if age<18:
    raise TooYoungExceptionError("your age should be 18 and above")
else:
    print("resistration succesfull")
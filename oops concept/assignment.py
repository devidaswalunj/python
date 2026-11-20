class student():
    def __init__(self,rno,name,m1,m2,m3,m4,m5):
        self.rno=rno
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def totalorpercentace(self):
        self.total=self.m1+self.m2+self.m3+self.m4+self.m4
        self.percentage=self.total/500*100
        self.grade()
        self.showdetails()
    def grade(self):
        if self.percentage>=75:
            self.a="grade a"
        elif self.percentage>=60 and  self.percentage<75:
                            self.a="grade b"
        elif self.percentage>=50 and  self.percentage<60:
                self.a="grade c"
        elif self.percentage>=40 and  self.percentage<50:
                            self.a="pass"
        else:
            self.a="fail"
        
    def showdetails(self):
            print(f"Roll no: {self.rno} name : {self.name}")
            print("total mark: ", self.total)
            print("percentage: ",self.percentage)
            print("grade:" ,self.a)
s=student(101,"ram",45,60,55,78,64)
s.totalorpercentace()
            

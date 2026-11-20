class College():
    def __init__(self):
        self.collegename="A B C"
        self.location="Pune"
        self.AcceptStudent()
        self.display()
    def AcceptStudent(self):
        
        self.rno=eval(input("enter roll number: "))
        self.name=input("enter name: ")
        self.standard=input("enter your standard: ")
        self.division=input("enter your division: ")
    def display(self):
        print(self.rno,self.name, self.standard,self.division,self.collegename, self.location)
        stu=self.student(self.rno,self.name,45,60,55,78,64)
    class student():
        def __init__(self,rno,name,m1,m2,m3,m4,m5):
            self.rno=rno
            self.name=name
            self.m1=m1
            self.m2=m2
            self.m3=m3
            self.m4=m4
            self.m5=m5
            self.totalorpercentace()
            self.grade()
            self.showdetails()
        def totalorpercentace(self):
            self.total=self.m1+self.m2+self.m3+self.m4+self.m4
            self.percentage=self.total/500*100
            
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
                


c=College()
    
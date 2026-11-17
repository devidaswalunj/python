class Student:
    def accept(self, rno, name):
        self.rno = rno
        self.name = name
        

    def show(self):
        print("Roll No: ", self.rno)
        print("Name: ", self.name)

s1 = Student()
print("s1",s1)
s1.accept(101, "Tom")
s1.show()
s2 = Student()
print("s2",s2)
s2.accept(102, "Jerry")
s2.show()
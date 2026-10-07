class home:
    def __init__(self,name,st_id,course):#__init__=>initilization
        self.name=name
        self.st_id=st_id
        self.course=course
    def info(self):
        print(f"{self.name} with id {self.st_id} is enrolled for {self.course}")
        #creation of object/instance
s1=home("ram",101,"Python")
s2=home("sitha",102,"java")
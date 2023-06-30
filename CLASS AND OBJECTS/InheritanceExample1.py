class Class1:
    def __init__(self):
        self.a=1
        self.b=11
    def showData(self):
        print(self.a,self.b)
class Class2(Class1):
    def __init__(self):
        self.c=2
        self.d=22
        super().__init__()
    # def showData(self):
    #     print(self.c,self.d)
    #     # super().showData()
class Class4(Class1):
    def __init__(self):
        self.g=4
        self.h=44
        super().__init__()
    # def showData(self):
    #     print(self.g,self.h)
    #     # super().showData()


class Class3(Class2,Class4):
    def __init__(self):
        self.e=3
        self.f=33
        super().__init__()
        Class4.__init__(self)
    # def showData(self):
    #     print(self.e,self.f)
    # #     # super().showData()

ob3=Class3()
print(Class3.__mro__)
ob3.showData()
# Class2.showData(ob3)
# Class1.showData(ob3);

'''There are 3 types of methods we use in a class.
    1. instance methods w/c are used or call by using obj of the class.
    2. class methods w/c are used or call by using cls name and not by obj.
    3. static methods w/c have nothing to do with class or instance methods. They just
    perform some func w/c we required somewhere in the class
    '''
class Class1:
    name = "ROHIT"
    x1=0    # class variable
    y1=0    # class variable

    def __init__(self): # class constructor
        self.m=1    # instance variable
        self.n=2    # instance variable

    def setData(self,a,b):  # instance method
        print("into the instance method")
        self.m=a    # method variables
        self.n=b
    @staticmethod
    def showStatic():   # static method
        print("into the static method")

    @classmethod
    def info(cls):  # class method
        print("into class method")
        return cls.name

ob1 = Class1()  # instance of the class has been created in the form of object named as "ob1".
print(f"values using class_name:\nclass variables: {Class1.x1} {Class1.y1}\n\tinstance variables: {ob1.m} {ob1.n}")

print(f"values using instance obj:\nclass variables: {ob1.x1},{ob1.y1}\n\tinstance variables: {ob1.m} {ob1.n}")
# ob1.x1 = 10
# Class1.x1 = 20
Class1.showStatic()
Class1.info()
# print(ob1.x1,ob1.y1,ob1.m,ob1.n,Class1.x1)

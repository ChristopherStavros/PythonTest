# class SuperBaseClass:
#     def hi(self):
#         print("You are here")

# class ClassA(SuperBaseClass):
#     pass

class ClassA:
    def hi(self):
        print("Hello")

class ClassB:
    def hi(self):
        print("Hallo")

    def another(self):
        print("In Class B")

class ClassC(ClassA, ClassB):
    pass

c = ClassC()

# Will look to first class (or it's parent class if method is not defined) and then to second class
c.hi()
c.another()
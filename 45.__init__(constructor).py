#45.__init__(constructor).py
class user:
    def __init__(self,name):
        print("call when new instance is created ")
        self.name=name
    def printall(self):
        print("Name:",self.name)
o1=user("Tutor joes") #it is the constructor so give the parameter in the object defined time given
o1.printall()
o2=user("joes")
o2.printall()
print(o1.__dict__)
print(o2.__dict__)
print(user.__dict__)

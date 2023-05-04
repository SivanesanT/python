#50.static method decorator
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdails(self):
        print("Name: ", self.name , " Age : ",self.age)

    @staticmethod
    def welcome():
        print("welcome to our institution")
s=student("siva",21)
s.printdails()
s.welcome()
s1=student("ramanathan",21)
s1.printdails()
s1.welcome()

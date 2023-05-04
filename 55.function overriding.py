"""
55.Function overriding
=> Base class la ulla function nam e aa derived class la
redefined panna athu peyar than functiuon overriding.

=>but function kulla ulla defenition mattum change pannuna athu peyarthan function
overriding.

=>derived class use panni maruna definition na parant class athulla print
pannuna kamikkalam and illa athu venuna anakku ethu call pannalum athan execute aakanuna athukku super() keywords use pannlaam.

"""
#using super keyword
class Employee:

    def workingHrs(self):
        self.hrs=50

    def printhrs(self):
        print("Total workinghrs: ", self.hrs)

class Trainee(Employee):

    def workingHrs(self):
        self.hrs=60

    def resetHrs(self):
        super().workingHrs()
employee = Employee()
employee.workingHrs()
employee.printhrs()   # run total working hrs = 50

trainee=Trainee()
trainee.workingHrs()    #ethulla ethulla ulla redefined statement than worke agum
trainee.printhrs()   # run total working hrs = 60

#reset kudutha Trainee hrs using super keyword and come answer means using printhrs means come answer is
# run total working hrs = 50
trainee.resetHrs()
trainee.printhrs()         # run total working hrs = 50



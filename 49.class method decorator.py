#49.class method decorator:-

class student:

    count = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age
        student.count += 1

    def printdetail(self):
        print("Name: " , self.name , " Age: " , self.age)

    #in here class method means give here in cls as the total
    #and give the propertykku pathilla @classmethod use in here by the class method

    @classmethod
    def total(cls):
        return cls.count

o=student("joes",25)
o.printdetail()
a=student("Raja",45)
a.printdetail()
print("Total admission : ",student.total())
print("Total Admission:",o.total())


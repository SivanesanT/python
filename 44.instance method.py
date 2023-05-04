class student:
    name="tutor joes"
    age=25
    def printall(self,gender): #brakets la parameter also pass pannalam
        print("name:",student.name)
        print("age:",student.age)
        print("gender:",gender)
o=student()
o.printall("male")
student.printall(o,"female") #object brackets la kudukkati error varum also pass parameter


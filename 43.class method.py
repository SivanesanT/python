class student:
    name="tutor joes"
    age=25
    def printall():
        print("Name:",student.name)
        print("Age:",student.age)
student.printall()
print(student.__dict__)
print("_____________________________")
print(getattr(student,"printall"))
getattr(student,"printall")()
# getattr(student.__dict__ ['printall'])
student.__dict__ ['printall']()
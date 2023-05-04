"""
variable or data  also called atributes.
two type of the attributes callleing one is dot.type and other is method type
namma athikamma dot notation than use pannuvom in here for athu than esay
"""


class student():
    name = "Ran kumar"
    age = 25
#get attribute method

print(getattr(student,'name'))
print(getattr(student,'age'))
print("-------------------")
#not have attributes call means error varrathuku error exception in here

print(getattr(student,'gender','no such attribute found'))
print("-------------------")

#dot(.)notation type print

print(student.name)
print(student.age)
print("-------------------")

#set attr in method type
setattr (student,'name','sivanesan')
print(student.name)
setattr(student,'gender','male')
print(student.gender)
print("-------------------")
#set attr in using the dot(.) type

student.city="salem"
print(student.city)
print("------------------")

#class structure
print(student.__dict__)

print("------------------")
#delete the attripute
delattr(student,"city")
print(student.__dict__)
print("------------------")


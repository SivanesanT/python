"""=>a class is a blue print or serves as a template from which individual object are created.
   =>object is an instance of a class which consists of methods and properties
   =>int here object also called as instance class car

"""
class car():
    pass
a=10
print(type(a))
print(type(car))
swift=car()
print(isinstance(swift,car))
print(isinstance(a,int))
print(type(swift))
"""
38.types of exception.py
"""
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
print("___________________________")


print("name error exception")
try:
    print(a)
except NameError as e:
    print("A is not defined")
print("___________________________")


print("zero error exception")
try:
    print(10/0)
except ZeroDivisionError as e:
    print("denominator can't be zero")
print("___________________________")


print("value error")
try:
    a=int("joes tutor")
except ValueError as e:
    print("please enter the number")
print("___________________________")
#e podlam podamaiyum erukkalam

print("Index error exception")
try:
    a=[10,20,30,40]
    print(a[10])
except IndexError:
    print("Invalid index")
print("___________________________")


print("file not found error")
try:
    f=open("test.text")
except FileNotFoundError as e:
    print("file not found exception")
else:
    print(f.read())
print("___________________________")

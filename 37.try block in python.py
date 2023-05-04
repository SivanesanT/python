"""
37.try block in python.py

"""
try:
    a=10/0
except Exception as e:
    print(e)

print("____________________")
print("try except else in python")
try:
    a=10/25
except Exception as e:
    print(e)
else:
    print("A value is :",a)
print("__")
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A value is :", a)
print("____________________")
print("try except else and finally in python")
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A value is :", a)
finally:
    print("thanking you")
print("__")
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A value is :", a)
finally:
    print("thanking you")
print("____________________")



"""
39.Handling multiple exception.py
"""
try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print("denomination must be in the non zero only excecution for division")
except IndexError:
    print("Invalid Index")
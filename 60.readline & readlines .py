#60.readline & readlines .py
try:
    file=open("test.text","r")
    print(file.readline())
    print(file.readline(2))
    print(file.readline(5))
    print(file.readlines())
except FileNotFoundError:
    print("Error: File NOt found")
else:
    file.close()
#63.append mode.py
try:
    file=open("test.text","a")
    file.write("this is sivanesan in the IT company and he owns the sivastech ")
    file.close()
    file = open("test.text","r")
    for line in file:
        print(line)
except FileNotFoundError:
    print("Error: File NOt found")
else:
    file.close()
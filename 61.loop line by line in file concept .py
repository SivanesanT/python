#61.loop line by line in file concept .py
try:
    file=open("test.text","r") #in same location means illa na upper kuduthu erukka mathari kudukkanum
    for line in file:
        print(line)
except FileNotFoundError:
    print("Error: File NOt found")
else:
    file.close()
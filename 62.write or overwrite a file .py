#62.write or overwrite a file .py

"""
=> adding the already file means use "a"
   append mode to join next lines
=> new folder to write a something means use the "w"
   for write mode. it also use overwrite means all there are
   delete and newly write them
"""
#write mode overwrite
try:
    file=open("test.text","w")
    file.write("this is stantly from sivanesan guide")
    file.close()
    file=open("test.text","r")
    for line in file:
        print(line)
except FileNotFoundError:
    print("Error: File NOt found")
else:
    file.close()





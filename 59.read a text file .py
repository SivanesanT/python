#59.read a text file .py
"""
file handling:
two type file:
   =>text and of file
   =>Bainary mode of file
simply name only but. is in another location means. navitgate them to the file


"""
#file = open(D:\\joes\\joestutor.txt")in another location means

try:
    file=open("test.text","r") #in same location means illa na upper kuduthu erukka mathari kudukkanum
    print(file.read())
except FileNotFoundError:
    print("Error: File NOt found")
else:
    file.close()
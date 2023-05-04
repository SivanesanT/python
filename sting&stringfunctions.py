# string and string functions
s="tutor Joes"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("t"))
print(s.endswith("ed"))
print(s.endswith("es"))
print(s.find("o"))
print(s.find("o",5)) #5 index sukku mella ulla adatha sollum list means use the aray wise
print(s.replace("o",'0'))

a='joes123'
print(type(a))
print("Is upper: ",a.isupper())
print("Is small: ",a.islower())
print("Is alpha numeric: ",a.isalnum())
print("Is alpha: ",a.isalpha())


s="he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))

a="tutor Joes computer Education"
print(a.split(" "))
a="Tutor, joes, computer, education"
print(a.split(","))

s="    joes   "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s="12-03-2020"
print(s.split("-"))
print(s.partition("-"))
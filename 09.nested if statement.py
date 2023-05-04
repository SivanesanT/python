"""
09.nested if statement.py
3 marks as input
total
average
result

if pass grade
90-100 A grade
80-89  B grade
70-79  c Grade
else D Grade
"""
m1 = int(input("enter a marke1: "))
m2 = int(input("enter a marke2: "))
m3 = int(input("enter a marke3: "))

total=m1+m2+m3
average=total/3

print("Total is:" , total)
print("Average is:" , average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("your are pass")
    if average >= 90 and average <= 100:
        print("your are a A Grade")
    elif average >= 80 and average <= 89:
        print("your are a B Grade")
    elif average >= 70 and average <= 79:
        print("your are a C Grade")
    else:
        print("your are a D Grade")
else:
    print("your are fail so no grade")

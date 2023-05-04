"""
07. if else statement.py

write a program to check vote eligibility by enter his/her name and age

"""
name=input("enter your name: ")
age=int(input("enter your age: "))

if (age>=18):
    print(name, "age is ",age,"eligible for vote")
else:
    print(name, "age is ", age, "not eligible for vote")
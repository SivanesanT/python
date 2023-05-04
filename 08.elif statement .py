"""
08.elif statement .py
days    fine amount for days
1-5        0.5
5-10        1
10-30      5
>30        member ship canceld
"""
name=input("enter your name:")
late=int(input("number of days late to submit a book:"))
if late==0:
    print(name, "very good ! you have no fine")
elif late>=1 and late<=5:
    print(name, "your fine amount is : ", late*0.5)
elif late>5 and late<=10:
    print(name, "your fine amount is : ", late*1)
elif late>10 and late<=30:
    print(name, "your fine amount is : ", late*5)
else:
    print(name, "your membership is canceled")
"""
33.recursive function.py
oru function oru work mudikka thannna thanee call panuna athu than
recursive function
factorial(5)
5*factorail(4)
5*4*factorail(3)
5*4*3*factorail(2)
5*4*3*2*1
"""
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
"""
factorial(5)
5*factorail(4)
5*4*factorail(3)
5*4*3*factorail(2)
5*4*3*2*1
"""
a=int(input("enter the you want of the factorial number:"))
print("factorial:",factorial(a))
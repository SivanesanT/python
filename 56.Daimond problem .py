#56.Daimond problem .py

"""
daimond problem means and how to solve in python

A ooda property ya B and C acess  and D yoda property ya D access it

   => oru function call pannum pothu first D la erukkunum pakkkum
   (C,D) inherit means la next C la erukkanum pakkum.
   munavathu B la erukkanum paakkum. last ta A la erukkum pakkum.

"""

class A:
    def display(self):
        print("I am the display of Class A")

class B(A):
    def display(self):
        print("I am the display of Class B")

class C(A):
    def display(self):
        print("I am the display of Class C")

class D(B,C):
    def display(self):
        print("I am the display of Class D")

o=D()
o.display()

"""

oru vella D pass meanse B la ullatha print pannum.
        =>I am the Display of class B 
        
oru vella D and B pass meanse B la ullatha print pannum.
        =>I am the Display of class C 
        
oru vella D and B and C pass meanse B la ullatha print pannum.
        =>I am the Display of class A
        
"""


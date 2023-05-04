"""
54.multilevel inheritance.py
A ova property ya B yal accewss panna mudiyum and B ooda
property ya C yal access panna mudiyum ethuthan multilevel inheritance
nnu solluvom
"""
class Granfather:
    def ownHouse(self):
        print("Grand pa house")

class father(Granfather):
    def Ownbike(self):
        print("Father's bike"

class Son(father):
    def Ownbook(self):
        print("Son have a book")

o = Son()
o.ownHouse()
o.Ownbike()
o.Ownbook()

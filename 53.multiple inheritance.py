"""
53.multiple inheritance
=> multiple inheritance is a feature of object oriental concept,
 where a class can inherit properties of more than one parant class.

at a time erandu parant class property yaiyum oree child class access
pandrathu than multiple inheritance.
"""
class Father:
    def fishing(self):
        print("fishing in rivers")
    def chess(self):
        print("playing chess from father")
class Mother:
    def cooking(self):
        print("cooking a Food")
    def chess(self):
        print("playing chess from mother")
class Son(Father,Mother):
    def ride(self):
        print("Riding a Bicycle")
o = Son()
o.fishing()
o.cooking()
o.ride()
"""
erandulaiyum oree function vantha entha function {Son(Father,Mother)}
athu first la athu inherit panni erukko athan aduthu print pannum 
inhere father than first inherit panni erukku so come answer is the 
playing chess form father.playing chess from father

like this as  {Son(MOther,Father)} meanse come the answer is playing chess from mother
"""
o.chess()

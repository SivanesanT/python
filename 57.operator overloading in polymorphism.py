#57.operator overloading in polymorphism.py
a=10
b=20
print(a+b)
a="Totor"
b="joes"
print(a+b)
"""
magic methods used to correct this
magic methods:-
--------------
__add__, __ sub__, moduls, multiply,Division ,floorDivision
and etc.... like a Many operator are haven. like 
   Operator Magic method
+   __add__(self, other)
-   __sub__(self,other)
*   __mul__(self,other)
/   __truediv__(self,other)
//  __floordiv__(self,other)
%   __mod__(self,other)
**  __pow__(self,other)
<<  __lshift__(self,other)
>>  __rshift__(self,other)
&   __and__(self,other)
|   __or__(self,other)
^   __xor__(self,other)
----------------------------

      Comparision operators:
      
   Operator Magic method
<   __LT__(self,Other)
>   __GT__(self,other)
<=  __LE__(self,other)
>=  __GE__(self,other)
==  __EQ__(self,other)
!=  __NE__(self,other)
--------------------------------

            Assignment Operators:
      
   Operator Magic method
   
-=  __ISUB__(self,other)
+=  __IADD__(self,other)
*=  __IMUL__(self,other)
/=  __IDIV__(self,other)
//= __IFLOORDIV__(self,other)
%=  __IMOD__(self,other)
**=  __IPOW__(self,other)
>>=  __IRSHIFT__(self,other)
<<=  __ILSHIFT__(self,other)
&=  __IAND__(self,other)
!=  __IOR__(self,other)
^=  __IXOR__(self,other)
--------------------------

                Unary OPerators:
         Operator Magic method
-          __NEG__(self,other)
+          __POS__(self,other)
~          __INVERT__(self,other)
"""
#inbulit methods as __add__ and __sub__ that catch the +- and etc..
class addition:
    def __init__(self,a):
        self.a=a

    def __add__(o1, o2):
        return o1.a+o2.a

    def __sub__(o1,o2):
        return o1.a-o2.a

o1=addition(30)
o2=addition(20)
print("Total:", (o1+o2))
print("Difference:", (o1-o2)


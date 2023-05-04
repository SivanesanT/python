"""
18.tuple.py

tuple in python
immutable  (not changed change  meanse list convert and change it)
surr4ounded by round brackets
"""
a=(1,2.5,True,"Ram")
print(type(a))
print(a)
print(a[0])
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append("raja")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)
if "raja" in a:
    print("Raja is found")
else:
    print("NOt found")

if "raj" in a:
    print("Raja is found")
else:
    print("NOt found")
print(len(a))
a=(1)
print(type(a))
a=(1,)
print(type(a))
del a
#print(a)
x=(1,2,3,4)
y=(5,6,7,8)
z=x+y
print(z)
print(z.count(5))

#Nested tuple
a=(1,2,7,4)
b=(5,6,7,8)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][2])
x=('joes',)*10
print(x)
a=(1,2,7,4)
print(min(a))
print(max(a))
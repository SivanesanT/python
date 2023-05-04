"""
21.identity operators.py
=>is
=>isnot
"""
a=[1,2]
b=[1,2]
c=a
print(id(a))
print(id(c))
print(id(b))

print(a is c)
print(a is b)
# id also equl means only come true in (a is b)
print(a==b)

print(a is not c)
# id also equl means only come false in( a is not b)
print(a is not b)
print(a!=b)

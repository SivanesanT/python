"""
#19.set  & its functions.py
collection of unorder and unidexed datatype
(values ordered daa erukkathu)
set in {}
"""
name={'ram','sam','ravi'}
print(name)
print(type(name))
#access values using for loop
for a in name:
    print(a)
    #( enga values sa change panna mudiyathu add and remove only the value change pannamudiyathu)
#adding new element
name.add('sara')
print(name)

#update another set of data
a={'kumar','sundar','suresh'}
name.update(a)
print(name)
name.remove('sara')
print(name)
#remove use pannuna antha name illadi error varum but discard la apdi illa
#in here name illa di error varathu
name.discard('sara')
print(name)
name.discard('kumar')
print(name)
#in here antha value venunalum pop agum
name.pop()
print(name)
name.clear()
print(name)
del name
# print(name)
print("--------------------------------")
names={'ram','sam','ravi','kumar','sundar','suresh'}
print(names)
#ore name aa rendu vadi kuduthallum oru  vadi than execute agum
names={'ram','sam','ravi','ravi','kumar','sundar','suresh'}
print(names)
print("--------------------------------")
#union intersection

a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)
#b la ulla value va a la update pannidum and a la ulla value delete agi a la union value stored agum
a.update(b)
print(a)
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
#intersection value va a la send pannum and palaiya value delete agidum
a.intersection_update(b)
print(a)
# semmetric deference
#b la ulla value and not in intersection
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.isdisjoint(b)
#ethu rendum joint illa yanu kekkurom
print(c)
# a la erukkurathu b la eruntha subsetat denote by the position of given
c=a.issubset(b)
print(c)
# b la erukkurathu a la eruntha supperset at denote by the position of given
c=a.issuperset(b)
print(c)
a={5,6,7,8,9}
b={5,6,7}
c=a.issuperset(b)
print(c)

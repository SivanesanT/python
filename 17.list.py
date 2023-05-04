"""
17. list.py
  sequence type
  mutable (values can change)
a[5]
a=[1,2,3,4,5]
a[0]
[]
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)


print("..............slicing...........")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[:2])
print(a[:3])
print("----------------")


a=[1,True,'ram',2.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print(a[4][1])
print("-------")

a=[10,24,35,45]
print(a)
a.clear()
print(a)

c=[10,24,35,66]
b = c.copy()
print(b)

d=[10,25,45,25,4,25]
print(d.count(25))
print(d.index(25))  #first occurence only come
print(len(d))
print(max(d))
print(min(d))
print(d)
d.pop(0) #pop first value
print(d)

a=[10,24,35,45,25,4,25] # only one only deleted
a.remove(25)
print(a)
print("_+_+_+_+_+__+__+_)_((&&!@#$%^&*()")
names=["ram"]
print(names)
names.append("sam")
names.append("kumar")
names.append("santhos")
names.append("ramesh")
print(names)
name2=["sara","anitha"]
names.extend(name2)
print(names)

names.insert(1,"suriya")
print(names)
print("-----------")


#list type constructors
print(list(range(5)))
print(list("sivanesan"))
print("-----------")

a=[100,5,10,25,10,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print("-------------------")
a=["Orange","Apple","zebra"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a=["Orange","Apple","zebra"]
a.sort(key=len)
print(a)




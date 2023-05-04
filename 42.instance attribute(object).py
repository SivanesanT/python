"""
in the class () brakets podalam podamaiyum erukkalam
instance has also store the datas
Thu apdi print agum na class attr la data eruntha atha kamikkum illana instance attr la ullatha kamikkum
instantce also store the datasa
"""
class user:
    course='java'
o=user()
print(user.__dict__)
print(user.course)
print(o.__dict__)
print(o.course)
o.course="c++" #like this only give value for the instance
print(o.__dict__)
print(o.course)#namma instance value set pannathu nalla antha value of the c++ only come
o2=user()
print(o2.course)#inhere there is no instance of the value so come the value of the class attrs val;ue of "java"



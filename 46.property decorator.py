class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.msg = self.name + " is " + str(self.age) + " years old"
    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old "

o = user('sivanesan', 25)
print(o.name)
print(o.age)
print(o.msg)
o.age = 45 #in here there normal init function there is no change of printing so only use the property
print(o.msg) #in here there is come answer is sivanesan is 25 years old only ont change here

"""
use them at print(o.msg()) nnuu use pannuna not error and come answer 
give answer at the sivanesan is 45 years old come correctly
alla edathullaiyum poi matha mudiyathu so we use them at the above of 
function give the @property means come answer correctly  
"""

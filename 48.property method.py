#property method

class student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5.0

    # enga there is property nnu kela kuduthu athulla allame geeter and setter nu kuduthuruvom athunnalla
    # athunalla @total.setter runna illa na @property nou kudukka thevai illa

    def getter(self):
        return self._total

#enga there is property nnu kela kuduthu athulla allame geeter and setter nu kuduthuruvom athunnalla
#athunalla @total.setter runna illa na @property nou kudukka thevai illa
    def setter(self, t):
        if t<0 or t>500:
            print("Invalid total and can't change")
        else:
            self._total = t
    #enga allathukkum sethu getter and setter use pannikkalam for using another method
    #alternative method  of the property decorator getter and setter
    total=property(getter,setter)
o = student(450)
print("total:", o.total)
print("Average:", o.average())
o.total = 350
print("total:", o.total)
print("Average:", o.average())
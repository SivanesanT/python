#47.property decorator getter and setter.py
"""
class student:
    def __init__(self,total):
        self.total=total
    def average(self):
        return self.total/5.0
o=student(450)
print("total:",o.total)
print("Average:",o.average())
total=250
print("total:",o.total)
print("Average:",o.average())

run:
   total: 450
Average: 90.0
total: 450
Average: 90.0
 but it is not secure for the outer of the class can use it
 so we can use the private(_)

   like this give means not secure in geter seter so only use the private valriable
   it is used to outer of the class not use the variable in python there is (_) this symbol
   is the delace the variable as the private it denote

"""

"""
class student:
    def __init__(self,total):
        self._total=total
    def average(self):
        return self._total/5.0
    
o=student(450)
print("total:",o.total)
print("Average:",o.average())
total=250
print("total:",o.total)
print("Average:",o.average())


in here there is error:-
 Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\plugins\python-ce\helpers\pydev\_pydev_bundle\pydev_umd.py", line 198, in runfile
    pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\plugins\python-ce\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
    
AttributeError: 'student' object has no attribute 'total'
  
      it is the error for them is private ta errukku etha velila use panna mudiyathu and set new is not  
so we use the property decorator getter and setter
"""


class student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5.0

    #enga adikkadi ovvaru function sa na call in the run time is not good so give here @property
    @property
    def total(self):
        return self._total

    #enga total la set panna mudiyathu so use the @total.setter
    @total.setter
    def total(self, t):
        if t<0 or t>500:
            print("Invalid total and can't change")
        else:
            self._total = t


    # def total(self,t):
    #     self._total=t enga oru condition naiyum check panni kudukkalam

o = student(450)
print("total:", o.total)
print("Average:", o.average())
o.total = 350
print("total:", o.total)
print("Average:", o.average())
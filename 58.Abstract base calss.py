#58.Abstract base class.py
"""
=>ethu annana oru set of rules create panni athavassu alla class sum emplemet
aakannum soltrathu than abstract base class
abc means abstract base class

=>oru class la ABC inherit import pannuna athu abstract class la akitum
=>ABC of class a function Name. only have not for definition inner of
ABC class
=>alla function saiyum inherit class use panni erukkanum when
@abstract method used.
main class la kudukkuratha sub class la redefin panni erukkanum kandippa
"""
from abc import ABC, abstractmethod

# use this means only come answer abc means abstract class

class Bank(ABC):

    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def credit(self):
        pass

    @abstractmethod
    def debit(self):
        pass


class HDFC(Bank):
    def loan(self):
        print("we can provide 7.5% Interest loan")

    def credit(self):
        print("HDFC provide Credit")

    def debit(self):
        print("HDFC provide debit cards")

    def card(self):
        print("HDFC provide Card")

o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()
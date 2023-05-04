#single inheritance.py
"""
=>inheritance is a process in which one object acquires autyomatically
=>single inheritance is defined as the inheritance in which a derived class in inherited from the only one base class
=>oru class la ulla property and function ennoru class mulymaka access pandrathu than inheritance.

"""
class Nokia:
    company="Nokia India"
    website="www.nokia-india.com"

    def contact_details(self):
        print("address: cherry road,near salem")

class Nokia110(Nokia):

    def __init__(self):
        self.name="Nokia 110"
        self.year=1998

    def product_details(self):
        print("Name: ",self.name)
        print("year: ",self.year)
        print("company: ",self.company)
        print("website: ",self.website)

mobile=Nokia110()
mobile.product_details()
mobile.contact_details()
"""
oru class la ulla property ya ennoru class la access pannurathu than 
inheritance"""
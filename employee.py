"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, dict):
        self.name = name
        self.dict = dict

    def ismonthly(self):
        monthly = False
        if 'monthly' in self.dict.keys():
            monthly = True
        return monthly
    
    def salary(self):
        salary = self.dict['monthly']
        return salary
    
    def ishourly(self):
        hourly = False
        if 'hourly' in self.dict.keys():
            hourly = True
        return hourly
    
    def numofhours(self):
        numofhours = self.dict['hourly']
        return numofhours
    
    def hourlyprice(self):
        hourlyprice = self.dict['price']
        return hourlyprice
    
    def hoursalary(self):
        money = self.numofhours() * self.hourlyprice()
        return money

    def hasCcomm(self):
        hasCcomm = False
        if 'contracts' in self.dict.keys():
            hasCcomm = True
        return hasCcomm
    
    def numofcontracts(self):
        numofcontracts = self.dict['contracts']
        return numofcontracts
    
    def contcomm(self):
        contcomm = self.dict['commprice']
        return contcomm
    
    def hasbonus(self):
        hasbonus = False
        if 'bonus' in self.dict.keys():
            hasbonus = True
        return hasbonus
    
    def bonuscomm(self):
        bonuscomm = self.dict['bonus']
        return bonuscomm

    def commvalue(self):
        money = 0
        if self.hasCcomm():
            money = self.numofcontracts() * self.contcomm()
        
        elif self.hasbonus():
            money = self.bonuscomm()
        
        return money
    
    def get_pay(self):
        total_pay = 0

        if self.ismonthly():
            total_pay = self.salary() + self.commvalue()
        elif self.ishourly():
            total_pay = self.hoursalary() + self.commvalue()

        return total_pay

    def commstatement(self):
        commst = ""

        if self.hasCcomm():
            commst = " and receives a commisson for " + str(self.numofcontracts()) + " contract(s) at " + str(self.contcomm()) + "/contract"
        
        elif self.hasbonus():
            commst = " and receives a bonus commission of " + str(self.bonuscomm()) 
        
        return commst

    def __str__(self):
        statement = self.name + " works on a "
        totalst = ".  Their total pay is " + str(self.get_pay()) + "."

        if self.ismonthly():
            statement += "monthly salary of " + str(self.salary()) + self.commstatement() + totalst
        elif self.ishourly():
            statement += "contract of " + str(self.numofhours()) + " hours at " + str(self.hourlyprice()) + "/hour" + self.commstatement() + totalst

        return statement


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', {'monthly':4000})

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', {'hourly':100, 'price':25})

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', {'monthly':3000, 'contracts': 4, 'commprice': 200})

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', {'hourly':150, 'price':25, 'contracts': 3, 'commprice': 220})

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', {'monthly':2000, 'bonus': 1500})

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', {'hourly':120, 'price':30, 'bonus': 600})
class car: #parent class
    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def mileage (self):
        print("Mileage of this car is ")

c=car("Solid","V12","CEAT")
print(c)

class Tata(car):#inheritance #child class
    pass

t= Tata("Matte","V8","Pirelli")
#print(t.engine)



#remove the comment to make it work
"""Multi level Inheritance"""

"""class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you account open status ")
    def deposit(self):
        print("This will show your deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("This will show you all the transaction to icici through hdfc")

#if we are calling hdfc the main is already linked if you call hdfc main will come with it

class ICICI_bank(HDFC_bank):
    pass
i=ICICI_bank()
i.hdfc_to_icici()
i.deposit()
i.transaction()
i.account_opening()"""



"""Multiple Inheritance"""

class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show you account open status ")
    def deposit(self):
        print("This will show your deposited amount")
    def test(self):
        print("This is a test method from bank")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("This will show you all the transaction to icici through hdfc")
    def test(self):
        print("This is a test method from HDFC bank")

class REXA_bank:
    def rexa_account_status(self):
        print("Print an account status in icici")

class ICICI_bank(bank,HDFC_bank,REXA_bank): #muleiple inheritance at once
    pass

i=ICICI_bank()
i.hdfc_to_icici()
i.deposit()
i.transaction()
i.account_opening()
i.rexa_account_status()
i.test() #it will give Output based on priority in class first there is bank then Hdfc so output would be from bank only


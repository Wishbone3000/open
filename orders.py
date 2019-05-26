from datetime import date
import random
import string

class Orders: 
    # Orders should be called after Person and Offers
    orderid  = 0 
    

    
    def __init__(self, PersonID=999, OfferID=999):
        self.Order_ID = self.get_orderID()
        self.Person_ID = PersonID
        self.SKU = self.getsku()
        self.Quantity = self.getquantity()
        self.Amount = self.getamount()
        self.Date = self.getdate()
        self.Offer_ID = OfferID

    def get_orderID(self):
        self.__class__.orderid += 1
        return self.__class__.orderid

    def getsku(self):
        return random.randint(100,900).join(random.sample(string.ascii_letters,3))
    
    def getquantity(self):
        return random.randint(1,59)

    def getamount(self):
        return random.randrange(12.00,125.00)
        random.
    def getdate(self):
        return date.today()

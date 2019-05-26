import random
from datetime import date   

class Person:

    def __init__(self):
        self.Gender = self.get_gender()
        self.FirstName = self.get_firstname()
        self.LastName = self.get_lastname()
        self.Birthdate = self.get_birthdate()

    def get_birthdate(self):
        #generate random birthdate 
        month = random.randint(1,12)
        #for now just do 28 days....
        day = random.randint(1,28)
        # simple hack lets say 19-80 (1939-)
        year = random.randint(1939,2000)
        return date(month,day,year)

    def get_gender(self):
        if random.randint(0,1) == 0:
            return('F')
        else:
            return('M')


    def get_firstname(self): 
        # for now just some values
        mens =  ['Jeff','Steve','Larry','Mike','Sergio','Juan']
        womens = ['Susan','Jennifer','Mary','Barb','Anna','Liz']
        
        if self.Gender == 'M':
            return mens[random.randint(0,5)]
        else: 
            return womens[random.randint(0,5)]

    def get_lastname(self):   
        last = ['Smith','Jones','Gupta','Garcia','Johnson', 'Chang']
        return last[random.randint(0,5)]

import collections
class lst(list): 
    def push(self, something): 
        super().append(something)
class order:
    def __init__ (self, token, time, quantity, price):
        self.token = token 
        self.time = time 
        self.quantity = quantity
        self.price = price
def getBalance(): 
    
    return 0;
class Msg: 
    def __init__ (self, sender, customer, value ): 
        self.customer = customer
        self.sender = sender
        self.value = value 
        ownerToBalance[customer] -= value

def getSumToken(totalToken): 
    sum=0
    if type(totalToken) is not lst: 
        for x in totalToken.keys(): 
            sum+= totalToken[x]
    else: 
        for x in totalToken:
            sum+= x.quantity
    return sum
def sendtoken(_token, _quantity): 
    totalToken[_token]-=_quantity
def convert(lstOfTuple): 
    l =lst()
    for x in lstOfTuple: 
        i = order(x[0], x[1], x[2],x[3])
        l.push(i)
    return l
class Address: 
    
    def __init__ (self, adr): 
        self.adr = adr 
        self.balance = ownerToBalance[self.adr]
    def transfer(self, amount ):    
        ownerToBalance[self.adr]+= amount
        ownerToBalance['0x0000']-=amount
class base: 
    def address(self,adr): 
        return Address(adr)
    def require(self,something, str="None"): 
        pass

now = None
this  ='0x0000'

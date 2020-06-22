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
admin="0xAb076e2f130e7Da2985B99a2b5Ce5af6cc34f82e"
user_address="0x7De8d441fBb7a6868D3ce81eE26d1Fc0868E8761"
totalToken={'123456798': 3, 'physics': 12, 'computer': 5}
ownerToOrderList = collections.defaultdict(lambda : 0)
ownerToOrderList[user_address]=[(123456789, 1591968279, 2, 100000000000000000), (123456789, 1591968294, 3, 200000000000000000), (987654321, 1591968339, 1, 150000000000000000), (123456798, 1591968714, 1, 100000000000000000), (123456798, 1591974594, 1, 100000000000000000), (123456798, 1591974834, 1, 100000000000000000), (123456798, 1591975104, 1, 100000000000000000), (123456798, 1591975164, 1, 100000000000000000), (123456798, 1591975254, 1, 100000000000000000), (123456798, 1591975434, 1, 100000000000000000), (123456798, 1591976424, 1, 100000000000000000), (123456798, 1591976529, 1, 100000000000000000), (123456798, 1591979574, 1, 100000000000000000), (123456798, 1591980354, 1, 100000000000000000), (123456798, 1591980414, 1, 100000000000000000), (123456798, 1591987614, 1, 100000000000000000), (123456798, 1591989564, 1, 100000000000000000), (123456798, 1591989759, 1, 100000000000000000), (123456798, 1591990494, 1, 100000000000000000), (123456798, 1591990644, 1, 100000000000000000), (123456798, 1592023359, 1, 100000000000000000), (123456798, 1592047704, 1, 100000000000000000), (123456798, 1592048484, 1, 100000000000000000), (123456798, 1592052459, 1, 100000000000000000), (123456798, 1592052714, 1, 100000000000000000), (123456798, 1592060559, 1, 100000000000000000), (123456798, 1592061639, 1, 100000000000000000)]
ownerToOrderList[user_address]=convert(ownerToOrderList[user_address])
ownerToBalance= collections.defaultdict(lambda : 0)
ownerToBalance[admin]=12707164760000000000
ownerToBalance[user_address]=35295134373000000000
ownerToBalance['0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De']=1200000000000000000
book_quantity=1
book_price=1e+17
book_isbn="123456798"
msg = Msg(admin, user_address, book_price*book_quantity)
ownerToBalance['0x0000'] = msg.value
class Ownable(base):
	_owner=None
	incognitoAddress="0xcAd4954fA4cb431bAD9a84c3ae8e279fe069A6De"
	def __init__(self):
		Ownable._owner=msg.sender
	def owner(self):
		return Ownable._owner
	def isOwner(self):
		return msg.sender==Ownable._owner
	def renounceOwnership(self):
		Ownable._owner=self.address(0)
	def transferOwnership(self,newOwner):
		self._transferOwnership(newOwner)
	def _transferOwnership(self,newOwner):
		self.require(newOwner!=self.address(0))
		Ownable._owner=newOwner
class BookStoreInit(Ownable):
	def withdraw(self):
		self._owner=self.owner()
		self.address(self._owner).transfer(self.address(this).balance)
	def SendToken(self,_to,_token,_ether_amount,_quantity):
		sendtoken(_token,_quantity)
		ownerToOrderList[_to].push(order(_token,now,_quantity,_ether_amount))
class BookStore(BookStoreInit):
	def implementTransaction(self,_from,_token,_quantity):
		self.require(msg.sender==_from,'Invalid transaction')
		self.withdraw()
		self.SendToken(_from,_token,msg.value,_quantity)
	def getOrderHistory(self,_user):
		self.result=[]
		self.result=ownerToOrderList[_user]
		return self.result
	def getBalance(self):
		return self.address(this).balance

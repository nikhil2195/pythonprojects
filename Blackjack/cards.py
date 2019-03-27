ranks=('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
values = {'Ace':11,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}
suits=('Spades','Hearts','Clubs','Diamonds')


class Cards:
	"""docstring for ClassName"""
	def __init__(self, rank,value,suit):

		self.rank = rank
		self.suit = suit
		self.value = value
		self.name=rank+' of '+suit


	def get_name(self):
		return(self.name)

	def print_name(self):
		print(self.name)



def build_deck():

	deck=[]

	for suit in suits:
		for rank,value in values.items():
			deck.append(Cards(rank,value,suit))

	return deck




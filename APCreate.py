import sys

class Card():
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def PrintCard(self):
		print ' ___________ '
		print '|           |'
		print '|           |'
		print '|   '+str(self.value)+'      |'
		print '|   '+str(self.suit)+'     |'
		print '|           |'
		print '|           |'
		print '|           |'
		print ' ___________ '

king = Card(13, 'red')

king.PrintCard()

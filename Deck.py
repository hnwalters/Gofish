#Hayden N. Walters
#import pdb; pdb.set_trace()
from random import shuffle

class Card(object):
    
    def __init__(self, number, suit):
        self._number = number
        self._suit = suit
        
    def __str__(self):        
        return "{0} of {1}".format(self.value(), self._suit)

    def __eq__(self, other):
        return self._number == other._number
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return self._number < other._number
    
    def __le__(self, other):
        return (self < other) or (self == other)
    
    def __gt__(self, other):
        return self._number > other._number
    
    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def number(self):
        return self._number
    
    def value(self):
        words = {2:"Two", 3:"Three", 4:"Four", 5:"Five",\
             6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",\
             10:"Ten", 11:"Jack", 12:"Queen", 13:"King",\
             14:"Ace"}
    
        return words[self._number]
        
class Deck(object):

    def __init__(self, ):
        self._deck = []
        suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        for num in range(2, 14):
            for suit in suits:
                self._deck.append(Card(num, suit)) 
                
        self.shuffle()
    
    def shuffle(self):
        shuffle(self._deck)
        
    def deal(self):
        return self._deck.pop(0)
    
    def __len__(self):
        return len(self._deck)
    
    def __str__(self):
        return self._deck  
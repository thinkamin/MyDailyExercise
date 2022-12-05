from collections import namedtuple

Card = namedtuple('Card',['color','number'])

class Jokes():
    colors = 'spades diamonds clubs hearts'.split()
    numbers = [str(n) for n in range(2,11)]+list('FQKA') 
    def __init__(self):
        self._cards = [Card(color,number) for color in self.colors for number in self.numbers]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]



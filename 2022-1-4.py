from collections import namedtuple
import random
Card = namedtuple('card','color num')

class Cards:
    colors = ['hongtao','heitao','fangpian','meihua']
    nums = list(range(2,11))+['A','J','Q','K']
    print(nums)
    def __init__(self):
        self.cards = [Card(color,num)  
                for color in self.colors
                for num in self.nums]
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)
    def __getitem__(self,position):
        return self.cards[position]

ex = Cards()
print(len(ex))
print(ex[1])


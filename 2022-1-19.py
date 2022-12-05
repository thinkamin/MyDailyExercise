import random
from my import gen_num
from collections import namedtuple

Card = namedtuple('Card','color num')

class Puck:
    colors = ['hongtao','heitao','fangpian','meihua']
    nums = list(range(2,10))+list('AJQK')
    def __init__(self):
        self.Cards = [Card(color,num)
                for color in self.colors
                for num in self.nums]
    def __len__(self):
        return len(self.Cards)
    def __getitem__(self,position):
        return self.Cards[position]

A = Puck()
print(len(A))
print(A[0])




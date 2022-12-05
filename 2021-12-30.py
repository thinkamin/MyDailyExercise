# from my import gen_num
from collections import namedtuple
# num_lst = gen_num()

Card = namedtuple('card','color number')
# a = 'a b c'.split()
# print(a)
class Cards:
    colors = ['hongtao','meihua','fangkuai','heitao']
    numbers = list(range(2,10))+'A J Q K'.split()
    def __init__(self):
        self.Card_lst = [Card(color,num)
                for color in self.colors
                for num in self.numbers]
    def __len__(self):
        return len(self.Card_lst)
    def __getitem__(self,position):
        return self.Card_lst[position]


cards = Cards()
for i in range(10):
    print(cards[i])
print(len(cards))


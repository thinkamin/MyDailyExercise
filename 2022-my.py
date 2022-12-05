#from my import G1,G2
#from collections import deque
import random

def gen_num(n=10):
    num_lst = [random.randint(0,10) for i in range(n)]
    print('原始数据')
    return num_lst


def G1():
    print("""
            A--B--C
            |\ | 
            D  E
            """)
    G1 = {
            'A':['B','E','D'],
            'B':['A','C'],
            'C':['B'],
            'D':['A'],
            'E':['A','B']
            }
    return G1


def G2():
    print("""
            A-1-B-1-C
            |   |   |
            2   2   10
            |   |   |
            F-10-E-1-D  
            """)
    G2 = {
            'A':{'B':1,'F':2},
            'B':{'A':1,'C':1,'E':2},
            'C':{'B':1,'D':10},
            'D':{'C':10,'E':1},
            'E':{'D':1,'C':10,'B':2},
            'F':{'E':10,'A':2}
            } 
    return G2




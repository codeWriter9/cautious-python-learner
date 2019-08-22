'''
Created on 20-Aug-2019

@author: Sanjay Ghosh
'''
from itertools import combinations_with_replacement;
_str, _k = input().split();
k = int(_k);
for t in combinations_with_replacement(sorted(_str), k):
    print("".join(t));
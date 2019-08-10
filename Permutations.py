'''
Created on 04-Jul-2019

@author: Sanjay Ghosh
'''
from itertools import permutations;
arr = input().split();
_str_ = arr[0];
num = int(arr[1]);
for perm in sorted(list(permutations(_str_, num))):
    print("".join(perm));
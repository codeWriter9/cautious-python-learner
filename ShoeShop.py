'''
Created on 08-Jun-2019

@author: Sanjay Ghosh
'''
from collections import Counter;
sumCount = 0;
ncust = int(input());
arr = [int(size) for size in input().split(" ")];
_dict_ = Counter(arr);
sizeToPrice = [];
T = int(input());
for customers in range(0, T):
    sizeToPrice.append(tuple(map(lambda x : int(x), list(input().split(" ")))));
for myTuple in sizeToPrice:
    if _dict_[myTuple[0]]: # only if we have the shoe size left
        sumCount = sumCount + myTuple[1];
        _dict_[myTuple[0]] = _dict_[myTuple[0]] - 1;
print(sumCount); 
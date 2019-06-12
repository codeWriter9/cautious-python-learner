'''
Created on 11-Jun-2019

@author: Sanjay Ghosh
'''
from itertools import combinations;
number = int(input());
arr = input().split();
k = int(input());
count = 0;
total = 0;
for tuple_ in combinations(arr, k):
    if 'a' in tuple_:
        count += 1;
    total += 1;
print(round(count/total, 4));
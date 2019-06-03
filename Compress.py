'''
Created on 02-Jun-2019

@author: Sanjay Ghosh
'''
from itertools import groupby;
numbers = [int(ch) for ch in input()];
groups = [];
for k, g in groupby(numbers, None):
    groups.append(str((len(list(g)), k)));      # Store group iterator as a list    
print(" ".join(groups));
'''
Created on 11-Aug-2019

@author: Sanjay Ghosh
'''
import operator;
N, K = map(int, input().split());
l = [];
for x in range(N):
    l.append(tuple(map(int, input().split())));
K = int(input());
l.sort(key = operator.itemgetter(K));
for x in l:    
    print(" ".join(map(str, x)));     
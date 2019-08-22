'''
Created on 17-Aug-2019

@author: Sanjay Ghosh
'''
T = int(input());
set1 = set(map(int, input().split()));
R = int(input());
set2 = set(map(int, input().split()));
c1 = set(set1.difference(set2));
c2 = set(set2.difference(set1));
c = c1.union(c2);
l = list(c);
l.sort();
print("\r\n".join(map(str, l)));
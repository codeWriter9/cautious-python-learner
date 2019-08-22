'''
Created on 07-Jul-2019

@author: Sanjay Ghosh
'''
import re;
pattern = re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$");
l, r = [], [];
for x in range(int(input())):
    l.append(input());
r = list(filter(pattern.match, l));
print(r);
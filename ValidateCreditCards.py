'''
Created on 05-Jun-2019

@author: Sanjay Ghosh
'''
import re;

def checkValid(m):
    if m:
        print(m.span());
    return "Valid" if m != None else "Invalid";


pattern = re.compile("([abc]b){2}", re.DEBUG);
T = int(input());
while T :
    print(checkValid(pattern.match(input())));
    T = T -1;
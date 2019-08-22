'''
Created on 21-Aug-2019

@author: Sanjay Ghosh
'''
from collections import deque;
s = deque();
operations = int(input());
for x in range(operations):
    arr = input().split();        
    try:
        if "pop" == arr[0]:
            s.pop();
        if "popleft" == arr[0]:
            s.popleft();
        if "append" == arr[0]:
            s.append(int(arr[1]));
        if "appendleft" == arr[0]:
            s.appendleft(int(arr[1]));
    except KeyError:
        continue;
print(" ".join(map(str, s)));
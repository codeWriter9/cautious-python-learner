'''
Created on 21-Aug-2019

@author: Sanjay Ghosh
'''
n = int(input());
s = set(map(int, input().split()));
operations = int(input());
for x in range(operations):
    arr = input().split();        
    try:
        if "pop" == arr[0]:
            s.pop();
        if "remove" == arr[0]:
            s.remove(int(arr[1]));
        if "discard" == arr[0]:
            s.discard(int(arr[1]));
    except KeyError:
        continue;
print(sum(s));
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations;
_str, _num = input().split();
num = int(_num);
for n in range(1, num + 1):    
    for x in list(combinations(sorted(_str),n)):
        print("".join(x));
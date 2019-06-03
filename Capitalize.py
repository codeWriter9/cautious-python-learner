'''
Created on 20-May-2019

@author: Sanjay Ghosh
'''

def solve(s):
    a = s.split(" ");
    s = '';
    for i in range(len(a)):
        s = s + a[i][0:1].upper() + a[i][1:] + " " ; 
    return s;

if __name__ == '__main__':
    print(solve(input()));
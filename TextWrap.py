'''
Created on 12-May-2019

@author: Sanjay Ghosh
'''
import textwrap;

def wrap(string, max_width):
    s = "";
    i = 0;
    for ch in string:
        s = s + ch;
        i = i + 1;
        if i % max_width == 0 and i % max_width != 1:
            s = s + '\n';
    return s;

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result);
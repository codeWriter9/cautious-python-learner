'''
Created on 13-Sep-2020

@author: Sanjay Ghosh
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def lcs(a, b, i, j):
    if i==0 or j==0:
        return 0
    if a[i - 1] == b[j - 1]:
        return 1 + lcs(a, b, i - 1, j - 1);
    else:
        return max(lcs(a, b, i, j -1), lcs(a, b, i - 1, j))


def starter(a, b):
    print("LCS is;" + str(lcs(a, b, len(a), len(b))));
    return;

if __name__ == '__main__':
    q = int(input("Numbe of sequences for testing:"))
    for q_itr in range(q):
        a = input("Enter First Sequence:")
        b = input("Enter  2nd  Sequence:")
        result = starter(a, b)
        print();


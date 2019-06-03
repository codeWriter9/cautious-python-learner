'''
Created on 02-Jun-2019

@author: Sanjay Ghosh
'''
from itertools import product;
def input_list():
    return [int(number) for number in input().split(" ")];

print(" ".join(str(x) for x in list(product(input_list(), input_list()))));
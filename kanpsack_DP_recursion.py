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

def knapsack(knapsack_capacity, weights, values, current_item):
    # all items done or no capacity left
    if knapsack_capacity == 0 and current_item == 0:
        return 0
    # return till last item
    if knapsack_capacity < weights[current_item - 1]:
        return knapsack(knapsack_capacity, weights, values, current_item - 1)
    else:
        return max(values[current_item - 1] + knapsack(knapsack_capacity - weights[current_item - 1], weights, values, current_item - 1), knapsack(knapsack_capacity, weights, values, current_item - 1))

# Complete the abbreviation function below.
def abbreviation(knapsack_capacity, weights, values, number_of_items):
    print(knapsack(knapsack_capacity, weights, values, number_of_items));
    return 0;

if __name__ == '__main__':
    

    q = int(input())
    for q_itr in range(q):
        knapsack_capacity = int(input())
        weights = map(int, input().split())
        values = map(int, input().split())
        number_of_items = len(weights)
        result = abbreviation(knapsack_capacity, weights, values, number_of_items)
        print(result)


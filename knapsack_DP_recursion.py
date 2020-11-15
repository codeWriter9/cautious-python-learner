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
    if knapsack_capacity <= 0 or current_item <= 0:
        return 0
    # return till last item
    if knapsack_capacity < weights[current_item - 1]:
        return knapsack(knapsack_capacity, weights, values, current_item - 1)
    else:
        return max(values[current_item - 1] + knapsack(knapsack_capacity - weights[current_item - 1], weights, values, current_item - 1), knapsack(knapsack_capacity, weights, values, current_item - 1))


if __name__ == '__main__':

    number_of_iterations = int(input("Enter Number  of iterations :"))
    for iterations in range(number_of_iterations):
        knapsack_capacity = int(input("Enter Total Weight :"))
        weights = list(map(int, input("Enter individual Weights :").split()))
        values = list(map(int, input("Enter individual Values :").split()))
        number_of_items = len(weights)
        result = knapsack(knapsack_capacity, weights, values, number_of_items)
        print(result)


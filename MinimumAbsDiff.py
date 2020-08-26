import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
  arr = sorted(arr);
  for x in range(1, len(arr) - 1):
    print(" arr[ " + str(x-1) + "] = " + str(arr[x-1])); 
    print(" arr[ " + str(x) + "] = " + str(arr[x])); 
  return 0
  
  



if __name__ == '__main__':    
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(str(result) + '\n')
    

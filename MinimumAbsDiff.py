from math import fabs;
from sys import maxsize;


def minimumAbsoluteDifference(arr):
  arr = sorted(arr);
  min = maxsize;
  for x in range(1, len(arr)):
    #print(" arr[ " + str(x-1) + "] = " + str(arr[x-1])); 
    #print(" arr[ " + str(x) + "] = " + str(arr[x]));
    diff = int(fabs(arr[x] - arr[x - 1]));
    #print(" diff " + str(diff));
    if diff < min:
      min = diff 
  return min
  
  



if __name__ == '__main__':    
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(str(result) + '\n')
    

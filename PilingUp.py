'''
Created on 09-Jun-2019

@author: Sanjay Ghosh
'''
for x in range(0, int(input())):
    n_of_Cubes = int(input());
    cubes = list(map(int, input().split()));    
    index = 0;
    while index < n_of_Cubes - 1 and cubes[index] >= cubes[index + 1]:
        index += 1;    
    while index < n_of_Cubes -1  and cubes[index] <= cubes[index + 1]:
        index += 1;
    print("Yes" if index == n_of_Cubes - 1 else "No"); 
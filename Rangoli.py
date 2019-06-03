'''
Created on 14-May-2019

@author: Sanjay Ghosh
'''
import array;

alphabet = [];
alphabet.append('a');
alphabet.append('b');
alphabet.append('c');
alphabet.append('d');
alphabet.append('e');
alphabet.append('f');
alphabet.append('g');
alphabet.append('h');
alphabet.append('i');
alphabet.append('j');
alphabet.append('k');
alphabet.append('l');
alphabet.append('m');
alphabet.append('n');
alphabet.append('o');
alphabet.append('p');
alphabet.append('q');
alphabet.append('r');
alphabet.append('s');
alphabet.append('t');
alphabet.append('u');
alphabet.append('v');
alphabet.append('w');
alphabet.append('x');
alphabet.append('y');
alphabet.append('z');

def isRowValid(row, size, constant):
    if row == 2 * (size - 1) - constant or row == constant:
        return True;
    else :
        return False;
    
def x_format(size, row, my_str):
    mid = size * 2 - 2;
    if isRowValid(row, size, 0) :
        alpha = size - 1;
        for j in range(0, 1, 2):
            my_str = my_str[ 0 : mid + j ] + alphabet[ alpha ] + my_str[ mid + 1 - j :];
        
    if isRowValid(row, size, 1) :
        alpa = size - 2;        
        for j in range(0, 3, 2):
            my_str = my_str[ 0 : mid + j ] + alphabet[ alpa ] + my_str[ mid + 1 + j :];
            my_str = my_str[ 0 : mid - j ] + alphabet[ alpa ] + my_str[ mid + 1 - j :];
            alpa = alpa + 1;      
        
        
    if isRowValid(row, size, 2) :
        alpa = size - 3;        
        for j in range(0, 5, 2):
            my_str = my_str[ 0 : mid + j ] + alphabet[ alpa ] + my_str[ mid + 1 + j :];
            my_str = my_str[ 0 : mid - j ] + alphabet[ alpa ] + my_str[ mid + 1 - j :];
            alpa = alpa + 1;       
        
    return my_str;

def print_rangoli(size):
    # your code goes here
    outer = 2 * (size - 1) + 1;    
    for row in range(outer):
        my_str = '-';
        inner = 2 * ( outer - 1 ) + 1;         
        for j in range(1, inner):
            my_str = my_str + '-';
        print(x_format(size, row, my_str));


if __name__ == '__main__':
    print_rangoli(int(input()));    